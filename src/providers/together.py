import os
import requests
from .common import to_float, base_row

URL = "https://api.together.xyz/v1/models"

def fetch_models():
    key = os.getenv("TOGETHER_API_KEY", "").strip()
    if not key:
        return []
    r = requests.get(URL, headers={"Authorization": f"Bearer {key}"}, timeout=40)
    r.raise_for_status()
    payload = r.json()
    data = payload if isinstance(payload, list) else payload.get("data", [])
    rows = []
    for m in data:
        if str(m.get("type", "")).lower() not in {"chat", "language", "code"}:
            continue
        p = m.get("pricing") or {}
        inp = to_float(p.get("input"))
        out = to_float(p.get("output"))
        if inp is None or out is None:
            continue
        rows.append(base_row(
            source="together",
            provider="Together AI",
            model_id=m.get("id"),
            name=m.get("display_name") or m.get("id"),
            context_length=m.get("context_length"),
            input_price=inp,
            output_price=out,
            cache_read=to_float(p.get("cached_input")),
            description="",
            metadata={"organization": m.get("organization"), "type": m.get("type")},
        ))
    return rows
