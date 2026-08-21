import requests

MODELS_URL = "https://openrouter.ai/api/v1/models"

def fetch_models():
    r = requests.get(MODELS_URL, timeout=30)
    r.raise_for_status()
    payload = r.json()
    rows = []

    for m in payload.get("data", []):
        pricing = m.get("pricing") or {}
        # OpenRouter API prices are commonly returned in dollars per token.
        try:
            prompt = float(pricing.get("prompt") or 0)
            completion = float(pricing.get("completion") or 0)
        except (TypeError, ValueError):
            continue

        rows.append({
            "source": "openrouter",
            "provider": "openrouter",
            "model_id": m.get("id"),
            "name": m.get("name") or m.get("id"),
            "context_length": m.get("context_length"),
            "input_usd_per_million": prompt * 1_000_000,
            "output_usd_per_million": completion * 1_000_000,
            "raw": {
                "architecture": m.get("architecture"),
                "top_provider": m.get("top_provider")
            }
        })
    return rows
