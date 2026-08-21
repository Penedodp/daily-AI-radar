# AI Price Radar v3

## Qué cambia

- Separa completamente rankings GRATIS y DE PAGO.
- Añade un ranking premium por calidad.
- Compara el mismo modelo entre proveedores/rutas.
- Añade collectors opcionales para:
  - OpenRouter
  - CheaperInference
  - Together AI
  - Novita AI
  - rutas internas de OpenRouter (si la key tiene permisos)
- Solo llama "bajada/descuento" a una reducción histórica del mismo proveedor/ruta.
- Las diferencias simultáneas entre proveedores se muestran como "ahorro entre rutas".

## Secrets

Ya existente:
- `OPENROUTER_API_KEY`

Opcionales:
- `CHEAPER_INFERENCE_API_KEY`
- `TOGETHER_API_KEY`
- `NOVITA_API_KEY`
- `OPENROUTER_MANAGEMENT_API_KEY`

Si un secret opcional no existe, el collector se salta sin romper el workflow.

## Actualización desde v2

Conserva `data/` y `reports/`.

Reemplaza:
- `.github/workflows/daily.yml`
- `config.json`
- `quality_profiles.json`
- `requirements.txt`
- `src/main.py`
- `src/filters.py`
- `src/quality.py`
- `src/scoring.py`
- `src/report_ai.py`
- `src/providers/openrouter.py`

Añade:
- `model_aliases.json`
- `src/normalize.py`
- `src/providers/common.py`
- `src/providers/registry.py`
- `src/providers/cheaperinference.py`
- `src/providers/together.py`
- `src/providers/novita.py`
- `src/providers/openrouter_routes.py`
