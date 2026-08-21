def to_float(value):
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def base_row(source, provider, model_id, name=None, context_length=None,
             input_price=None, output_price=None, cache_read=None,
             cache_write=None, description="", metadata=None):
    return {
        "source": source,
        "provider": provider,
        "model_id": model_id,
        "name": name or model_id,
        "description": (description or "")[:800],
        "context_length": context_length,
        "input_modalities": ["text"],
        "output_modalities": ["text"],
        "input_usd_per_million": float(input_price or 0),
        "output_usd_per_million": float(output_price or 0),
        "cache_read_usd_per_million": cache_read,
        "cache_write_usd_per_million": cache_write,
        "metadata": metadata or {},
    }
