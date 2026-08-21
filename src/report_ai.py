import os
import requests

URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_summary(snapshot, config):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return None

    recs = snapshot.get("recommendations", {})
    changes = snapshot.get("changes", {})
    payload = {
        "date": snapshot.get("generated_at"),
        "recommendations": recs,
        "price_drops": changes.get("drops", [])[:10],
        "price_increases": changes.get("increases", [])[:5],
        "new_free": changes.get("new_free", [])[:10],
    }

    prompt = f"""
Eres el analista de un radar diario de precios de APIs de IA.
Redacta en español un informe corto, accionable y prudente.

OBJETIVO:
- decir qué modelo conviene usar HOY para coding, agentic coding, reasoning y general;
- destacar gratis y bajadas de precio;
- priorizar ahorro sin sacrificar demasiada calidad.

REGLAS:
- Los quality_score recibidos son una HEURÍSTICA CURADA interna, no benchmarks oficiales.
- No inventes benchmarks, latencias, descuentos ni capacidades.
- Si no hay histórico suficiente, dilo.
- Los modelos gratis pueden tener límites/rate limits; menciónalo una sola vez.
- Da una recomendación concreta: principal, gratis, y premium si merece la pena.
- Máximo unas 350 palabras.

DATOS:
{payload}
"""

    try:
        r = requests.post(
            URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "X-Title": "AI Price Radar",
            },
            json={
                "model": config.get("summary_model", "openrouter/free"),
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2,
            },
            timeout=90,
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception as exc:
        # El radar de precios debe seguir funcionando aunque falle el resumen IA.
        print(f"[WARN] No se pudo generar el resumen IA: {type(exc).__name__}")
        return None
