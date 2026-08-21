import os
import requests

URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_summary(snapshot, config):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return None

    rows = sorted(snapshot["models"], key=lambda x: x["weighted_cost"])[:config["max_models_in_ai_summary"]]
    compact = [{
        "model": r["model_id"],
        "input": round(r["input_usd_per_million"], 4),
        "output": round(r["output_usd_per_million"], 4),
        "weighted_cost": round(r["weighted_cost"], 6),
        "change_pct": r.get("change_pct")
    } for r in rows]

    prompt = f"""
Eres un analista de precios de APIs de IA. Redacta un informe diario breve en español.
Objetivo: recomendar modelos baratos y razonables para programación, razonamiento y tareas generales.
NO inventes benchmarks ni calidad que no esté en los datos. Si no hay evidencia de calidad, dilo.
Resalta bajadas de precio y modelos gratis. Explica coste estimado por tarea usando weighted_cost.
Datos:
{compact}
"""
    r = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "X-Title": "AI Price Radar"
        },
        json={
            "model": "openrouter/free",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        },
        timeout=90
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]
