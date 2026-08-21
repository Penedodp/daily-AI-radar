import os
import requests
from .common import to_float, base_row

URL = "https://openrouter.ai/api/v1/models"

def fetch_models():
    headers = {}
    key = os.getenv("OPENROUTER_API_KEY", "").strip()
    if key:
        headers["Authorization"] = f"Bearer {key}"

    r = requests.get(URL, params={"output_modalities": "text"}, headers=headers, timeout=40)
    r.raise_for_status()
    rows = []
    for m in r.json().get("data", []):
        p = m.get("pricing") or {}
        inp = to_float(p.get("prompt"))
        out = to_float(p.get("completion"))
        if inp is None or out is None or inp < 0 or out < 0:
            continue
        arch = m.get("architecture") or {}
        row = base_row(
            source="openrouter",
            provider="OpenRouter",
            model_id=m.get("id"),
            name=m.get("name") or m.get("id"),
            context_length=m.get("context_length"),
            input_price=inp * 1_000_000,
            output_price=out * 1_000_000,
            cache_read=(to_float(p.get("input_cache_read") or p.get("cache_read")) or 0) * 1_000_000 or None,
            cache_write=(to_float(p.get("input_cache_write") or p.get("cache_write")) or 0) * 1_000_000 or None,
            description=m.get("description") or "",
            metadata={
                "supported_parameters": m.get("supported_parameters") or [],
                "canonical_slug": m.get("canonical_slug"),
            },
        )
        row["input_modalities"] = arch.get("input_modalities") or ["text"]
        row["output_modalities"] = arch.get("output_modalities") or ["text"]
        rows.append(row)
    return rows
