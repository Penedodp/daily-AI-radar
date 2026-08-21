import re

def match_quality_profile(model_id, quality_config):
    for rule in quality_config.get("rules", []):
        if re.search(rule["pattern"], model_id or "", flags=re.IGNORECASE):
            return {
                "label": rule.get("label", model_id),
                "confidence": rule.get("confidence", "desconocida"),
                "source_note": rule.get("source_note", ""),
                "scores": rule.get("scores", {}),
            }
    return None
