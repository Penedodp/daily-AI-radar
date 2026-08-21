def estimated_cost(row, input_tokens, output_tokens):
    return (
        (input_tokens / 1_000_000) * row["input_usd_per_million"]
        + (output_tokens / 1_000_000) * row["output_usd_per_million"]
    )

def weighted_daily_cost(row, profiles):
    total = 0.0
    for p in profiles.values():
        total += p["weight"] * estimated_cost(
            row, p["input_tokens"], p["output_tokens"]
        )
    return total

def price_change(current, previous):
    if previous is None or previous <= 0:
        return None
    return ((current - previous) / previous) * 100.0
