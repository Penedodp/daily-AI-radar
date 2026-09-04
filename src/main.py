from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import defaultdict
import json

from providers.registry import collect_all
from providers.openrouter_routes import fetch_routes
from filters import is_relevant_text_model
from normalize import canonicalize
from quality_bench import fetch_leaderboard, match_models as match_bench_models
from scoring import costs_by_task, weighted_daily_cost, price_change, value_score, is_free
from report_ai import generate_summary
from report_html import build_html

ROOT = Path(__file__).resolve().parents[1]
LABELS = {
    "coding": "💻 Coding",
    "agentic": "🤖 Agentic coding",
    "reasoning": "🧠 Razonamiento",
    "general": "⚡ General",
}

def load_json(path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))

def previous_snapshot(data_dir, today):
    candidates = [p for p in sorted(data_dir.glob("*.json"), reverse=True) if p.stem != today]
    return load_json(candidates[0], {}) if candidates else None

def price_trend(data_dir, today, canonical_model, limit=14):
    """Cheapest weighted_cost for `canonical_model` on each of the last
    `limit` days (oldest first), read straight from the committed snapshots."""
    files = [p for p in sorted(data_dir.glob("*.json")) if p.stem != today][-limit:]
    points = []
    for p in files:
        snap = load_json(p, None)
        if not snap:
            continue
        best = None
        for r in snap.get("models", []):
            if r.get("canonical_model") != canonical_model:
                continue
            cost = r.get("weighted_cost")
            if cost is not None and (best is None or cost < best):
                best = cost
        if best is not None:
            points.append({"date": p.stem, "cost": best})
    return points

def route_key(row):
    return f"{row.get('provider','')}::{row.get('model_id','')}"

def previous_map(snapshot):
    out = {}
    for r in (snapshot or {}).get("models", []):
        out[route_key(r)] = r
    return out

def compact(row, category=None):
    result = {
        "model": row["canonical_model"],
        "raw_model": row["model_id"],
        "provider": row["provider"],
        "source": row["source"],
        "free": is_free(row),
        "input": round(row["input_usd_per_million"], 6),
        "output": round(row["output_usd_per_million"], 6),
        "weighted_cost": round(row["weighted_cost"], 6),
    }
    if category:
        result["task_cost"] = round(row["costs_by_task"][category], 6)
        if row.get("quality"):
            result["quality_score"] = row["quality"]["scores"].get(category)
            result["value_score"] = row["value_scores"].get(category)
            result["quality_label"] = row["quality"].get("label")
            result["quality_match_ratio"] = row["quality"].get("match_ratio")
    if row.get("change_pct") is not None:
        result["change_pct"] = round(row["change_pct"], 1)
    return result

def dedup_by_model(rows, limit):
    """Keep the first (best-ranked) route per canonical model, so a model with
    many provider routes doesn't flood a top-N list on its own."""
    seen = set()
    out = []
    for r in rows:
        if r["canonical_model"] in seen:
            continue
        seen.add(r["canonical_model"])
        out.append(r)
        if len(out) >= limit:
            break
    return out

def recommendations(models, config):
    recs = {}
    for category in LABELS:
        scored = [
            r for r in models
            if r.get("quality") and r["quality"]["scores"].get(category) is not None
        ]
        free = [r for r in scored if is_free(r)]
        paid = [r for r in scored if not is_free(r)]

        min_q = config.get("paid_min_quality", {}).get(category, 0)
        paid_good = [
            r for r in paid
            if r["quality"]["scores"].get(category, 0) >= min_q
        ]

        free.sort(
            key=lambda r: (
                r["quality"]["scores"].get(category, 0),
                r.get("context_length") or 0,
            ),
            reverse=True,
        )
        paid_good.sort(
            key=lambda r: (
                r["value_scores"].get(category) or -1,
                r["quality"]["scores"].get(category, 0),
            ),
            reverse=True,
        )
        paid_quality = sorted(
            paid,
            key=lambda r: r["quality"]["scores"].get(category, 0),
            reverse=True,
        )

        recs[category] = {
            "best_free": compact(free[0], category) if free else None,
            "best_paid_value": compact(paid_good[0], category) if paid_good else None,
            "best_paid_quality": compact(paid_quality[0], category) if paid_quality else None,
            "top_paid_value": [compact(r, category) for r in dedup_by_model(paid_good, 5)],
            "top_free": [compact(r, category) for r in dedup_by_model(free, 5)],
        }
    return recs

def cross_provider_opportunities(models, config):
    groups = defaultdict(list)
    for r in models:
        if not is_free(r):
            groups[r["canonical_model"]].append(r)

    opportunities = []
    for canonical, routes in groups.items():
        providers = {r["provider"] for r in routes}
        if len(providers) < 2:
            continue

        # Deduplicate identical provider/model rows; keep cheapest weighted route.
        best_by_provider = {}
        for r in routes:
            current = best_by_provider.get(r["provider"])
            if current is None or r["weighted_cost"] < current["weighted_cost"]:
                best_by_provider[r["provider"]] = r
        routes = list(best_by_provider.values())
        if len(routes) < 2:
            continue

        routes.sort(key=lambda r: r["weighted_cost"])
        cheapest, second = routes[0], routes[1]
        if second["weighted_cost"] <= 0:
            continue
        saving = (1 - cheapest["weighted_cost"] / second["weighted_cost"]) * 100
        if saving < config.get("cross_provider_min_saving_pct", 5):
            continue

        q = cheapest.get("quality")
        opportunities.append({
            "model": canonical,
            "cheapest": compact(cheapest),
            "next": compact(second),
            "saving_vs_next_pct": round(saving, 1),
            "routes_count": len(routes),
            "quality": q["scores"] if q else None,
        })

    opportunities.sort(
        key=lambda x: (
            x.get("saving_vs_next_pct", 0),
            max((x.get("quality") or {}).values() or [0]),
        ),
        reverse=True,
    )
    return opportunities

def main():
    config = load_json(ROOT / "config.json", {})
    aliases = load_json(ROOT / "model_aliases.json", {"rules": []})

    now = datetime.now(ZoneInfo(config.get("timezone", "Europe/Lisbon")))
    day = now.date().isoformat()

    data_dir = ROOT / "data"
    reports_dir = ROOT / "reports"
    docs_dir = ROOT / "docs"
    data_dir.mkdir(exist_ok=True)
    reports_dir.mkdir(exist_ok=True)
    docs_dir.mkdir(exist_ok=True)

    previous = previous_snapshot(data_dir, day)
    prev_map = previous_map(previous)

    raw_rows, provider_status = collect_all(config)

    bench_cache = data_dir / "benchmarks" / "aider_polyglot.json"
    bench_entries, bench_status = fetch_leaderboard(bench_cache)
    provider_status["aider_polyglot"] = {"status": bench_status, "count": len(bench_entries)}

    # OpenRouter underlying routes: track only useful/scored model IDs, not all 400+.
    openrouter_only = [r for r in raw_rows if r["source"] == "openrouter"]
    bench_candidates = match_bench_models(bench_entries, openrouter_only)
    openrouter_candidates = []
    seen = set()
    for r in openrouter_only:
        if route_key(r) in bench_candidates and r["model_id"] not in seen:
            openrouter_candidates.append(r["model_id"])
            seen.add(r["model_id"])

    route_cfg = config.get("providers", {}).get("openrouter_routes", {})
    if route_cfg.get("enabled", True):
        try:
            route_rows, route_status = fetch_routes(
                openrouter_candidates,
                config.get("route_tracking_max_models", 35),
            )
            raw_rows.extend(route_rows)
            provider_status["openrouter_routes"] = {
                "status": route_status,
                "count": len(route_rows),
            }
        except Exception as exc:
            provider_status["openrouter_routes"] = {
                "status": "error",
                "count": 0,
                "error": f"{type(exc).__name__}: {str(exc)[:180]}",
            }

    # Final bench match over the full row set (openrouter + routes + other providers),
    # now that all sources/routes have been collected.
    bench_matches = match_bench_models(bench_entries, raw_rows)

    models = []
    filtered = 0
    task_profiles = config.get("task_profiles", {})
    anchor = config.get("value_cost_anchor_usd", 0.05)

    for row in raw_rows:
        ok, _reason = is_relevant_text_model(row, config)
        if not ok:
            filtered += 1
            continue

        row["canonical_model"] = canonicalize(row["model_id"], aliases)

        bench_q = bench_matches.get(route_key(row))
        row["quality"] = None
        if bench_q:
            row["quality"] = {
                "label": bench_q["label"],
                "confidence": f"auto:{bench_q['source']}",
                "scores": dict(bench_q["scores"]),
                "match_ratio": bench_q.get("match_ratio"),
            }

        row["costs_by_task"] = costs_by_task(row, task_profiles)
        row["weighted_cost"] = weighted_daily_cost(row, task_profiles)
        row["value_scores"] = {}
        if row["quality"]:
            for category in LABELS:
                row["value_scores"][category] = value_score(
                    row["quality"]["scores"].get(category),
                    row["costs_by_task"][category],
                    anchor,
                )

        old = prev_map.get(route_key(row))
        row["change_pct"] = price_change(
            row["weighted_cost"],
            old.get("weighted_cost") if old else None,
        )
        models.append(row)

    # Detect same-route historical changes. Cross-provider differences are NOT called discounts.
    drops, increases = [], []
    if previous:
        threshold_down = -abs(config.get("discount_threshold_pct", 10))
        threshold_up = abs(config.get("price_increase_threshold_pct", 10))
        for r in models:
            ch = r.get("change_pct")
            if ch is not None and ch <= threshold_down:
                drops.append(compact(r))
            elif ch is not None and ch >= threshold_up:
                increases.append(compact(r))
    drops.sort(key=lambda x: x["change_pct"])
    increases.sort(key=lambda x: x["change_pct"], reverse=True)

    recs = recommendations(models, config)
    opportunities = cross_provider_opportunities(models, config)

    # Categories with at least one automated/manual quality score. Categories
    # without a benchmark source yet (agentic/reasoning/general, for now) get
    # an explanatory note in the report instead of empty rows.
    scored_categories = {
        cat for cat in LABELS
        if any(r.get("quality") and r["quality"]["scores"].get(cat) is not None for r in models)
    }
    NO_BENCH_NOTE = "_Sin benchmark automatizado disponible todavía para esta categoría._"

    # Price history of today's featured "best value" pick per category, for the dashboard sparkline.
    price_trends = {}
    for cat in scored_categories:
        pick = recs[cat]["best_paid_value"]
        if not pick:
            continue
        points = price_trend(data_dir, day, pick["model"])
        points.append({"date": day, "cost": pick["weighted_cost"]})
        if len(points) >= 2:
            price_trends[cat] = {"model": pick["model"], "points": points}

    snapshot = {
        "generated_at": now.isoformat(),
        "provider_status": provider_status,
        "stats": {
            "raw_rows": len(raw_rows),
            "models_kept": len(models),
            "models_filtered": filtered,
            "providers_with_data": sum(1 for s in provider_status.values() if s.get("count", 0) > 0),
            "scored_routes": sum(1 for r in models if r.get("quality")),
        },
        "recommendations": recs,
        "cross_provider_opportunities": opportunities,
        "changes": {"drops": drops, "increases": increases},
        "models": models,
    }

    (data_dir / f"{day}.json").write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    lines = [
        f"# AI Price Radar — {day}",
        "",
        f"> **{len(models)} rutas/modelos** útiles · "
        f"**{snapshot['stats']['providers_with_data']} fuentes con datos** · "
        f"**{snapshot['stats']['scored_routes']} rutas puntuadas**.",
        "",
        "## 📡 Fuentes",
        "",
        "| Fuente | Estado | Registros |",
        "|---|---|---:|",
    ]
    for name, status in provider_status.items():
        state = status.get("status", "unknown")
        lines.append(f"| {name} | `{state}` | {status.get('count', 0)} |")

    lines += [
        "",
        "## 🆓 Mejor opción gratuita",
        "",
        "| Uso | Modelo | Calidad* | Proveedor/ruta | $/M input | $/M output |",
        "|---|---|---:|---|---:|---:|",
    ]
    for cat, label in LABELS.items():
        if cat not in scored_categories:
            lines.append(f"| {label} | {NO_BENCH_NOTE} | | | | |")
            continue
        r = recs[cat]["best_free"]
        if r:
            lines.append(
                f"| {label} | **{r['model']}** | {r.get('quality_score','—')}/10 | {r['provider']} | "
                f"${r['input']:.4f} | ${r['output']:.4f} |"
            )
        else:
            lines.append(f"| {label} | — | — | — | — | — |")

    lines += [
        "",
        "## 💰 Mejor relación calidad/precio DE PAGO",
        "",
        "| Uso | Modelo | Proveedor/ruta | Coste/tarea | $/M input | $/M output | Calidad* | Value |",
        "|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for cat, label in LABELS.items():
        if cat not in scored_categories:
            lines.append(f"| {label} | {NO_BENCH_NOTE} | | | | | | |")
            continue
        r = recs[cat]["best_paid_value"]
        if r:
            lines.append(
                f"| {label} | **{r['model']}** | **{r['provider']}** | "
                f"${r['task_cost']:.5f} | ${r['input']:.4f} | ${r['output']:.4f} | "
                f"{r.get('quality_score','—')}/10 | {r.get('value_score','—')} |"
            )
        else:
            lines.append(f"| {label} | — | — | — | — | — | — | — |")

    lines += [
        "",
        "## 🧠 Opción premium por calidad",
        "",
        "| Uso | Modelo | Proveedor/ruta | Coste/tarea | $/M input | $/M output | Calidad* |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for cat, label in LABELS.items():
        if cat not in scored_categories:
            lines.append(f"| {label} | {NO_BENCH_NOTE} | | | | | |")
            continue
        r = recs[cat]["best_paid_quality"]
        if r:
            lines.append(
                f"| {label} | **{r['model']}** | {r['provider']} | "
                f"${r['task_cost']:.5f} | ${r['input']:.4f} | ${r['output']:.4f} | "
                f"{r.get('quality_score','—')}/10 |"
            )
        else:
            lines.append(f"| {label} | — | — | — | — | — | — |")

    lines += [
        "",
        "\\* *Calidad (coding) = pass-rate del Aider Polyglot Leaderboard escalado a 0–10, "
        "emparejado automáticamente por nombre de modelo (sin intervención manual). "
        "Cuando no hay match fiable, el modelo queda sin puntuar en vez de estimarse.*",
        "",
        "## 🔀 Mismo modelo, proveedor/ruta más barata",
        "",
    ]
    if opportunities:
        lines += [
            "| Modelo | Más barato | Coste perfil | $/M input | $/M output | Siguiente | Ahorro vs siguiente |",
            "|---|---|---:|---:|---:|---|---:|",
        ]
        for o in opportunities[:15]:
            a, b = o["cheapest"], o["next"]
            lines.append(
                f"| **{o['model']}** | **{a['provider']}** | ${a['weighted_cost']:.5f} | "
                f"${a['input']:.4f} | ${a['output']:.4f} | "
                f"{b['provider']} (${b['weighted_cost']:.5f}) | **{o['saving_vs_next_pct']:.1f}%** |"
            )
    else:
        lines.append(
            "Aún no hay suficientes fuentes configuradas con el mismo modelo, "
            "o no hay diferencias ≥ al umbral."
        )

    lines += ["", "## 🏆 Top 5 DE PAGO por calidad/precio", ""]
    for cat, label in LABELS.items():
        lines.append(f"### {label}")
        if cat not in scored_categories:
            lines.append(f"- {NO_BENCH_NOTE}")
            lines.append("")
            continue
        top = recs[cat]["top_paid_value"]
        if not top:
            lines.append("- Sin candidatos de pago que superen el mínimo de calidad configurado.")
        for i, r in enumerate(top, 1):
            lines.append(
                f"{i}. **{r['model']}** vía **{r['provider']}** — "
                f"calidad {r.get('quality_score','—')}/10 · "
                f"coste/tarea ${r['task_cost']:.5f} "
                f"(\\${r['input']:.4f} in / \\${r['output']:.4f} out) · "
                f"value {r.get('value_score','—')}"
            )
        lines.append("")

    lines += ["## 🔥 Bajadas reales de precio", ""]
    if not previous:
        lines.append("Todavía no hay snapshot de un día anterior para comparar.")
    elif drops:
        for r in drops[:12]:
            lines.append(
                f"- **{r['model']}** vía **{r['provider']}** — **{r['change_pct']:.1f}%** "
                f"(ahora \\${r['input']:.4f} in / \\${r['output']:.4f} out)"
            )
    else:
        lines.append("- No se detectaron bajadas ≥ al umbral en la misma ruta/proveedor.")

    if increases:
        lines += ["", "### Subidas", ""]
        for r in increases[:8]:
            lines.append(
                f"- **{r['model']}** vía **{r['provider']}** — +{r['change_pct']:.1f}% "
                f"(ahora \\${r['input']:.4f} in / \\${r['output']:.4f} out)"
            )

    lines += [
        "",
        "## 🧪 Notas",
        "",
        "- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.",
        "- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.",
        "- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico.",
        "- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.",
        "- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.",
        "- La calidad de **coding** se obtiene automáticamente del Aider Polyglot Leaderboard "
        "(fuente pública, sin API key) y no requiere mantenimiento manual. "
        "**Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada "
        "igual de fiable — se añadirán cuando se identifique una.",
    ]

    ai = generate_summary(snapshot, config)
    if ai:
        lines += ["", "## 🤖 Estrategia recomendada para hoy", "", ai]

    report = "\n".join(lines) + "\n"
    (reports_dir / f"{day}.md").write_text(report, encoding="utf-8")
    (reports_dir / "latest.md").write_text(report, encoding="utf-8")

    dashboard = build_html(snapshot, day, has_previous=bool(previous), ai_summary=ai, price_trends=price_trends)
    (docs_dir / "index.html").write_text(dashboard, encoding="utf-8")

    print(report)

if __name__ == "__main__":
    main()
