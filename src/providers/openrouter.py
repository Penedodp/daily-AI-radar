import requests

MODELS_URL = "https://openrouter.ai/api/v1/models"

def _to_float(value):
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def fetch_models():
    r = requests.get(MODELS_URL, timeout=30)
    r.raise_for_status()
    payload = r.json()
    rows = []

    for m in payload.get("data", []):
        pricing = m.get("pricing") or {}
        prompt = _to_float(pricing.get("prompt"))
        completion = _to_float(pricing.get("completion"))

        # Para nuestro radar LLM necesitamos precio por token de entrada y salida.
        if prompt is None or completion is None or prompt < 0 or completion < 0:
            continue

        arch = m.get("architecture") or {}
        input_modalities = (
            m.get("input_modalities")
            or arch.get("input_modalities")
            or []
        )
        output_modalities = (
            m.get("output_modalities")
            or arch.get("output_modalities")
            or []
        )

        cache_read = _to_float(
            pricing.get("input_cache_read")
            or pricing.get("cache_read")
        )
        cache_write = _to_float(
            pricing.get("input_cache_write")
            or pricing.get("cache_write")
        )

        rows.append({
            "source": "openrouter",
            "provider": "openrouter",
            "model_id": m.get("id"),
            "name": m.get("name") or m.get("id"),
            "description": (m.get("description") or "")[:800],
            "context_length": m.get("context_length"),
            "input_modalities": input_modalities,
            "output_modalities": output_modalities,
            "supported_parameters": m.get("supported_parameters") or [],
            "input_usd_per_million": prompt * 1_000_000,
            "output_usd_per_million": completion * 1_000_000,
            "cache_read_usd_per_million": (
                cache_read * 1_000_000 if cache_read is not None else None
            ),
            "cache_write_usd_per_million": (
                cache_write * 1_000_000 if cache_write is not None else None
            ),
        })
    return rows
