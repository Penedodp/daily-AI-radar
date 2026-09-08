import math

def estimated_cost(row, input_tokens, output_tokens):
    return (
        (input_tokens / 1_000_000) * row["input_usd_per_million"]
        + (output_tokens / 1_000_000) * row["output_usd_per_million"]
    )

def costs_by_task(row, task_profiles):
    return {
        key: estimated_cost(row, p["input_tokens"], p["output_tokens"])
        for key, p in task_profiles.items()
    }

def weighted_daily_cost(row, task_profiles):
    costs = costs_by_task(row, task_profiles)
    return sum(costs[k] * task_profiles[k].get("weight", 0) for k in task_profiles)

def price_change(current, previous):
    if previous is None or previous <= 0:
        return None
    return ((current - previous) / previous) * 100.0

def value_score(quality_score, task_cost, anchor_usd=0.05):
    if quality_score is None:
        return None
    if task_cost <= 0:
        return round(float(quality_score) * 10.0, 1)
    anchor = max(float(anchor_usd), 1e-9)
    affordability = 1.0 / math.sqrt(1.0 + (task_cost / anchor))
    return round(float(quality_score) * 10.0 * affordability, 1)

# Known routers: entities that pick a model per-request rather than being one
# themselves. A router has no fixed benchmark or checkpoint identity of its
# own, so it must never receive a model-level score (audit #3 §18).
ROUTER_MODEL_IDS = {"openrouter/free"}

def is_router_entity(row):
    return (row.get("model_id") or "").lower() in ROUTER_MODEL_IDS

def override_key(provider, model_id):
    return f"{provider or ''}::{(model_id or '').lower()}"

def compute_pricing_status(row, overrides=None):
    """A price of 0/0 is ambiguous: free tier, dedicated-only capacity,
    missing/unavailable price, or a collector error can all surface as
    zero. Precedence (PRE_BENCH_V2_FINAL_CLEANUP #7), highest first:
      1. explicit paid signal (input/output > 0) — always wins;
      2. a verified provider pricing override (config/provider_pricing_overrides.json) —
         a human checked the provider's own pricing page and dated it;
      3. a known collector-level signal (OpenRouter's own `:free` id suffix,
         the `openrouter/free` router itself);
      4. "unknown" — priced but not verifiably free, must not enter
         free-tier rankings or paid cost rankings either, since we don't
         actually know its real cost.
    `overrides`: {override_key(provider, model_id): entry}, entry has at
    least "pricing_status" ('free' or 'promotional_free').
    """
    inp = row.get("input_usd_per_million", 0) or 0
    out = row.get("output_usd_per_million", 0) or 0
    if inp > 0 or out > 0:
        return "paid"
    override = (overrides or {}).get(override_key(row.get("provider"), row.get("model_id")))
    if override and override.get("pricing_status") in {"free", "promotional_free"}:
        return override["pricing_status"]
    if is_router_entity(row):
        return "free_router"
    if (row.get("model_id") or "").lower().endswith(":free"):
        return "free"
    return "unknown"

def has_known_price(row):
    """Rows whose pricing_status lets us trust cost-based comparisons."""
    return row.get("pricing_status") in {"paid", "free", "promotional_free"}

def is_free(row):
    return row.get("pricing_status") in {"free", "promotional_free"}

def is_free_available(row):
    """Broader than is_free(): anything a user could actually call for $0
    right now, including the free router — used for the "gratis disponibles
    hoy" listing, which is explicitly NOT a quality ranking (audit #3 §14)."""
    return row.get("pricing_status") in {"free", "promotional_free", "free_router"}
