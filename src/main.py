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
from quality_bench import (
    fetch_aider_leaderboard, fetch_lmarena_webdev,
    match_models as match_bench_models, SOURCE_LABELS,
)
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
# Which bench sources can score which category. Every source in the plan
# today only measures coding; declared as a map (not a constant) so a future
# benchmark for another category is a one-line addition, not a rewrite.
CATEGORY_SOURCES = {
    "coding": ["aider_polyglot", "lmarena_webdev"],
}
NO_BENCH_NOTE = "_Sin benchmark automatizado disponible todavía para esta categoría._"

def load_json(path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))

def previous_snapshot(data_dir, today):
    candidates = [p for p in sorted(data_dir.glob("*.json"), reverse=True) if p.stem != today]
    if not candidates:
        return None, None
    return load_json(candidates[0], {}), candidates[0].stem

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

def dedup_exact_routes(raw_rows):
    """Exact-duplicate rows (same provider + model id + route/quantization)
    must never reach the snapshot — two identical rows would silently double
    a model's presence in every table. Keeps the first occurrence."""
    seen = set()
    deduped = []
    duplicates = 0
    for r in raw_rows:
        meta = r.get("metadata") or {}
        key = (r.get("provider"), r.get("model_id"), meta.get("route_tag"), meta.get("quantization"))
        if key in seen:
            duplicates += 1
            continue
        seen.add(key)
        deduped.append(r)
    return deduped, duplicates

def compact(row, category=None, source=None):
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
        "context_length": row.get("context_length"),
    }
    if category and source:
        q = (row.get("quality_by_source") or {}).get(source)
        result["task_cost"] = round(row["costs_by_task"][category], 6)
        if q:
            result["quality_score"] = q["scores"].get(category)
            result["quality_raw"] = q.get("raw_score")
            result["quality_raw_unit"] = q.get("raw_unit")
            result["quality_label"] = q.get("label")
            result["quality_match_ratio"] = q.get("match_ratio")
            result["quality_match_type"] = q.get("match_type")
            result["quality_source"] = source
            result["quality_source_label"] = q.get("source_label")
            result["quality_source_url"] = q.get("source_url")
            result["quality_captured_at"] = q.get("captured_at")
            result["value_score"] = (row.get("value_scores") or {}).get(source, {}).get(category)
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
    """One independent ranking per (category, benchmark source). Aider and
    WebDev Arena never rank against each other — see
    DAILY_AI_RADAR_CONTINUACION_AUDITORIA_2.md #2."""
    recs = {}
    for category in LABELS:
        cat_out = {"sources": {}}
        for source in CATEGORY_SOURCES.get(category, []):
            scored = [
                r for r in models
                if has_known_price(r)
                and (r.get("quality_by_source") or {}).get(source)
                and r["quality_by_source"][source]["scores"].get(category) is not None
            ]
            if not scored:
                continue
            free = [r for r in scored if is_free(r)]
            paid = [r for r in scored if not is_free(r)]

            min_q = config.get("paid_min_quality", {}).get(category, 0)
            paid_good = [
                r for r in paid
                if r["quality_by_source"][source]["scores"].get(category, 0) >= min_q
            ]

            free.sort(
                key=lambda r: (
                    r["quality_by_source"][source]["scores"].get(category, 0),
                    r.get("context_length") or 0,
                ),
                reverse=True,
            )
            paid_good.sort(
                key=lambda r: (
                    (r.get("value_scores") or {}).get(source, {}).get(category) or -1,
                    r["quality_by_source"][source]["scores"].get(category, 0),
                ),
                reverse=True,
            )
            paid_quality = sorted(
                paid,
                key=lambda r: r["quality_by_source"][source]["scores"].get(category, 0),
                reverse=True,
            )

            cat_out["sources"][source] = {
                "source_label": SOURCE_LABELS.get(source, source),
                "best_free": compact(free[0], category, source) if free else None,
                "best_paid_value": compact(paid_good[0], category, source) if paid_good else None,
                "best_paid_quality": compact(paid_quality[0], category, source) if paid_quality else None,
                "top_paid_value": [compact(r, category, source) for r in dedup_by_model(paid_good, 5)],
                "top_free": [compact(r, category, source) for r in dedup_by_model(free, 5)],
            }
        recs[category] = cat_out
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

        # Quality is informational here, per-source, never a ranking key —
        # combining Aider/WebDev into one number would repeat the mistake
        # this phase fixes elsewhere.
        quality_by_source = {
            source: q["scores"].get("coding")
            for source, q in (cheapest.get("quality_by_source") or {}).items()
            if q.get("scores", {}).get("coding") is not None
        }
        opportunities.append({
            "model": canonical,
            "cheapest": compact(cheapest),
            "next": compact(second),
            "saving_vs_next_pct": round(saving, 1),
            "routes_count": len(routes),
            "quality_by_source": quality_by_source or None,
        })

    # Ranked purely by saving — never by a cross-benchmark quality tiebreak.
    opportunities.sort(key=lambda x: x.get("saving_vs_next_pct", 0), reverse=True)
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
        quality_by_source = {
            source: {
                "score": q["scores"].get("coding"),
                "source_label": q.get("source_label"),
                "raw_score": q.get("raw_score"),
                "raw_unit": q.get("raw_unit"),
                "match_type": q.get("match_type"),
            }
            for source, q in (best.get("quality_by_source") or {}).items()
            if q.get("scores", {}).get("coding") is not None
        }
        search_bits = {best["provider"]} | {r["provider"] for r in rows} | {
            (r.get("metadata") or {}).get("quantization") for r in rows
        }
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
                    "quantization": (r.get("metadata") or {}).get("quantization"),
                    "latency_p50": (r.get("metadata") or {}).get("latency_p50"),
                    "throughput_p50": (r.get("metadata") or {}).get("throughput_p50"),
                    "uptime_last_1d": (r.get("metadata") or {}).get("uptime_last_1d"),
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
            "quality_by_source": quality_by_source,
            "search_text": " ".join(str(s) for s in search_bits if s).lower(),
        })

    def best_score(m):
        scores = [q["score"] for q in m["quality_by_source"].values() if q["score"] is not None]
        return max(scores) if scores else -1

    out.sort(key=lambda m: (best_score(m), -m["weighted_cost"]), reverse=True)
    return out

def validate_snapshot(models):
    """Two-tier invariant checks (Fase 6 §6): ERRORs mean a bug slipped past
    the conservative rules elsewhere and must block publishing (the daily
    workflow exits non-zero and the commit/push step never runs). WARNINGs
    are expected, routine conditions (an unscored model, an unknown price)
    that are worth surfacing but must never stop the run — see the plan's
    'mostrar el dato en vez de ocultarlo' principle."""
    errors, warnings = [], []

    seen_routes = set()
    for r in models:
        meta = r.get("metadata") or {}
        key = (r["provider"], r["model_id"], meta.get("route_tag"), meta.get("quantization"))
        if key in seen_routes:
            errors.append(f"ruta exacta duplicada tras deduplicar: {key}")
        seen_routes.add(key)

    for r in models:
        for field in ("input_usd_per_million", "output_usd_per_million"):
            v = r.get(field)
            if v is None or v < 0 or v != v or v in (float("inf"), float("-inf")):
                errors.append(f"precio inválido ({field}={v}) en {r['provider']} / {r['model_id']}")

    for r in models:
        if is_free(r) and r.get("pricing_status") not in {"free", "promotional_free"}:
            errors.append(f"free=true sin pricing_status verificado: {r['provider']} / {r['model_id']}")

    for r in models:
        for source, q in (r.get("quality_by_source") or {}).items():
            if not (q.get("source_label") and q.get("label")):
                errors.append(f"quality sin fuente/label trazable: {r['provider']} / {r['model_id']} ({source})")

    size_re = re.compile(r"\b(\d+(?:\.\d+)?)b\b")
    size_groups = defaultdict(set)
    for r in models:
        m = size_re.search(r["model_id"].lower())
        if m:
            size_groups[r["canonical_model"]].add(m.group(1))
    for canonical, sizes in size_groups.items():
        if len(sizes) > 1:
            errors.append(f"tamaños de modelo distintos bajo el mismo canonical '{canonical}': {sorted(sizes)}")

    unknown_count = sum(1 for r in models if r.get("pricing_status") == "unknown")
    if unknown_count:
        warnings.append(f"{unknown_count} ruta(s) con precio 'unknown' (no entran en ningún ranking por coste)")

    unscored_count = sum(1 for r in models if not r.get("quality_by_source"))
    if unscored_count:
        warnings.append(f"{unscored_count} ruta(s) sin ningún benchmark de coding todavía")

    return errors, warnings

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

    previous, previous_day = previous_snapshot(data_dir, day)
    prev_map = previous_map(previous)

    raw_rows, provider_status = collect_all(config)

    aider_cache = data_dir / "benchmarks" / "aider_polyglot.json"
    aider_entries, aider_status, aider_captured_at = fetch_aider_leaderboard(aider_cache)
    provider_status["aider_polyglot"] = {"status": aider_status, "count": len(aider_entries)}

    arena_cache = data_dir / "benchmarks" / "lmarena_webdev.json"
    arena_entries, arena_status, arena_captured_at = fetch_lmarena_webdev(arena_cache)
    provider_status["lmarena_webdev"] = {"status": arena_status, "count": len(arena_entries)}

    captured_at_by_source = {"aider_polyglot": aider_captured_at, "lmarena_webdev": arena_captured_at}

    def bench_match_by_source(rows):
        """Aider and WebDev Arena matched independently and kept separate —
        never merged into one field. A route can have a score from one, the
        other, both, or neither."""
        arena_matches = match_bench_models(arena_entries, rows, "lmarena_webdev")
        aider_matches = match_bench_models(aider_entries, rows, "aider_polyglot")
        out = defaultdict(dict)
        for k, v in arena_matches.items():
            out[k]["lmarena_webdev"] = v
        for k, v in aider_matches.items():
            out[k]["aider_polyglot"] = v
        return out

    # OpenRouter underlying routes: track only useful/scored model IDs, not all 400+.
    openrouter_only = [r for r in raw_rows if r["source"] == "openrouter"]
    bench_candidates = bench_match_by_source(openrouter_only)
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

    raw_rows, duplicate_routes_removed = dedup_exact_routes(raw_rows)

    # Final bench match over the full row set (openrouter + routes + other providers),
    # now that all sources/routes have been collected.
    bench_matches = bench_match_by_source(raw_rows)

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

        matches = bench_matches.get(route_key(row)) or {}
        row["quality_by_source"] = {}
        for source, bq in matches.items():
            row["quality_by_source"][source] = {
                "label": bq["label"],
                "source_label": bq.get("source_label", source),
                "source_url": bq.get("source_url"),
                "captured_at": captured_at_by_source.get(source),
                "scores": dict(bq["scores"]),
                "raw_score": bq.get("raw_score"),
                "raw_unit": bq.get("raw_unit"),
                "n_cases": bq.get("n_cases"),
                "match_ratio": bq.get("match_ratio"),
                "match_type": bq.get("match_type"),
            }

        row["costs_by_task"] = costs_by_task(row, task_profiles)
        row["weighted_cost"] = weighted_daily_cost(row, task_profiles)
        row["value_scores"] = {}
        for source, q in row["quality_by_source"].items():
            row["value_scores"][source] = {}
            for category in LABELS:
                sc = q["scores"].get(category)
                if sc is not None:
                    row["value_scores"][source][category] = value_score(
                        sc, row["costs_by_task"][category], anchor,
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

    # Price history of today's featured "best value" pick per (category, source).
    price_trends = defaultdict(dict)
    for category, cat_data in recs.items():
        for source, sdata in cat_data["sources"].items():
            pick = sdata["best_paid_value"]
            if not pick:
                continue
            points = price_trend(data_dir, day, pick["model"])
            points.append({"date": day, "cost": pick["weighted_cost"]})
            if len(points) >= 2:
                price_trends[category][source] = {
                    "model": pick["model"], "points": points,
                    "source_label": sdata["source_label"],
                }

    # openrouter_routes is telemetry about existing OpenRouter models, not an
    # independent price catalog — don't count it as a "pricing provider".
    PRICE_SOURCES = {"openrouter", "cheaperinference", "together", "novita"}
    BENCH_SOURCES = {"aider_polyglot", "lmarena_webdev"}
    explorer = build_explorer(models)

    errors, validation_warnings = validate_snapshot(models)
    for w in validation_warnings:
        print(f"[WARN] {w}")
    if errors:
        print(f"[ERROR] validate_snapshot: {len(errors)} error(es) crítico(s) — no se publica hoy:")
        for e in errors:
            print(f"  - {e}")
        raise SystemExit(1)

    snapshot = {
        "generated_at": now.isoformat(),
        "previous_snapshot_date": previous_day,
        "provider_status": provider_status,
        "stats": {
            "raw_rows": len(raw_rows) + duplicate_routes_removed,
            "duplicate_routes_removed": duplicate_routes_removed,
            "models_kept": len(models),
            "models_filtered": filtered,
            "unique_models": len({r["canonical_model"] for r in models}),
            "providers_with_data": sum(
                1 for k, s in provider_status.items() if k in PRICE_SOURCES and s.get("count", 0) > 0
            ),
            "benchmarks_active": sum(
                1 for k, s in provider_status.items() if k in BENCH_SOURCES and s.get("count", 0) > 0
            ),
            "openrouter_routes_analyzed": provider_status.get("openrouter_routes", {}).get("count", 0),
            "scored_routes": sum(1 for r in models if r.get("quality_by_source")),
            "unknown_price_routes": sum(1 for r in models if r.get("pricing_status") == "unknown"),
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

    stats = snapshot["stats"]
    lines = [
        f"# Daily AI Radar — {day}",
        "",
        f"> Generado {now.strftime('%d/%m/%Y %H:%M %Z')} · "
        f"**{stats['unique_models']} modelos únicos** · "
        f"**{len(models)} rutas/precios** · "
        f"**{stats['providers_with_data']} proveedores de precios** · "
        f"**{stats['benchmarks_active']} benchmarks activos** · "
        f"**{stats['openrouter_routes_analyzed']} rutas OpenRouter analizadas** · "
        f"**{stats['scored_routes']} rutas puntuadas**.",
        "",
        "_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: "
        "30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._",
        "",
    ]
    if stats["duplicate_routes_removed"]:
        lines.append(
            f"_{stats['duplicate_routes_removed']} ruta(s) duplicada(s) exacta(s) detectada(s) y "
            "eliminada(s) antes de publicar._"
        )
        lines.append("")
    if stats["unknown_price_routes"]:
        lines.append(
            f"_{stats['unknown_price_routes']} ruta(s) con precio `unknown` (0/0 sin señal explícita de "
            "gratis) — no entran en ningún ranking por coste._"
        )
        lines.append("")

    lines += [
        "## 📡 Fuentes",
        "",
        "| Fuente | Estado | Registros |",
        "|---|---|---:|",
    ]
    for name, status in provider_status.items():
        state = status.get("status", "unknown")
        lines.append(f"| {name} | `{state}` | {status.get('count', 0)} |")

    def cat_sources(category):
        return list(recs[category]["sources"].items())

    empty_categories = [LABELS[c] for c in LABELS if not cat_sources(c)]

    lines += [
        "",
        "## 🆓 Mejor opción gratuita puntuada",
        "",
        "| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |",
        "|---|---|---|---:|---|---:|---:|",
    ]
    any_free_row = False
    for cat in LABELS:
        for source, sdata in cat_sources(cat):
            r = sdata["best_free"]
            if not r:
                continue
            any_free_row = True
            lines.append(
                f"| {LABELS[cat]} | {sdata['source_label']} | **{r['model']}** | {r.get('quality_score','—')}/10 | "
                f"{r['provider']} | ${r['input']:.4f} | ${r['output']:.4f} |"
            )
    if not any_free_row:
        lines.append("| — | — | Ningún modelo gratuito puntuado todavía | — | — | — | — |")

    lines += [
        "",
        "## 💰 Mejor relación calidad/precio (por fuente de benchmark)",
        "",
        "| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |",
        "|---|---|---|---|---:|---:|---:|---:|---:|",
    ]
    any_value_row = False
    for cat in LABELS:
        for source, sdata in cat_sources(cat):
            r = sdata["best_paid_value"]
            if not r:
                continue
            any_value_row = True
            lines.append(
                f"| {LABELS[cat]} | {sdata['source_label']} | **{r['model']}** | **{r['provider']}** | "
                f"${r['task_cost']:.5f} | ${r['input']:.4f} | ${r['output']:.4f} | "
                f"{r.get('quality_score','—')}/10 | {r.get('value_score','—')} |"
            )
    if not any_value_row:
        lines.append("| — | — | Ningún modelo de pago supera el mínimo de calidad configurado | — | — | — | — | — |")

    lines += [
        "",
        "## 🧠 Mayor puntuación entre modelos de pago (por fuente de benchmark)",
        "",
        "| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad |",
        "|---|---|---|---|---:|---:|---:|---:|",
    ]
    any_quality_row = False
    for cat in LABELS:
        for source, sdata in cat_sources(cat):
            r = sdata["best_paid_quality"]
            if not r:
                continue
            any_quality_row = True
            lines.append(
                f"| {LABELS[cat]} | {sdata['source_label']} | **{r['model']}** | {r['provider']} | "
                f"${r['task_cost']:.5f} | ${r['input']:.4f} | ${r['output']:.4f} | "
                f"{r.get('quality_score','—')}/10 |"
            )
    if not any_quality_row:
        lines.append("| — | — | Sin candidatos de pago puntuados | — | — | — | — |")

    if empty_categories:
        lines += ["", f"_Próximamente: {' · '.join(empty_categories)} (sin benchmark automatizado todavía)._"]

    lines += [
        "",
        "\\* *Aider Polyglot Leaderboard (pass-rate de un test de corrección fijo) y LMArena WebDev Arena "
        "(rating Elo por voto humano) son benchmarks distintos, escalados a 0–10 cada uno por separado. "
        "**Nunca se ordenan entre sí como si fueran la misma escala** — cada tabla indica la fuente exacta "
        "junto al dato, no solo al pasar el ratón por encima. Emparejados automáticamente por nombre de "
        "modelo; sin match fiable, el modelo queda sin puntuar en vez de estimarse.*",
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

    lines += ["", "## 🏆 Top 5 de pago por calidad/precio (por fuente)", ""]
    any_top5 = False
    for cat in LABELS:
        for source, sdata in cat_sources(cat):
            top = sdata["top_paid_value"]
            if not top:
                continue
            any_top5 = True
            lines.append(f"### {LABELS[cat]} · {sdata['source_label']}")
            for i, r in enumerate(top, 1):
                lines.append(
                    f"{i}. **{r['model']}** vía **{r['provider']}** — "
                    f"calidad {r.get('quality_score','—')}/10 · "
                    f"coste/tarea ${r['task_cost']:.5f} "
                    f"(\\${r['input']:.4f} in / \\${r['output']:.4f} out) · "
                    f"Radar Value {r.get('value_score','—')}"
                )
            lines.append("")
    if not any_top5:
        lines.append("Sin candidatos de pago que superen el mínimo de calidad configurado.")
        lines.append("")

    if previous:
        if _is_yesterday(previous_day, day):
            changes_heading = "## 🔥 Bajadas reales de precio (vs ayer)"
        else:
            changes_heading = f"## 🔥 Bajadas reales de precio (vs último snapshot disponible · {previous_day})"
    else:
        changes_heading = "## 🔥 Bajadas reales de precio"
    lines += [changes_heading, ""]
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
        "- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — "
        "un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.",
        "- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.",
        "- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.",
        "- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, "
        "**rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y "
        "**LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para "
        "modelos recién publicados). No requiere mantenimiento manual. "
        "**Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada "
        "igual de fiable — se añadirán cuando se identifique una.",
        "- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio "
        "desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.",
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

def _is_yesterday(previous_day, today):
    if not previous_day:
        return False
    try:
        d_prev = datetime.fromisoformat(previous_day).date()
        d_today = datetime.fromisoformat(today).date()
    except ValueError:
        return False
    return (d_today - d_prev).days == 1

if __name__ == "__main__":
    main()
