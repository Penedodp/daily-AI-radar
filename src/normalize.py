import re

def canonicalize(model_id, aliases):
    value = (model_id or "").strip()
    for rule in aliases.get("rules", []):
        if re.search(rule["pattern"], value, flags=re.IGNORECASE):
            return rule["canonical"]

    # Fallback: remove provider prefix and common free/latest route decorations.
    slug = value.split("/", 1)[-1].lower()
    slug = re.sub(r":free$", "", slug)
    slug = re.sub(r"^~", "", slug)
    slug = re.sub(r"[-_/ ]latest$", "", slug)
    return slug
