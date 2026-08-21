import re

def is_relevant_text_model(row, config):
    haystack = f"{row.get('model_id','')} {row.get('name','')}".lower()
    for pattern in config.get("filters", {}).get("exclude_patterns", []):
        if re.search(pattern, haystack, flags=re.IGNORECASE):
            return False, f"exclude:{pattern}"

    outputs = [str(x).lower() for x in (row.get("output_modalities") or [])]
    if config.get("filters", {}).get("require_text_output", True):
        if outputs and "text" not in outputs:
            return False, "non_text_output"

    if row.get("input_usd_per_million") is None or row.get("output_usd_per_million") is None:
        return False, "missing_price"
    return True, None
