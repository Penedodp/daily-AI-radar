import re

def match_quality_profile(canonical_model, raw_model_id, quality_config):
    haystack = f"{canonical_model} {raw_model_id}"
    for rule in quality_config.get("rules", []):
        if re.search(rule["pattern"], haystack, flags=re.IGNORECASE):
            return {
                "label": rule.get("label", canonical_model),
                "confidence": rule.get("confidence", "desconocida"),
                "scores": rule.get("scores", {}),
            }
    return None
