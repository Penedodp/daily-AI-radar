import re

def is_relevant_text_model(row, config):
    filters = config.get("filters", {})
    haystack = f"{row.get('model_id', '')} {row.get('name', '')}".lower()

    for pattern in filters.get("exclude_patterns", []):
        if re.search(pattern, haystack, flags=re.IGNORECASE):
            return False, f"exclude_pattern:{pattern}"

    if filters.get("require_text_output", True):
        outputs = [str(x).lower() for x in (row.get("output_modalities") or [])]
        # Si OpenRouter expone modalidades y text no está, no es un LLM de texto.
        if outputs and "text" not in outputs:
            return False, f"non_text_output:{','.join(outputs)}"

    return True, None
