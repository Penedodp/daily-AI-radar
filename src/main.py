from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import defaultdict
import hashlib
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
    is_free, compute_pricing_status, has_known_price, is_router_entity, is_free_available,
    override_key,
)
from report_ai import generate_summary
from report_html import (
    build_html, build_explorer_page, build_methodology_page, build_benchmarks_placeholder_page,
)

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
_KNOWN_EXPLORER_STATUSES = {"paid", "free", "promotional_free", "free_router"}

# Bumped only when the formula/normalization itself changes — never
# reinterprets past snapshots, which keep whatever version they were built
# with (audit #3 §23-25).
SCORING_VERSION = "radar_value_v1"
BENCHMARK_NORMALIZATION_VERSION = {
    "aider_polyglot": "aider_pass_rate_linear_v1",
    "lmarena_webdev": "webdev_elo_950_1750_v1",
}

def task_profiles_fingerprint(task_profiles):
    """FINAL_PRE_BENCH_V2_UX_ARCHITECTURE #16: a short, stable fingerprint of
    `task_profiles` so two historical points can be checked for compatibility
    before being connected on a chart — an edit to config.json's token
    profiles changes this, even though nothing about pricing moved."""
    return hashlib.sha1(
        json.dumps(task_profiles, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]

def load_json(path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))

def previous_snapshot(data_dir, today):
    candidates = [p for p in sorted(data_dir.glob("*.json"), reverse=True) if p.stem != today]
    if not candidates:
        return None, None
    return load_json(candidates[0], {}), candidates[0].stem

def best_market_history(data_dir, today, canonical_model, limit=14):
    """PRE_BENCH_V2_FINAL_CLEANUP #31/#34: this is explicitly BEST MARKET
    HISTORY — the cheapest route's cost for `canonical_model` on each of the
    last `limit` days (oldest first) — NOT one route's own price history
    (that's `endpoint_price_trend` below). The winning route can be a
    different provider/quantization from one day to the next, so each point
    also records which route won and under which calculation_context, so a
    consumer can tell whether two points are even comparable (#32)."""
    files = [p for p in sorted(data_dir.glob("*.json")) if p.stem != today][-limit:]
    points = []
    for p in files:
        snap = load_json(p, None)
        if not snap:
            continue
        best_row = None
        for r in snap.get("models", []):
            if r.get("canonical_model") != canonical_model:
                continue
            cost = r.get("weighted_cost")
            if cost is not None and (best_row is None or cost < best_row.get("weighted_cost")):
                best_row = r
        if best_row is not None:
            calc_ctx = snap.get("calculation_context") or {}
            points.append({
                "date": p.stem,
                "cost": best_row["weighted_cost"],
                "route_identity": route_identity(best_row),
                "provider": best_row.get("provider"),
                "route_tag": (best_row.get("metadata") or {}).get("route_tag"),
                "quantization": (best_row.get("metadata") or {}).get("quantization"),
                "scoring_version": calc_ctx.get("scoring_version"),
                "task_profiles_version": task_profiles_fingerprint(calc_ctx.get("task_profiles", {})),
            })
    return points

def price_trend(data_dir, today, canonical_model, limit=14):
    """Back-compat shim for callers that only want (date, cost) pairs."""
    return [{"date": p["date"], "cost": p["cost"]} for p in best_market_history(data_dir, today, canonical_model, limit)]

def endpoint_price_trend(data_dir, today, target_route_identity, limit=14):
    """PRE_BENCH_V2_FINAL_CLEANUP #33: history of ONE specific route/endpoint
    (never mixing routes) — a preparatory building block for a future
    per-route history view. Uses exclusively `route_identity()`, never the
    coarser `route_key()`."""
    files = [p for p in sorted(data_dir.glob("*.json")) if p.stem != today][-limit:]
    points = []
    for p in files:
        snap = load_json(p, None)
        if not snap:
            continue
        for r in snap.get("models", []):
            if route_identity(r) == target_route_identity:
                points.append({"date": p.stem, "cost": r.get("weighted_cost"),
                               "context_length": r.get("context_length"),
                               "throughput_p50": (r.get("metadata") or {}).get("throughput_p50"),
                               "uptime_last_1d": (r.get("metadata") or {}).get("uptime_last_1d")})
                break
    return points

def route_key(row):
    """Model-scoped key: provider label + model id, no route/quantization.
    Intentionally coarser than `route_identity()` — this is what benchmark
    matching uses internally too (a benchmark measures the *model*, not one
    specific endpoint; see `benchmark_scope`), so it must stay aligned with
    `quality_bench.match_models`'s own key format."""
    return f"{row.get('provider','')}::{row.get('model_id','')}"

ROUTE_IDENTITY_VERSION = "route_identity_v1"

def route_identity(row):
    """Stable identity of one endpoint/route — used for deduplication,
    price-change detection and historical tracking, wherever two rows must
    be recognized as "the same route over time" or rejected as duplicates.

    Deliberately NOT based on the human-facing `provider` display label
    (e.g. "OpenRouter → OpenAI (flex)"), which is synthesized for readability
    and could theoretically collide or drift — see audit #3 §5. For
    `openrouter-route` rows it uses the raw `provider_name` + `route_tag`
    from the API instead; for plain price-list collectors, `provider` IS
    already the stable identity (e.g. "Together AI"), so it's used directly.
    """
    meta = row.get("metadata") or {}
    source = row.get("source", "")
    if source == "openrouter-route":
        parts = [
            source, row.get("model_id", ""),
            meta.get("provider_name") or "", meta.get("route_tag") or "",
            meta.get("quantization") or "",
        ]
    else:
        parts = [source, row.get("provider", ""), row.get("model_id", "")]
    return ROUTE_IDENTITY_VERSION + "::" + "|".join(str(p) for p in parts)

def _combined_tariff_change_pct(row):
    """A single representative %-change for sorting/display in the
    drops/increases lists, built ONLY from real tariff deltas (never
    weighted_cost) — whichever of input/output moved the most, by
    magnitude, since that's the more significant real change."""
    candidates = [c for c in (row.get("input_change_pct"), row.get("output_change_pct")) if c is not None]
    if not candidates:
        return None
    return max(candidates, key=abs)

def build_model_benchmark_registry(models):
    """Model Benchmark Registry (PRE_BENCH_V2_FINAL_CLEANUP #11-15): a
    benchmark measures the canonical MODEL, not any one route's raw slug —
    two routes of the exact same model must never disagree on whether/how
    they're benchmarked just because one provider's slug string happened to
    fuzzy-match and a differently-formatted one from another provider
    didn't. Consumes and removes each row's `_route_quality_by_source`
    (its own raw per-route match, keyed by source) and returns ONE registry
    entry per canonical model — keeping, per source, whichever route matched
    with the highest confidence — so every route of that model can share the
    exact same benchmark reference instead of each owning its own
    (possibly-inconsistent) copy."""
    model_benchmarks = defaultdict(dict)
    for row in models:
        route_bench = row.pop("_route_quality_by_source", {})
        if row.get("entity_type") == "router":
            continue
        for source, q in route_bench.items():
            existing = model_benchmarks[row["canonical_model"]].get(source)
            if existing is None or (q.get("match_ratio") or 0) > (existing.get("match_ratio") or 0):
                model_benchmarks[row["canonical_model"]][source] = q
    return model_benchmarks

def commercial_provider(row):
    """FINAL_PRE_BENCH_V2_UX_ARCHITECTURE #14/#24/#28: the entity that owns
    the free-tier/commercial POLICY (e.g. "OpenRouter") is not always the
    literal `provider` display label — for an `openrouter-route` row that
    label also encodes the underlying infra endpoint_provider (e.g.
    "OpenRouter → Nvidia"), which has no free-tier policy of its own.
    Free-tier limits are a property of the commercial_provider only."""
    if row.get("source") in {"openrouter", "openrouter-route"}:
        return "OpenRouter"
    return row.get("provider")

def endpoint_provider(row):
    """The underlying infra/provider actually serving an OpenRouter route
    (e.g. "Nvidia", "GMICloud") — distinct from `commercial_provider`
    (always "OpenRouter" for these rows). None for non-route sources, where
    `provider` already IS the one and only relevant identity."""
    if row.get("source") == "openrouter-route":
        return (row.get("metadata") or {}).get("provider_name")
    return None

def free_limits_for(row, free_tiers):
    """Data-driven free-tier conditions (config/free_tiers.json) — never
    hardcoded in the renderer, so limits can be corrected without a code
    change when a provider updates them (audit #3 §16). Looked up by
    `commercial_provider`, not the raw `provider` display label, so a
    subroute like "OpenRouter → Nvidia" still inherits OpenRouter's own
    free-tier policy instead of missing it entirely (#14)."""
    if row.get("entity_type") == "router":
        return free_tiers.get("OpenRouter Free Router")
    if row.get("pricing_status") in {"free", "promotional_free"}:
        return free_tiers.get(commercial_provider(row))
    return None

def apply_price_change(row, old):
    """Sets change-detection fields on `row` from `old` (the same route's row
    in the previous snapshot, or None). Real tariff change (input/output
    $/M) is computed separately from the estimated task-cost change — a
    task_profiles edit in config.json must never be reported as a tariff
    move (audit #3 §3)."""
    row["input_change_pct"] = price_change(
        row["input_usd_per_million"], old.get("input_usd_per_million") if old else None,
    )
    row["output_change_pct"] = price_change(
        row["output_usd_per_million"], old.get("output_usd_per_million") if old else None,
    )
    row["change_pct"] = _combined_tariff_change_pct(row)
    row["estimated_cost_change_pct"] = price_change(
        row["weighted_cost"], old.get("weighted_cost") if old else None,
    )

def previous_map(snapshot):
    out = {}
    for r in (snapshot or {}).get("models", []):
        out[route_identity(r)] = r
    return out

def dedup_exact_routes(raw_rows):
    """Exact-duplicate rows (same route_identity) must never reach the
    snapshot — two identical rows would silently double a model's presence
    in every table. Keeps the first occurrence."""
    seen = set()
    deduped = []
    duplicates = 0
    for r in raw_rows:
        key = route_identity(r)
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
        "commercial_provider": row.get("commercial_provider"),
        "endpoint_provider": row.get("endpoint_provider"),
        "route_tag": (row.get("metadata") or {}).get("route_tag"),
        "quantization": (row.get("metadata") or {}).get("quantization"),
        "route_identity": route_identity(row),
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
            result["benchmark_scope"] = q.get("benchmark_scope", "model")
            result["value_score"] = (row.get("value_scores") or {}).get(source, {}).get(category)
    if row.get("change_pct") is not None:
        result["change_pct"] = round(row["change_pct"], 1)
    if row.get("input_change_pct") is not None:
        result["input_change_pct"] = round(row["input_change_pct"], 1)
    if row.get("output_change_pct") is not None:
        result["output_change_pct"] = round(row["output_change_pct"], 1)
    if row.get("estimated_cost_change_pct") is not None:
        result["estimated_cost_change_pct"] = round(row["estimated_cost_change_pct"], 1)
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
    route the model has is kept in `routes` for the expandable detail view.
    Routers (e.g. openrouter/free) are excluded — they have no single
    checkpoint identity to compare (audit #3 §18); see `build_free_today`."""
    groups = defaultdict(list)
    for r in models:
        if r.get("entity_type") == "router":
            continue
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
                "benchmark_scope": q.get("benchmark_scope", "model"),
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
                    "commercial_provider": r.get("commercial_provider"),
                    "endpoint_provider": r.get("endpoint_provider"),
                    "route_tag": (r.get("metadata") or {}).get("route_tag"),
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

    # Default order is a NEUTRAL criterion — never max(Aider, WebDev), which
    # would silently compare two incompatible scales again (audit #3 §12).
    # Known-priced models first (cheapest first), then unknown-priced ones,
    # so nothing meaningful is hidden below the fold; sorting by quality is
    # left to the user via the (per-source) column headers.
    out.sort(key=lambda m: (m["pricing_status"] in _KNOWN_EXPLORER_STATUSES, -m["weighted_cost"]), reverse=True)
    return out

def _select_openrouter_route_candidates(openrouter_only, bench_candidates, previous):
    """Union of: models with a benchmark match, free (`:free`) models, and
    models that moved price meaningfully yesterday — not just whichever
    models happen to be scored, which would bias `openrouter_routes`
    coverage toward benchmarked models only (audit #3 §20)."""
    mover_ids = set()
    for entry in (previous or {}).get("changes", {}).get("drops", []):
        if entry.get("raw_model"):
            mover_ids.add(entry["raw_model"])
    for entry in (previous or {}).get("changes", {}).get("increases", []):
        if entry.get("raw_model"):
            mover_ids.add(entry["raw_model"])

    candidates = []
    seen = set()
    for r in openrouter_only:
        model_id = r["model_id"]
        if model_id in seen:
            continue
        is_scored = route_key(r) in bench_candidates
        is_free_model = model_id.lower().endswith(":free")
        is_mover = model_id in mover_ids
        if is_scored or is_free_model or is_mover:
            candidates.append(model_id)
            seen.add(model_id)
    return candidates

def _benchmark_coverage_stats(models):
    """Separates "a model has a benchmark" from "an endpoint was itself
    benchmarked" — today the second number is always 0 (no endpoint-scoped
    source exists yet), and that's the correct, honest answer, not a bug
    (audit #3 §22)."""
    benchmarked_models = {r["canonical_model"] for r in models if r.get("quality_by_source")}
    endpoints_of_benchmarked_models = sum(1 for r in models if r["canonical_model"] in benchmarked_models)
    endpoint_specific = sum(
        1 for r in models
        for q in (r.get("quality_by_source") or {}).values()
        if q.get("benchmark_scope") == "endpoint"
    )
    return {
        "models_with_benchmark": len(benchmarked_models),
        "endpoints_of_benchmarked_models": endpoints_of_benchmarked_models,
        "endpoint_specific_benchmarks": endpoint_specific,
    }

def _pricing_override_match_stats(models, overrides):
    """FINAL_PRE_BENCH_V2_UX_ARCHITECTURE #2/#5: an override that's configured
    but never matches any live row is a silent bug (usually a stale/wrong
    model_id) — surface it as configured/used/unused instead of only
    trusting that a match happened."""
    used_keys = {
        override_key(r.get("provider"), r.get("model_id"))
        for r in models if r.get("pricing_override")
    }
    configured = len(overrides)
    used = len(used_keys & set(overrides.keys()))
    return {
        "pricing_overrides_configured": configured,
        "pricing_overrides_used": used,
        "pricing_overrides_unused": configured - used,
    }

def _pricing_override_stats(models, today, staleness_days):
    """PRE_BENCH_V2_FINAL_CLEANUP #41/#42: an override doesn't get silently
    invalidated once it's old, but it does get flagged in Data Health so a
    stale claim ('this is free, verified 2026-01-01') isn't presented with
    the same confidence as a freshly-checked one."""
    active, stale = 0, 0
    try:
        today_date = datetime.fromisoformat(today).date()
    except ValueError:
        today_date = None
    for r in models:
        override = r.get("pricing_override")
        if not override:
            continue
        active += 1
        verified_at = override.get("verified_at")
        is_stale = True
        if verified_at and today_date:
            try:
                age = (today_date - datetime.fromisoformat(verified_at).date()).days
                is_stale = age > staleness_days
            except ValueError:
                is_stale = True
        if is_stale:
            stale += 1
    return {"pricing_overrides_active": active, "pricing_overrides_stale": stale}

def _free_route_bench(r):
    """Per-source scores for one free route, kept separate — never collapsed
    to a single max() across heterogeneous benchmark scales
    (PRE_BENCH_V2_FINAL_CLEANUP #9/#10)."""
    return {
        source: {
            "score": q["scores"].get("coding"),
            "source_label": q.get("source_label"),
            "raw_score": q.get("raw_score"),
            "raw_unit": q.get("raw_unit"),
            "benchmark_scope": q.get("benchmark_scope", "model"),
        }
        for source, q in (r.get("quality_by_source") or {}).items()
        if q.get("scores", {}).get("coding") is not None
    }

def build_free_today(models):
    """Every free-available route today (including the free router),
    regardless of benchmark — answers "what can I use for $0 right now",
    a different question from "what's the best free model" (audit #3 §14).

    Grouped ONE ROW PER CANONICAL MODEL, with its individual free routes
    listed underneath for expansion (PRE_BENCH_V2_FINAL_CLEANUP #10/#21) —
    a model with several free routes (e.g. across providers or
    quantizations) must appear once, not once per route. Quality is never
    reduced to a single max() across benchmark sources (#9): each source's
    score is kept independently, or "Sin benchmark compatible" if none
    matched. Sorted by a neutral criterion (context, then name) — NOT by
    quality."""
    groups = defaultdict(list)
    router_row = None
    for r in models:
        if r.get("entity_type") == "router":
            router_row = router_row or r
            continue
        if not is_free(r):
            continue
        groups[r["canonical_model"]].append(r)

    out = []
    for canonical, rows in groups.items():
        rows_sorted = sorted(rows, key=lambda r: -(r.get("context_length") or 0))
        best = rows_sorted[0]
        out.append({
            "model": canonical,
            "entity_type": "model",
            "provider": best["provider"],
            "pricing_status": best["pricing_status"],
            "context_length": best.get("context_length"),
            "quality_by_source": _free_route_bench(best),
            "free_limits": best.get("free_limits"),
            "routes_count": len(rows_sorted),
            "routes": [
                {
                    "raw_model": r["model_id"],
                    "provider": r["provider"],
                    "pricing_status": r["pricing_status"],
                    "context_length": r.get("context_length"),
                    "quantization": (r.get("metadata") or {}).get("quantization"),
                    "free_limits": r.get("free_limits"),
                    "pricing_override": r.get("pricing_override"),
                }
                for r in rows_sorted
            ],
        })

    out.sort(key=lambda m: (-(m["context_length"] or 0), m["model"]))

    if router_row is not None:
        out.append({
            "model": router_row["canonical_model"],
            "entity_type": "router",
            "provider": router_row["provider"],
            "pricing_status": router_row["pricing_status"],
            "context_length": router_row.get("context_length"),
            "quality_by_source": {},
            "free_limits": router_row.get("free_limits"),
            "routes_count": 1,
            "routes": [],
        })
    return out

def validate_snapshot(models, pricing_overrides=None):
    """Two-tier invariant checks (Fase 6 §6): ERRORs mean a bug slipped past
    the conservative rules elsewhere and must block publishing (the daily
    workflow exits non-zero and the commit/push step never runs). WARNINGs
    are expected, routine conditions (an unscored model, an unknown price)
    that are worth surfacing but must never stop the run — see the plan's
    'mostrar el dato en vez de ocultarlo' principle."""
    errors, warnings = [], []

    if pricing_overrides:
        override_stats = _pricing_override_match_stats(models, pricing_overrides)
        if override_stats["pricing_overrides_configured"] > 0 and override_stats["pricing_overrides_used"] == 0:
            warnings.append(
                f"{override_stats['pricing_overrides_configured']} pricing override(s) configurado(s) pero "
                "NINGUNO hizo match con una ruta real — probablemente un model_id desactualizado o mal escrito"
            )
        elif override_stats["pricing_overrides_unused"] > 0:
            warnings.append(
                f"{override_stats['pricing_overrides_unused']} de {override_stats['pricing_overrides_configured']} "
                "pricing override(s) configurado(s) no hicieron match con ninguna ruta"
            )

    seen_routes = set()
    for r in models:
        key = route_identity(r)
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

    for r in models:
        override = r.get("pricing_override")
        if not override:
            continue
        if not override.get("verified_at"):
            warnings.append(
                f"pricing override sin fecha de verificación: {r['provider']} / {r['model_id']}"
            )
        if override.get("pricing_status") == "promotional_free" and not override.get("source_url"):
            warnings.append(
                f"promotional_free override sin source_url: {r['provider']} / {r['model_id']}"
            )

    for r in models:
        for source, q in (r.get("quality_by_source") or {}).items():
            if q.get("benchmark_scope") == "model" and not r.get("canonical_model"):
                errors.append(f"benchmark scope=model sin canonical_model válido: {r.get('model_id')} ({source})")
            if q.get("benchmark_scope") == "endpoint" and not route_identity(r):
                errors.append(f"benchmark scope=endpoint sin route_identity: {r.get('model_id')} ({source})")

    return errors, warnings

def main():
    config = load_json(ROOT / "config.json", {})
    aliases = load_json(ROOT / "model_aliases.json", {"rules": []})
    free_tiers = {
        e["provider"]: e
        for e in load_json(ROOT / "config" / "free_tiers.json", {"entries": []}).get("entries", [])
    }
    pricing_overrides_cfg = load_json(ROOT / "config" / "provider_pricing_overrides.json", {"entries": []})
    pricing_overrides = {
        override_key(e["provider"], e["model_id"]): e
        for e in pricing_overrides_cfg.get("entries", [])
    }
    override_staleness_days = pricing_overrides_cfg.get("_meta", {}).get("staleness_days", 30)

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

    # OpenRouter underlying routes: track a union of useful model IDs, not all
    # 400+ and not ONLY the already-benchmarked ones (which would bias route
    # coverage — audit #3 §20).
    openrouter_only = [r for r in raw_rows if r["source"] == "openrouter"]
    bench_candidates = bench_match_by_source(openrouter_only)
    openrouter_candidates = _select_openrouter_route_candidates(openrouter_only, bench_candidates, previous)
    route_limit = config.get("route_tracking_max_models", 35)
    models_monitored = min(len(openrouter_candidates), route_limit)

    route_cfg = config.get("providers", {}).get("openrouter_routes", {})
    if route_cfg.get("enabled", True):
        try:
            route_rows, route_status = fetch_routes(
                openrouter_candidates,
                route_limit,
            )
            raw_rows.extend(route_rows)
            provider_status["openrouter_routes"] = {
                "status": route_status,
                "count": len(route_rows),
                "models_monitored": models_monitored,
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
        row["pricing_status"] = compute_pricing_status(row, pricing_overrides)
        row["pricing_override"] = pricing_overrides.get(override_key(row.get("provider"), row.get("model_id")))
        row["entity_type"] = "router" if is_router_entity(row) else "model"
        row["free_limits"] = free_limits_for(row, free_tiers)
        row["commercial_provider"] = commercial_provider(row)
        row["endpoint_provider"] = endpoint_provider(row)

        # A router has no single checkpoint identity — it must never carry a
        # model-level benchmark score, however a name-based match might fire
        # (audit #3 §18). Matched here per RAW route (route_key = provider +
        # raw model_id) — this is only the input to the Model Benchmark
        # Registry step below, not the final per-row score yet.
        matches = {} if row["entity_type"] == "router" else (bench_matches.get(route_key(row)) or {})
        row["_route_quality_by_source"] = {}
        for source, bq in matches.items():
            row["_route_quality_by_source"][source] = {
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
                # Every benchmark today measures the checkpoint/model, matched via
                # route_key() (provider+model_id, no route_tag/quantization) —
                # never a specific endpoint. Kept explicit so a route showing a
                # cheap FP4 price next to this score never implies FP4 itself was
                # benchmarked (audit #3 §7/§8). Endpoint-scoped benchmarks are a
                # future addition (Benchmark Engine v2) that can set this to
                # "endpoint" without changing anything else in this data model.
                "benchmark_scope": "model",
            }

        models.append(row)

    model_benchmarks = build_model_benchmark_registry(models)
    for row in models:
        row["quality_by_source"] = (
            {} if row["entity_type"] == "router"
            else dict(model_benchmarks.get(row["canonical_model"], {}))
        )
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
        apply_price_change(row, prev_map.get(route_identity(row)))

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
            points = best_market_history(data_dir, day, pick["model"])
            # FINAL_PRE_BENCH_V2_UX_ARCHITECTURE #15: TODAY's point must carry
            # the same identity/versioning fields as every historical point —
            # otherwise the most recent point on the chart is the one entry
            # that can't be checked for route/profile compatibility.
            points.append({
                "date": day, "cost": pick["weighted_cost"],
                "route_identity": pick["route_identity"],
                "provider": pick["provider"],
                "route_tag": pick.get("route_tag"),
                "quantization": pick.get("quantization"),
                "scoring_version": SCORING_VERSION,
                "task_profiles_version": task_profiles_fingerprint(task_profiles),
            })
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
    free_today = build_free_today(models)

    errors, validation_warnings = validate_snapshot(models, pricing_overrides)
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
            # FINAL_PRE_BENCH_V2_UX_ARCHITECTURE #6/#7/#43: entity_type == "router"
            # (e.g. openrouter/free) is a dynamic service, not a checkpoint — it
            # must never inflate a "model" count.
            "unique_models": len({
                r["canonical_model"] for r in models if r.get("entity_type") != "router"
            }),
            "router_entities_excluded": len({
                r["canonical_model"] for r in models if r.get("entity_type") == "router"
            }),
            "providers_with_data": sum(
                1 for k, s in provider_status.items() if k in PRICE_SOURCES and s.get("count", 0) > 0
            ),
            "benchmarks_active": sum(
                1 for k, s in provider_status.items() if k in BENCH_SOURCES and s.get("count", 0) > 0
            ),
            "openrouter_routes_analyzed": provider_status.get("openrouter_routes", {}).get("count", 0),
            "openrouter_models_monitored": provider_status.get("openrouter_routes", {}).get("models_monitored", 0),
            # "routes_with_model_benchmark" is the accurate name (#42): a route
            # inheriting its canonical model's registry entry, not a route with
            # its OWN benchmark (that's endpoint_specific_benchmarks, below).
            "routes_with_model_benchmark": sum(
                1 for r in models if r.get("entity_type") != "router" and r.get("quality_by_source")
            ),
            "unknown_price_routes": sum(1 for r in models if r.get("pricing_status") == "unknown"),
            **_benchmark_coverage_stats(models),
            **_pricing_override_stats(models, day, override_staleness_days),
            **_pricing_override_match_stats(models, pricing_overrides),
            "free_models": len({
                r["canonical_model"] for r in models
                if r.get("entity_type") != "router" and is_free(r)
            }),
            "free_routes": sum(1 for r in models if r.get("entity_type") != "router" and is_free(r)),
            "promotional_free_models": len({
                r["canonical_model"] for r in models
                if r.get("entity_type") != "router" and r.get("pricing_status") == "promotional_free"
            }),
        },
        "calculation_context": {
            "task_profiles": task_profiles,
            "task_profiles_version": task_profiles_fingerprint(task_profiles),
            "value_cost_anchor_usd": anchor,
            "scoring_version": SCORING_VERSION,
            "benchmark_normalization_version": BENCHMARK_NORMALIZATION_VERSION,
            "route_identity_version": ROUTE_IDENTITY_VERSION,
        },
        "recommendations": recs,
        "cross_provider_opportunities": opportunities,
        "changes": {"drops": drops, "increases": increases},
        "models": models,
        "explorer": explorer,
        "free_today": free_today,
        "validation_warnings": validation_warnings,
        # FINAL_PRE_BENCH_V2_UX_ARCHITECTURE #8/#9: persisted top-level so the
        # Model Benchmark Registry is a real, inspectable source of truth
        # instead of only living inside each row's (duplicated) copy.
        "model_registry": {
            canonical: {
                "display_name": canonical,
                "benchmarks": bench,
            }
            for canonical, bench in model_benchmarks.items()
        },
        # Placeholder for endpoint-scoped benchmarks (AutoExacto, Endpoint
        # Accuracy, ...) — always {} today, which is the correct, honest
        # answer, not a gap (Benchmark Engine v2 territory).
        "endpoint_benchmarks": {},
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
        f"**{stats['openrouter_routes_analyzed']} endpoints de "
        f"{stats['openrouter_models_monitored']} modelos OpenRouter monitorizados** · "
        f"**{stats['models_with_benchmark']} modelos con benchmark**.",
        "",
        "_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: "
        "30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._",
        "",
        f"_Cobertura de benchmark: {stats['models_with_benchmark']} modelos con benchmark propio, "
        f"{stats['endpoints_of_benchmarked_models']} endpoints heredan ese score de su modelo, "
        f"{stats['endpoint_specific_benchmarks']} endpoints benchmarkeados de forma específica "
        "(0 es lo esperado hoy — ver Metodología)._",
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

    # FINAL_PRE_BENCH_V2_UX_ARCHITECTURE #17-#20: RADAR (decisión rápida),
    # EXPLORER (profundidad/catálogo) and METHODOLOGY (confianza) are now
    # separate static pages instead of one giant index.html.
    dashboard = build_html(
        snapshot, day, has_previous=bool(previous), ai_summary=ai,
        price_trends=price_trends, config=config,
    )
    (docs_dir / "index.html").write_text(dashboard, encoding="utf-8")
    (docs_dir / "explorer.html").write_text(build_explorer_page(snapshot, day, config=config), encoding="utf-8")
    (docs_dir / "methodology.html").write_text(build_methodology_page(snapshot, day, config=config), encoding="utf-8")
    (docs_dir / "benchmarks.html").write_text(
        build_benchmarks_placeholder_page(day, generated_at=now.isoformat()), encoding="utf-8"
    )

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
