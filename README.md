# AI Price Radar

Radar diario (GitHub Actions) que compara el catálogo de modelos de IA de varios
proveedores, calcula el coste real por tipo de tarea y genera un ranking de
mejores opciones **hoy**, separando modelos gratis de modelos de pago.

El foco principal es **programación** (coding), donde la calidad se puntúa de
forma automática — no hace falta editar nada a mano cuando sale un modelo
nuevo.

## Qué hace cada mañana

1. Descarga el catálogo de precios de cada proveedor configurado.
2. Descarga el [Aider Polyglot Leaderboard](https://github.com/Aider-AI/aider)
   (benchmark público de programación, sin API key) y empareja automáticamente
   sus resultados con los IDs de modelo de cada proveedor.
3. Calcula el coste estimado por tarea (coding, agentic, razonamiento, general)
   según el mix de tokens de entrada/salida de cada perfil.
4. Genera `reports/<fecha>.md` y `reports/latest.md` con:
   - mejor opción gratis,
   - mejor relación calidad/precio de pago,
   - opción premium por calidad,
   - oportunidades de usar el mismo modelo por una ruta/proveedor más barata,
   - bajadas/subidas de precio reales (mismo proveedor/ruta vs. el día anterior).
5. Comitea `data/<fecha>.json` (snapshot completo) y el informe.

## Puntuación de calidad: automática, no manual

- **Coding**: pass-rate del Aider Polyglot Leaderboard, escalado a 0–10. El
  matching entre el nombre del benchmark y el ID del proveedor es estricto —
  los números de versión (`3` vs `3.5`, `k2` vs `k2.5`...) deben coincidir
  exactamente, o el modelo se queda sin puntuar. Es preferible no puntuar un
  modelo a puntuarlo mal.
- **Agentic / razonamiento / general**: todavía no tienen una fuente de
  benchmark pública igual de fiable y automatizable. El informe lo indica
  explícitamente en vez de rellenar con una estimación. Es la siguiente pieza
  pendiente de esta auditoría.

No hay ningún archivo de calidad curado a mano que mantener.

## Secrets (GitHub → Settings → Secrets and variables → Actions)

| Secret | Obligatorio | Proveedor |
|---|---|---|
| `OPENROUTER` | Sí | OpenRouter (el listado de modelos es público, pero se usa para el resumen IA) |
| `TOGETHERAI` | No | Together AI |
| `NOVIA_AI` | No | Novita AI |
| `CHEAPERINFERENCE` | No | CheaperInference |
| `OPENROUTER_MANAGEMENT_API_KEY` | No | Rutas internas de OpenRouter (uptime/latencia por endpoint) |

Si un secret opcional no existe, ese collector se salta sin romper el
workflow (aparece como `not_configured_or_empty` en la sección "Fuentes" del
informe).

## Ejecutar en local

```bash
pip install -r requirements.txt
python src/main.py
```

Variables de entorno equivalentes a los secrets de arriba:
`OPENROUTER_API_KEY`, `TOGETHER_API_KEY`, `NOVITA_API_KEY`,
`CHEAPER_INFERENCE_API_KEY`, `OPENROUTER_MANAGEMENT_API_KEY`.

## Estructura

- `src/main.py` — orquesta collectors, matching, scoring y genera el informe.
- `src/providers/` — un collector por proveedor de precios.
- `src/quality_bench.py` — descarga y matching del benchmark de coding.
- `src/normalize.py` — canonicaliza IDs de modelo para comparar entre proveedores.
- `src/scoring.py` — coste por tarea, coste ponderado, value score.
- `src/report_ai.py` — resumen en español generado con un modelo gratis de OpenRouter.
- `model_aliases.json` — reglas de canonicalización (editable).
- `data/` — snapshots diarios completos + caché del benchmark.
- `reports/` — informe diario en Markdown.
