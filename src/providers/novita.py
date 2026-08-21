import os
import requests
from .common import to_float, base_row

URL = "https://api.novita.ai/openai/v1/models"
# Novita's numeric model-catalog fields are expressed in 0.0001 USD units per 1M tokens.
PRICE_UNIT_USD = 0.0001

def fetch_models():
    key = os.getenv("NOVITA_API_KEY", "").strip()
    if not key:
        return []
    r = requests.get(
        URL,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        timeout=40,
    )
    r.raise_for_status()
    rows = []
    for m in r.json().get("data", []):
        raw_in = to_float(m.get("input_token_price_per_m"))
        raw_out = to_float(m.get("output_token_price_per_m"))
        if raw_in is None or raw_out is None:
            continue
        inp = raw_in * PRICE_UNIT_USD
        out = raw_out * PRICE_UNIT_USD
        # Sanity check: ignore clearly malformed catalog values.
        if inp < 0 or out < 0 or inp > 1000 or out > 1000:
            continue
        rows.append(base_row(
            source="novita",
            provider="Novita AI",
            model_id=m.get("id"),
            name=m.get("title") or m.get("id"),
            context_length=m.get("context_size"),
            input_price=inp,
            output_price=out,
            description=m.get("description") or "",
            metadata={"raw_input_price": raw_in, "raw_output_price": raw_out},
        ))
    return rows
