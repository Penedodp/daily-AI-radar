import os
import requests
from .common import to_float, base_row

URL = "https://api.cheaperinference.com/v1/models"

def fetch_models():
    key = os.getenv("CHEAPER_INFERENCE_API_KEY", "").strip()
    if not key:
        return []
    r = requests.get(
        URL,
        params={"type": "text"},
        headers={"Authorization": f"Bearer {key}"},
        timeout=40,
    )
    r.raise_for_status()
    payload = r.json()
    rows = []
    for m in payload.get("data", []):
        p = m.get("pricing") or {}
        inp = to_float(p.get("input_per_million"))
        out = to_float(p.get("output_per_million"))
        if inp is None or out is None:
            continue
        rows.append(base_row(
            source="cheaperinference",
            provider="CheaperInference",
            model_id=m.get("id"),
            name=m.get("name") or m.get("id"),
            context_length=m.get("context_length"),
            input_price=inp,
            output_price=out,
            cache_read=to_float(p.get("cache_read_input_per_million")),
            cache_write=to_float(p.get("cache_write_input_per_million")),
            description=m.get("description") or "",
            metadata={
                "pricing_version": payload.get("pricing_version"),
                "pricing_checked_at": payload.get("pricing_checked_at"),
                "pricing_updated_at": payload.get("pricing_updated_at"),
                "reasoning": m.get("reasoning"),
                "streaming": m.get("streaming"),
            },
        ))
    return rows
