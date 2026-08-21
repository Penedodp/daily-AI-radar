from . import openrouter, cheaperinference, together, novita

COLLECTORS = {
    "openrouter": openrouter.fetch_models,
    "cheaperinference": cheaperinference.fetch_models,
    "together": together.fetch_models,
    "novita": novita.fetch_models,
}

def collect_all(config):
    rows = []
    statuses = {}
    for name, fn in COLLECTORS.items():
        pcfg = config.get("providers", {}).get(name, {})
        if not pcfg.get("enabled", True):
            statuses[name] = {"status": "disabled", "count": 0}
            continue
        try:
            result = fn()
            rows.extend(result)
            if result:
                statuses[name] = {"status": "ok", "count": len(result)}
            elif pcfg.get("optional"):
                statuses[name] = {"status": "not_configured_or_empty", "count": 0}
            else:
                statuses[name] = {"status": "empty", "count": 0}
        except Exception as exc:
            statuses[name] = {
                "status": "error",
                "count": 0,
                "error": f"{type(exc).__name__}: {str(exc)[:180]}",
            }
    return rows, statuses
