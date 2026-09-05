import os
import time
import requests
from urllib.parse import quote
from .common import to_float, base_row

BASE = "https://openrouter.ai/api/v1/models"

def route_label(provider_name, tag):
    """Two endpoints can share the same provider_name (e.g. "OpenAI") while
    being different routes (standard/flex/zdr/priority) distinguished only by
    `tag` — keep that visible instead of collapsing them into one label."""
    provider_name = provider_name or tag or "Unknown"
    label = f"OpenRouter → {provider_name}"
    if tag and str(tag).strip().lower() != str(provider_name).strip().lower():
        label += f" ({tag})"
    return label

def fetch_routes(model_ids, max_models=35):
    # The endpoint may require a management-capable key depending on account/key type.
    key = (
        os.getenv("OPENROUTER_MANAGEMENT_API_KEY", "").strip()
        or os.getenv("OPENROUTER_API_KEY", "").strip()
    )
    if not key:
        return [], "no_key"

    rows = []
    headers = {"Authorization": f"Bearer {key}"}
    for idx, model_id in enumerate(model_ids[:max_models]):
        if "/" not in model_id:
            continue
        author, slug = model_id.split("/", 1)
        url = f"{BASE}/{quote(author, safe='')}/{quote(slug, safe=':')}/endpoints"
        r = requests.get(url, headers=headers, timeout=25)

        if r.status_code == 403:
            # Avoid hammering the endpoint if this key type cannot read it.
            return rows, "forbidden_management_key_may_be_required"
        if r.status_code in {404, 429}:
            continue
        r.raise_for_status()

        data = r.json().get("data", {})
        for ep in data.get("endpoints", []):
            p = ep.get("pricing") or {}
            inp = to_float(p.get("prompt"))
            out = to_float(p.get("completion"))
            if inp is None or out is None:
                continue
            rows.append(base_row(
                source="openrouter-route",
                provider=route_label(ep.get("provider_name"), ep.get("tag")),
                model_id=model_id,
                name=ep.get("model_name") or model_id,
                context_length=ep.get("context_length"),
                input_price=inp * 1_000_000,
                output_price=out * 1_000_000,
                metadata={
                    "route_tag": ep.get("tag"),
                    "uptime_last_1d": ep.get("uptime_last_1d"),
                    "uptime_last_30m": ep.get("uptime_last_30m"),
                    "latency_p50": (ep.get("latency_last_30m") or {}).get("p50"),
                    "throughput_p50": (ep.get("throughput_last_30m") or {}).get("p50"),
                    "quantization": ep.get("quantization"),
                },
            ))
        time.sleep(0.03)
    return rows, "ok"
