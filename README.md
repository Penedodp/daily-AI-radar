# AI Price Radar v2

Radar diario de precios de LLMs con GitHub Actions.

## V2

- Filtra modelos de moderación, embeddings, rerank, audio e imagen.
- Calcula coste estimado por tipo de tarea.
- Usa `quality_profiles.json` para scores auditables.
- Ranking de calidad/precio para coding, agentic coding, reasoning y general.
- Distingue mejores opciones gratis.
- Detecta bajadas/subidas comparando con el snapshot anterior.
- Mantiene el informe aunque falle la llamada al LLM gratuito.
- `openrouter/free` sólo redacta el resumen; los números salen de Python.

## Archivos nuevos/importantes

- `quality_profiles.json`: heurísticas de calidad editables.
- `src/filters.py`: filtros de modelos irrelevantes.
- `src/quality.py`: asignación de perfiles.
- `src/scoring.py`: coste y Value Score.
- `src/main.py`: ranking e informe.

## Actualización sobre una instalación v1

Conserva tus carpetas `data/` y `reports/`.
Reemplaza los archivos de código/configuración con los de este paquete y ejecuta
Actions → AI Price Radar → Run workflow.
