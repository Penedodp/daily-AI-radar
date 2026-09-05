# Daily AI Radar

Radar diario (GitHub Actions) que compara el catálogo de modelos de IA de varios
proveedores, calcula el coste **estimado** por tipo de tarea y genera un ranking de
mejores opciones **hoy**, separando modelos gratis de modelos de pago.

El foco principal es **programación** (coding), donde la calidad se puntúa de
forma automática — no hace falta editar nada a mano cuando sale un modelo
nuevo. El proyecto prioriza **fiabilidad sobre cobertura**: prefiere un dato
desconocido a una conclusión que los datos no respaldan (ver
`DAILY_AI_RADAR_CLAUDE_PLAN.md` para el criterio completo).

## Qué hace cada mañana

1. Descarga el catálogo de precios de cada proveedor configurado.
2. Descarga el [Aider Polyglot Leaderboard](https://github.com/Aider-AI/aider)
   (test de corrección fijo, prioritario) y el
   [LMArena WebDev Arena](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset)
   (Elo por voto humano, respaldo con más cobertura) — ambos sin API key — y
   empareja automáticamente sus resultados con los IDs de modelo de cada
   proveedor.
3. Calcula el coste estimado por tarea (coding, agentic, razonamiento, general)
   según el mix de tokens de entrada/salida de cada perfil.
4. Deduplica rutas exactas (mismo proveedor + id + tag/quantization) y valida
   el snapshot: si encuentra un error crítico (precio inválido, identidad
   inconsistente, benchmark sin fuente trazable...) **no publica** — sale con
   código de error antes de escribir nada, y el workflow no llega al commit.
5. Genera `reports/<fecha>.md`, `reports/latest.md` y `docs/index.html` con:
   - mejor opción gratis (verificada, no solo precio 0),
   - mejor relación calidad/precio **por fuente de benchmark** (Aider y
     WebDev Arena nunca compiten en el mismo ranking),
   - mayor puntuación entre modelos de pago con benchmark disponible,
   - oportunidades de usar el mismo modelo por una ruta/proveedor más barata,
   - bajadas/subidas de precio reales (mismo proveedor/ruta vs. el snapshot
     anterior — con su fecha real, no siempre "ayer").
6. Comitea `data/<fecha>.json` (snapshot completo) y el informe.

## Identidad de modelo: conservadora por diseño

`model_aliases.json` sigue teniendo reglas "de familia" (una sola regex para
todas las variantes de `deepseek*r1*`, por ejemplo) porque hace falta para
unificar cómo distintos proveedores escriben el mismo checkpoint. Pero antes
de aplicar cualquiera de esas reglas, `src/normalize.py` comprueba que el id
original no lleve un tamaño (`32b`), fecha/checkpoint (`0528`, `20240806`) o
palabra de variante (`distill`, `instruct`, `preview`, `thinking`...) que la
regla no represente ya. Si lo lleva, la regla se descarta y el modelo cae al
normalizado seguro (solo formato, nunca fusiona información), en vez de
fusionarse con un checkpoint distinto. Por eso `deepseek-r1`,
`deepseek-r1-0528` y `deepseek-r1-distill-llama-70b` quedan como tres modelos
distintos en vez de uno solo — ver `tests/test_normalize.py`.

La comparación "mismo modelo, ruta más barata" (sección 🔀) solo compara
rutas cuyo `canonical_model` coincide exactamente por esta vía.

## "Gratis" no es lo mismo que precio 0

Un `0`/`0` de un proveedor puede significar gratis, pero también capacidad
dedicada sin tarifa serverless, precio no disponible, o un valor ausente
convertido a cero. `src/scoring.py::compute_pricing_status` solo marca una
ruta como `free` cuando hay una señal explícita y comprobable (hoy: el sufijo
`:free` de OpenRouter); cualquier otro `0`/`0` queda como `unknown` y **no**
entra ni en el ranking de gratis ni en el de pago (no sabemos su coste real).
Ver `tests/test_scoring.py`.

## Puntuación de calidad: automática, no manual

- **Coding**: pass-rate del Aider Polyglot Leaderboard (prioritario) o rating
  Elo de LMArena WebDev Arena (respaldo), escalados a 0–10. El matching es
  estricto: los números de versión y fechas de checkpoint (`3` vs `3.5`,
  `k2` vs `k2.5`, `0324` vs `0824`...) deben coincidir exactamente, y no se
  eliminan palabras que puedan distinguir un checkpoint (`base`, `instruct`,
  `thinking`, `preview`, `chat`, `exp`...) antes de comparar. Si no hay
  coincidencia fiable, el modelo se queda sin puntuar en vez de estimarse.
  Ver `tests/test_quality_bench.py`.
- Aider y LMArena miden cosas distintas (corrección de código vs. preferencia
  humana en apps web) y sus puntuaciones **no son directamente comparables**
  entre sí. Por eso `recommendations()` produce un ranking independiente por
  cada `(categoría, fuente)` — nunca un único ranking que mezcle ambas
  escalas — y la fuente exacta se muestra siempre junto al dato, no solo en
  el tooltip. Ver `tests/test_snapshot_validation.py::test_aider_and_webdev_never_rank_against_each_other`.
- Se guarda también el score crudo (`raw_score`/`raw_unit`: `% pass rate` o
  `Elo`), la fecha de captura del benchmark y su URL — visibles en el
  tooltip de cada score.
- **Agentic / razonamiento / general**: todavía no tienen una fuente de
  benchmark pública igual de fiable y automatizable. El informe lo indica
  explícitamente en vez de rellenar con una estimación.

No hay ningún archivo de calidad curado a mano que mantener.

## Radar Value

`Radar Value` es un índice propio de este proyecto (no un benchmark):
`calidad × 10 / sqrt(1 + coste_tarea / value_cost_anchor_usd)`. Combina
calidad medida y coste estimado para ordenar opciones "por valor", y se
etiqueta como tal en el informe para no confundirlo con una puntuación de
benchmark. `value_cost_anchor_usd` (`config.json`) es el punto de coste a
partir del cual empieza a penalizar.

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

## Validación del snapshot: warnings vs errors

`main.py::validate_snapshot` corre en cada ejecución, antes de escribir
ningún archivo, y distingue dos niveles:

- **ERROR** (bloquea la publicación, `sys.exit(1)`): ruta duplicada tras
  deduplicar, precio inválido (negativo/NaN/Infinito), `free=true` sin
  `pricing_status` verificado, benchmark sin fuente/label trazable, o un
  mismo `canonical_model` agrupando tamaños de modelo distintos.
- **WARNING** (se registra, no bloquea): rutas con precio `unknown`, modelos
  sin ningún benchmark todavía. Son condiciones esperadas del día a día.

## Tests

```bash
pip install -r requirements.txt
python -m pytest tests/ -q
```

El workflow diario ejecuta `pytest` **antes** de generar nada — si falla, no
se publica. Los tests cubren identidad de modelo (`test_normalize.py`),
matching de benchmark (`test_quality_bench.py`), estado de precio/gratis
(`test_scoring.py`), etiquetado y deduplicación de rutas (`test_routes.py`),
y un fixture de extremo a extremo (`test_snapshot_validation.py`) y de
renderizado HTML (`test_report_html.py`) que reproducen los casos de ambos
documentos de auditoría (variantes DeepSeek, standard/flex, Aider vs WebDev,
precio `unknown`, etc). No dependen de red.

## Estructura

- `src/main.py` — orquesta collectors, matching, scoring y genera el informe.
- `src/providers/` — un collector por proveedor de precios.
- `src/quality_bench.py` — descarga y matching de los benchmarks de coding.
- `src/normalize.py` — canonicaliza IDs de modelo para comparar entre proveedores.
- `src/scoring.py` — coste por tarea, coste ponderado, value score, estado de precio.
- `src/report_ai.py` — resumen en español generado con un modelo gratis de OpenRouter.
- `src/report_html.py` — dashboard estático publicado en `docs/` (GitHub Pages).
- `model_aliases.json` — reglas de canonicalización (editable).
- `data/` — snapshots diarios completos + caché de benchmarks.
- `reports/` — informe diario en Markdown.
- `docs/` — dashboard HTML publicado vía GitHub Pages.
- `tests/` — tests de regresión de las reglas críticas.

## Limitaciones conocidas

- Los precios pueden cambiar durante el día; el snapshot es de un momento dado
  (ver timestamp y frescura en la cabecera del dashboard).
- Un modelo sin benchmark no significa baja calidad — significa que no hay
  dato fiable todavía.
- Latencia/throughput (cuando existen, vía rutas de OpenRouter) pueden variar
  por región/carga.
- Agentic, razonamiento y general no tienen benchmark automatizado todavía.

Ver `DAILY_AI_RADAR_CLAUDE_PLAN.md` y `DAILY_AI_RADAR_CONTINUACION_AUDITORIA_2.md`
para el historial completo de auditoría y las mejoras pendientes (histórico
por ruta, señales de alerta 7/30d, simulador de cache hit, vistas
más-rápido/más-estable por ruta, etc.).
