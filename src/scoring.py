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

def is_free(row):
    return (
        row.get("input_usd_per_million", 0) == 0
        and row.get("output_usd_per_million", 0) == 0
    )
