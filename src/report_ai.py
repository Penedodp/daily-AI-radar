import os
import requests

URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_summary(snapshot, config):
    key = os.getenv("OPENROUTER_API_KEY", "").strip()
    if not key:
        return None

    compact = {
        "date": snapshot.get("generated_at"),
        "provider_status": snapshot.get("provider_status"),
        "recommendations": snapshot.get("recommendations"),
        "cross_provider_opportunities": snapshot.get("cross_provider_opportunities", [])[:12],
        "price_changes": snapshot.get("changes", {}),
    }

    prompt = f"""
Eres un analista de costes de APIs de IA. Escribe un informe diario en español, máximo 450 palabras.

Distingue SIEMPRE:
1) mejor opción GRATIS,
2) mejor relación calidad/precio DE PAGO,
3) opción PREMIUM si la mejora de calidad puede justificar el coste,
4) oportunidades de usar el MISMO MODELO por un proveedor/ruta más barata.

No llames "descuento" a una diferencia entre proveedores. Reserva "bajada/descuento" para un cambio de precio
del mismo proveedor/ruta frente al histórico.
No inventes benchmarks, latencia, disponibilidad ni promociones.
Los quality_score son heurísticas internas, no benchmarks oficiales.
Si algunos proveedores opcionales no están configurados, dilo brevemente.
Da al final una estrategia concreta para hoy: tareas normales, coding y problemas difíciles.

DATOS:
{compact}
"""
    try:
        r = requests.post(
            URL,
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "X-Title": "AI Price Radar",
            },
            json={
                "model": config.get("summary_model", "openrouter/free"),
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.15,
            },
            timeout=90,
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception as exc:
        print(f"[WARN] Resumen IA no disponible: {type(exc).__name__}")
        return None
