import os
import requests

URL = "https://openrouter.ai/api/v1/chat/completions"

# Known-good fallback: a real OpenRouter free-tier slug, used only if we can't
# find any free model in today's snapshot to route the summary through.
FALLBACK_FREE_MODEL = "meta-llama/llama-3.1-8b-instruct:free"

def pick_free_model(snapshot, config):
    configured = (config.get("summary_model") or "").strip()
    # "openrouter/free" and similar shortcuts are not real OpenRouter slugs
    # (free models are addressed as "<provider>/<model>:free"), so only trust
    # a configured value that actually looks like one.
    if configured and configured.endswith(":free"):
        return configured

    for rec in (snapshot.get("recommendations") or {}).values():
        for source_data in (rec.get("sources") or {}).values():
            best_free = source_data.get("best_free")
            if best_free and best_free.get("raw_model", "").endswith(":free"):
                return best_free["raw_model"]

    return FALLBACK_FREE_MODEL

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
Las puntuaciones de calidad vienen de dos benchmarks reales e independientes, Aider Polyglot y LMArena WebDev
Arena — trátalos siempre por separado (nunca digas que un modelo con score de un benchmark es "mejor" que otro
con score del otro benchmark, son escalas distintas) y menciona la fuente exacta si citas un score.
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
                "X-Title": "Daily AI Radar",
            },
            json={
                "model": pick_free_model(snapshot, config),
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.15,
            },
            timeout=90,
        )
        if not r.ok:
            print(f"[WARN] Resumen IA no disponible: HTTP {r.status_code} — {r.text[:300]}")
            return None
        body = r.json()
        choices = body.get("choices") or []
        if not choices:
            print(f"[WARN] Resumen IA no disponible: respuesta sin choices — {str(body)[:300]}")
            return None
        return choices[0]["message"]["content"]
    except Exception as exc:
        print(f"[WARN] Resumen IA no disponible: {type(exc).__name__}: {str(exc)[:200]}")
        return None
