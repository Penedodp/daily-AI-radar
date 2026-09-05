from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import defaultdict
import json
import re

from providers.registry import collect_all
from providers.openrouter_routes import fetch_routes
from filters import is_relevant_text_model
from normalize import canonicalize_with_confidence
from quality_bench import fetch_aider_leaderboard, fetch_lmarena_webdev, match_models as match_bench_models
from scoring import (
    costs_by_task, weighted_daily_cost, price_change, value_score,
    is_free, compute_pricing_status, has_known_price,
)
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
        "pricing_status": row.get("pricing_status"),
        "identity_confidence": row.get("identity_confidence"),
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
            result["quality_source_label"] = row["quality"].get("source_label")
            result["quality_match_type"] = row["quality"].get("match_type")
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
            and has_known_price(r)
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
        if has_known_price(r) and not is_free(r):
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

def build_explorer(models):
    """One entry per canonical model (not per route), for the Model Explorer /
    search / compare UI. Cheapest known-price route is shown by default; every
    route the model has is kept in `routes` for the expandable detail view."""
    groups = defaultdict(list)
    for r in models:
        groups[r["canonical_model"]].append(r)

    out = []
    for canonical, rows in groups.items():
        priced = [r for r in rows if has_known_price(r)]
        rows_sorted = sorted(priced, key=lambda r: r["weighted_cost"]) or rows
        best = rows_sorted[0]
        q = best.get("quality") or {}
        out.append({
            "model": canonical,
            "routes": [
                {
                    "provider": r["provider"],
                    "raw_model": r["model_id"],
                    "pricing_status": r.get("pricing_status"),
                    "input": round(r["input_usd_per_million"], 6),
                    "output": round(r["output_usd_per_million"], 6),
                    "weighted_cost": round(r["weighted_cost"], 6),
                    "context_length": r.get("context_length"),
                }
                for r in sorted(rows, key=lambda r: r["weighted_cost"])
            ],
            "routes_count": len(rows),
            "best_provider": best["provider"],
            "input": round(best["input_usd_per_million"], 6),
            "output": round(best["output_usd_per_million"], 6),
            "weighted_cost": round(best["weighted_cost"], 6),
            "context_length": best.get("context_length"),
            "free": is_free(best),
            "pricing_status": best.get("pricing_status"),
            "quality_coding": q.get("scores", {}).get("coding"),
            "quality_source_label": q.get("source_label"),
            "quality_match_type": q.get("match_type"),
        })

    out.sort(
        key=lambda m: (
            m["quality_coding"] if m["quality_coding"] is not None else -1,
            -m["weighted_cost"],
        ),
        reverse=True,
    )
    return out

def validate_snapshot(models):
    """Cheap, non-fatal invariant checks (Fase 3/P3): a violation here means a
    bug slipped past the conservative rules elsewhere, and should be visible
    rather than silently shipped. Never blocks publishing — see the plan's
    'dato desconocido antes que conclusión falsa' principle: for the same
    reason, an unnoticed bug shouldn't block the whole daily run either."""
    warnings = []

    seen_routes = set()
    for r in models:
        key = (r["provider"], r["model_id"])
        if key in seen_routes:
            warnings.append(f"ruta duplicada: {key[0]} / {key[1]}")
        seen_routes.add(key)

    for r in models:
        for field in ("input_usd_per_million", "output_usd_per_million"):
            v = r.get(field)
            if v is None or v < 0 or v != v or v in (float("inf"), float("-inf")):
                warnings.append(f"precio inválido ({field}={v}) en {r['provider']} / {r['model_id']}")

    for r in models:
        if is_free(r) and r.get("pricing_status") not in {"free", "promotional_free"}:
            warnings.append(f"free=true sin pricing_status verificado: {r['provider']} / {r['model_id']}")

    for r in models:
        q = r.get("quality")
        if q and not (q.get("source_label") and q.get("label")):
            warnings.append(f"quality sin fuente/label trazable: {r['provider']} / {r['model_id']}")

    size_re = re.compile(r"\b(\d+(?:\.\d+)?)b\b")
    size_groups = defaultdict(set)
    for r in models:
        m = size_re.search(r["model_id"].lower())
        if m:
            size_groups[r["canonical_model"]].add(m.group(1))
    for canonical, sizes in size_groups.items():
        if len(sizes) > 1:
            warnings.append(f"tamaños de modelo distintos bajo el mismo canonical '{canonical}': {sorted(sizes)}")

    return warnings

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

    aider_cache = data_dir / "benchmarks" / "aider_polyglot.json"
    aider_entries, aider_status = fetch_aider_leaderboard(aider_cache)
    provider_status["aider_polyglot"] = {"status": aider_status, "count": len(aider_entries)}

    arena_cache = data_dir / "benchmarks" / "lmarena_webdev.json"
    arena_entries, arena_status = fetch_lmarena_webdev(arena_cache)
    provider_status["lmarena_webdev"] = {"status": arena_status, "count": len(arena_entries)}

    def bench_match_union(rows):
        """Aider first (objective pass/fail correctness test); LMArena WebDev
        Arena (crowd Elo, broader/faster coverage) fills in whatever Aider misses."""
        arena_matches = match_bench_models(arena_entries, rows, "lmarena_webdev")
        aider_matches = match_bench_models(aider_entries, rows, "aider_polyglot")
        return {**arena_matches, **aider_matches}

    # OpenRouter underlying routes: track only useful/scored model IDs, not all 400+.
    openrouter_only = [r for r in raw_rows if r["source"] == "openrouter"]
    bench_candidates = bench_match_union(openrouter_only)
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
    bench_matches = bench_match_union(raw_rows)

    models = []
    filtered = 0
    task_profiles = config.get("task_profiles", {})
    anchor = config.get("value_cost_anchor_usd", 0.05)

    for row in raw_rows:
        ok, _reason = is_relevant_text_model(row, config)
        if not ok:
            filtered += 1
            continue

        row["canonical_model"], row["identity_confidence"] = canonicalize_with_confidence(row["model_id"], aliases)
        row["pricing_status"] = compute_pricing_status(row)

        bench_q = bench_matches.get(route_key(row))
        row["quality"] = None
        if bench_q:
            row["quality"] = {
                "label": bench_q["label"],
                "confidence": f"auto:{bench_q['source']}",
                "source_label": bench_q.get("source_label", bench_q["source"]),
                "scores": dict(bench_q["scores"]),
                "match_ratio": bench_q.get("match_ratio"),
                "match_type": bench_q.get("match_type"),
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
            if r.get("pricing_status") != "paid":
                continue  # price moves are only meaningful for verifiably-paid routes
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

    PRICE_SOURCES = {"openrouter", "cheaperinference", "together", "novita", "openrouter_routes"}
    BENCH_SOURCES = {"aider_polyglot", "lmarena_webdev"}
    explorer = build_explorer(models)
    validation_warnings = validate_snapshot(models)
    if validation_warnings:
        print(f"[WARN] validate_snapshot: {len(validation_warnings)} aviso(s):")
        for w in validation_warnings:
            print(f"  - {w}")

    snapshot = {
        "generated_at": now.isoformat(),
        "provider_status": provider_status,
        "stats": {
            "raw_rows": len(raw_rows),
            "models_kept": len(models),
            "models_filtered": filtered,
            "unique_models": len({r["canonical_model"] for r in models}),
            "providers_with_data": sum(
                1 for k, s in provider_status.items() if k in PRICE_SOURCES and s.get("count", 0) > 0
            ),
            "benchmarks_active": sum(
                1 for k, s in provider_status.items() if k in BENCH_SOURCES and s.get("count", 0) > 0
            ),
            "scored_routes": sum(1 for r in models if r.get("quality")),
        },
        "recommendations": recs,
        "cross_provider_opportunities": opportunities,
        "changes": {"drops": drops, "increases": increases},
        "models": models,
        "explorer": explorer,
        "validation_warnings": validation_warnings,
    }

    (data_dir / f"{day}.json").write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    lines = [
        f"# AI Price Radar — {day}",
        "",
        f"> Generado {now.strftime('%d/%m/%Y %H:%M %Z')} · "
        f"**{snapshot['stats']['unique_models']} modelos únicos** · "
        f"**{len(models)} rutas/precios** · "
        f"**{snapshot['stats']['providers_with_data']} proveedores de precios** · "
        f"**{snapshot['stats']['benchmarks_active']} benchmarks activos** · "
        f"**{snapshot['stats']['scored_routes']} rutas puntuadas**.",
        "",
        "_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: "
        "30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._",
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
        "| Uso | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad* | Radar Value** |",
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
        "## 🧠 Mayor puntuación entre modelos de pago con benchmark disponible",
        "",
        "| Uso | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad* |",
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
        "\\* *Calidad (coding) = pass-rate del Aider Polyglot Leaderboard (prioritario) o, si no está, "
        "rating Elo de LMArena WebDev Arena (respaldo con más cobertura), escalados a 0–10 y emparejados "
        "automáticamente por nombre de modelo (sin intervención manual). "
        "Aider y LMArena miden cosas distintas (corrección de código vs. preferencia humana en apps web) "
        "y sus puntuaciones **no son directamente comparables entre sí** — la fuente exacta va siempre junto al dato. "
        "Cuando no hay match fiable en ninguna de las dos, el modelo queda sin puntuar en vez de estimarse.*",
        "",
        f"\\*\\* *Radar Value es un índice propio (no un benchmark) que combina calidad medida y coste estimado: "
        f"`calidad × 10 / sqrt(1 + coste_tarea / {config.get('value_cost_anchor_usd', 0.05)})`. "
        f"El ancla de {config.get('value_cost_anchor_usd', 0.05)} USD/tarea es el punto en el que empieza a penalizar "
        f"el coste; es configurable en `config.json`.*",
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
                f"Radar Value {r.get('value_score','—')}"
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
        "- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key: "
        "**Aider Polyglot Leaderboard** (test de corrección fijo, prioritario cuando existe) y "
        "**LMArena WebDev Arena** (ranking Elo por voto humano, respaldo con cobertura mucho más amplia "
        "y rápida para modelos recién publicados). No requiere mantenimiento manual. "
        "**Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada "
        "igual de fiable — se añadirán cuando se identifique una.",
    ]

    ai = generate_summary(snapshot, config)
    if ai:
        lines += ["", "## 🤖 Estrategia recomendada para hoy", "", ai]

    report = "\n".join(lines) + "\n"
    (reports_dir / f"{day}.md").write_text(report, encoding="utf-8")
    (reports_dir / "latest.md").write_text(report, encoding="utf-8")

    dashboard = build_html(
        snapshot, day, has_previous=bool(previous), ai_summary=ai,
        price_trends=price_trends, config=config,
    )
    (docs_dir / "index.html").write_text(dashboard, encoding="utf-8")

    try:
        print(report)
    except UnicodeEncodeError:
        # Some local consoles (Windows cp1252) can't render emoji; the report
        # files are already written above, so this is display-only.
        print(report.encode("ascii", "replace").decode("ascii"))

if __name__ == "__main__":
    main()
