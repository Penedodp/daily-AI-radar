# Daily AI Radar

Radar diario (GitHub Actions) que compara el catálogo de modelos de IA de varios
proveedores, calcula el coste **estimado** por tipo de tarea y genera un ranking de
mejores opciones **hoy**, separando modelos gratis de modelos de pago.

El foco principal es **programación** (coding), donde la calidad se puntúa de
forma automática — no hace falta editar nada a mano cuando sale un modelo
nuevo. El proyecto prioriza **fiabilidad sobre cobertura**: prefiere un dato
desconocido a una conclusión que los datos no respaldan (ver
`DAILY_AI_RADAR_CLAUDE_PLAN.md` para el criterio completo).

## Estructura de páginas

El dashboard son 4 páginas estáticas, no una sola tabla interminable:

- **`docs/index.html` (Radar)** — decisión rápida: mejores opciones, gratis
  destacados, value/calidad, ahorro entre proveedores, Top 5, movimientos de
  precio. Nunca renderiza el catálogo completo.
- **`docs/explorer.html` (Explorer)** — profundidad: catálogo completo con
  búsqueda, filtros, perfil de coste personalizado, comparador multi-modelo
  y detalle de rutas. Enlazado desde Radar ("Explorar todos los modelos →").
- **`docs/methodology.html` (Metodología)** — confianza: fuentes, reglas de
  pricing/gratis, alcance de benchmark, identidad de ruta, scoring y Data
  Health.
- **`docs/benchmarks.html` (Benchmarks)** — placeholder "Próximamente",
  reservado para Benchmark Engine v2 (todavía sin empezar).

Las cuatro comparten cabecera, navegación (`RADAR | EXPLORER | BENCHMARKS |
METODOLOGÍA`, con estado activo visible) y el mismo CSS/JS — sin
`prefers-reduced-motion` en ninguna, por decisión explícita del usuario.

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
original no lleve NINGÚN token (tamaño, fecha/checkpoint, palabra de variante,
o cualquier otra cosa) que la regla no represente ya. La política es una
**lista blanca, no una lista negra**: solo convergen diferencias puramente
sintácticas (separadores, mayúsculas, puntuación decimal); cualquier resto
semántico —conocido o no— bloquea el alias, en vez de dejar pasar solo los
que ya conocíamos como peligrosos (`distill`, `sante`, `fin`...). Este cambio
de política (PRE_BENCH_V2_FINAL_CLEANUP) corrigió un falso merge real:
`Ling-3.0-Flash`, `Ling-3.0-Flash-Sante` y `Ling-3.0-Flash-Fin` son
checkpoints especializados distintos de Novita y antes colapsaban en uno
solo. Por eso `deepseek-r1`, `deepseek-r1-0528` y
`deepseek-r1-distill-llama-70b` (o `ling-3.0-flash` y `ling-3.0-flash-sante`)
quedan como modelos distintos en vez de uno solo — ver
`tests/test_normalize.py`.

La comparación "mismo modelo, ruta más barata" (sección 🔀) solo compara
rutas cuyo `canonical_model` coincide exactamente por esta vía.

### Identidad de modelo vs. identidad de ruta/endpoint

`route_identity()` (`route_identity_v1`) es una identidad **más fina** que el
`canonical_model`: incluye `route_tag` y `quantization`, y para rutas de
OpenRouter usa el `provider_name` crudo de la API en vez de la etiqueta
sintetizada para mostrar en pantalla (nunca la display label como identidad).
Se usa para deduplicar, para detectar movimientos de precio y para el
histórico — así "OpenAI Standard" y "OpenAI Flex", o dos cuantizaciones del
mismo modelo, nunca se confunden entre sí ni con la ruta ganadora de otro
día. Ver `tests/test_routes.py`.

### `benchmark_scope`

Todo score de calidad de hoy mide el **modelo/checkpoint** (`benchmark_scope
= "model"`), nunca un endpoint concreto — una ruta con una cuantización
distinta (FP4, por ejemplo) puede comportarse de forma distinta y no ha sido
medida por separado. El dato queda explícito en cada score (tooltip y JSON)
para que nunca se insinúe lo contrario. Es el punto de extensión pensado
para que un futuro benchmark a nivel de endpoint pueda coexistir sin rehacer
el modelo de datos.

### Model Benchmark Registry

Un benchmark mide el **modelo canónico**, no la cadena cruda de una ruta
concreta. Antes, cada ruta buscaba su propio match de benchmark por su
propio `model_id` — así que dos rutas del mismo modelo (dos proveedores con
la ruta de OpenRouter, por ejemplo) podían acabar con cobertura de benchmark
distinta solo porque uno de los dos slugs no encajó con el fuzzy-match del
leaderboard. `main.py::build_model_benchmark_registry()` corrige esto:
agrupa todos los matches por `canonical_model`, se queda con el de mayor
confianza (`match_ratio`) por cada fuente, y todas las rutas de ese modelo
comparten exactamente el mismo resultado. Ver
`tests/test_model_benchmark_registry.py`.

## "Gratis" no es lo mismo que precio 0

Un `0`/`0` de un proveedor puede significar gratis, pero también capacidad
dedicada sin tarifa serverless, precio no disponible, o un valor ausente
convertido a cero. `src/scoring.py::compute_pricing_status` solo marca una
ruta como `free`/`promotional_free` cuando existe una señal verificable:
- una señal del propio collector (hoy: el sufijo `:free` de OpenRouter), o
- un **override de proveedor verificado a mano**
  (`config/provider_pricing_overrides.json`) con `verified_at` y
  `source_url` — usado, por ejemplo, para Ling-3.0-Flash-Fin/-Sante de
  Novita, que la API reporta como `0/0` pero que Novita publica
  explícitamente como gratis/promocional en su propia página de precios.

Cualquier otro `0`/`0` sin señal queda como `unknown` y **no** entra ni en el
ranking de gratis ni en el de pago (no sabemos su coste real). Un override
con más de `staleness_days` (30 por defecto) sin volver a verificarse se
marca `pricing_overrides_stale` en Data Health — no se invalida solo, pero
deja de mostrarse con la misma confianza que uno recién comprobado.
Ver `tests/test_pricing_overrides.py`.

## Puntuación de calidad: automática, no manual

- **Coding**: pass-rate del Aider Polyglot Leaderboard y rating Elo de LMArena
  WebDev Arena, escalados a 0–10 **cada uno por separado** (ninguno es
  "principal" ni "de respaldo" del otro — un modelo con match en ambos
  conserva las dos puntuaciones de forma independiente). El matching es
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

## Gratis: qué es "disponible hoy" vs "mejor puntuado"

El dashboard separa dos preguntas distintas. **"Mejor opción gratuita
puntuada"** solo muestra un modelo si además tiene benchmark comparable.
**"Modelos gratuitos disponibles hoy"** lista TODAS las rutas verificadas
como gratis, tengan o no benchmark, en un orden neutral (nunca por calidad
cuando no la tienen). Cada `FREE ⓘ` es un popover accesible (click, tap o
foco+Enter — nunca depende solo de `title`) con los límites conocidos del
proveedor, cargados desde `config/free_tiers.json` (editable sin tocar
código). `openrouter/free` se trata como lo que es — un **router** que
selecciona un modelo compatible por petición, no un checkpoint — así que
nunca recibe una puntuación propia ni aparece en el Explorador de modelos
(que es, por definición, de modelos). Ver `tests/test_free_tiers.py`.

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

## Movimientos de precio: tarifa real, no coste estimado

Una bajada/subida compara **tarifas** (`input_usd_per_million`/
`output_usd_per_million`, misma `route_identity`) frente al snapshot
anterior — nunca el `weighted_cost`, que también cambiaría si se edita
`task_profiles` en `config.json` sin que ningún proveedor haya tocado su
precio. El coste estimado del perfil se sigue registrando por separado
(`estimated_cost_change_pct`) pero nunca se llama "cambio de precio". Ver
`tests/test_price_changes.py`.

## Best Market History (no "histórico del modelo")

El gráfico de evolución de coste de cada categoría es explícitamente **Best
Market History**: el coste de la ruta más barata cada día, que puede cambiar
de proveedor de un día a otro — no el histórico de una ruta fija. El
dashboard lo etiqueta así (no "histórico del modelo") y avisa cuando el
proveedor ganador cambió durante el periodo mostrado, o cuando
`scoring_version` cambió a mitad de serie (los puntos ya no usan
necesariamente la misma fórmula). `main.py::endpoint_price_trend()` es la
base preparada (no expuesta todavía en el dashboard) para un futuro
histórico por-ruta que nunca mezcle dos `route_identity` distintas.

## Data Health

La sección "Metodología y Data Health" del dashboard expone, por snapshot:
filas en bruto, duplicados eliminados, rutas con precio desconocido,
modelos con benchmark propio vs. endpoints que solo heredan el score de su
modelo vs. endpoints benchmarkeados específicamente (hoy, siempre 0 — no
existe todavía una fuente a nivel de endpoint), y el recuento de avisos de
validación. También incluye `calculation_context` (perfiles de tarea,
ancla de Radar Value, y las versiones `scoring_version` /
`benchmark_normalization_version` / `route_identity_version` — un snapshot
antiguo nunca se reinterpreta con una fórmula nueva).

## Tests

```bash
pip install -r requirements.txt
python -m pytest tests/ -q
```

El workflow diario ejecuta `pytest` **antes** de generar nada — si falla, no
se publica. Los tests cubren identidad de modelo (`test_normalize.py`,
incluida la política de sufijo-desconocido y el caso Ling-3.0-Flash),
matching de benchmark (`test_quality_bench.py`), el Model Benchmark Registry
(`test_model_benchmark_registry.py`), estado de precio/gratis
(`test_scoring.py`), overrides de precio verificados
(`test_pricing_overrides.py`), etiquetado/identidad/deduplicación de rutas
(`test_routes.py`), movimientos de precio basados en tarifa real
(`test_price_changes.py`), gratis/router/free-tiers (`test_free_tiers.py`),
renderizado HTML incluida la regresión de `colspan` (`test_report_html.py`)
un fixture de extremo a extremo (`test_snapshot_validation.py`) que
reproduce los casos de los documentos de auditoría (variantes DeepSeek,
standard/flex, Aider vs WebDev sin mezclarse ni con `max()`, precio
`unknown`, Qwen3.8 dash/dot, etc), y la separación Radar/Explorer/
Metodología, exclusión del router y overrides namespaced
(`test_final_ux_architecture.py`). No dependen de red.

## Estructura

- `src/main.py` — orquesta collectors, matching, scoring y genera el informe.
- `src/providers/` — un collector por proveedor de precios.
- `src/quality_bench.py` — descarga y matching de los benchmarks de coding.
- `src/normalize.py` — canonicaliza IDs de modelo para comparar entre proveedores.
- `src/scoring.py` — coste por tarea, coste ponderado, value score, estado de precio.
- `src/report_ai.py` — resumen en español generado con un modelo gratis de OpenRouter.
- `src/report_html.py` — dashboard estático publicado en `docs/` (GitHub Pages).
- `model_aliases.json` — reglas de canonicalización (editable).
- `config/free_tiers.json` — condiciones de free tier por proveedor (editable, sin tocar código).
- `config/provider_pricing_overrides.json` — clasificaciones `free`/`promotional_free` verificadas a mano para precios `0/0` ambiguos (editable, con `verified_at`/`source_url`).
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
- El coste estimado no tiene en cuenta el porcentaje de cache hit todavía.
- Un precio `unknown` que en realidad sea `dedicated`/`byok`/`contact_sales`
  se queda como `unknown` hasta tener una señal explícita del proveedor —
  nunca se infiere sin evidencia.
- No existe todavía ningún benchmark a nivel de endpoint (por ruta/
  cuantización) — `endpoint_specific_benchmarks` es siempre 0 hoy, y es la
  respuesta correcta, no un hueco.
- El histórico por-ruta (`endpoint_price_trend`) existe como función base
  pero no está expuesto todavía en el dashboard — solo Best Market History.
- El comparador (Explorer) ya es multi-benchmark y transpuesto (una fila por
  fuente de benchmark, raw score primero, badge MODEL/ENDPOINT visible), pero
  compara solo **modelos** — no existe todavía un comparador **ruta-vs-ruta**
  separado (provider/endpoint/quantization/latencia/throughput/uptime lado a
  lado).
- No hay cupos por categoría (recomendación/gratis/price-mover/...) al elegir
  qué modelos de OpenRouter monitorizar — la selección es una unión simple, y
  no se guarda un `route_monitor_reason` explícito por ruta.
- La paginación del Explorer (50/100/Todos) es solo de visibilidad en el DOM
  — todas las filas se generan en el HTML estático; no existe un
  `explorer-data.json` cargado bajo demanda.
- `docs/benchmarks.html` es un placeholder "Próximamente" — Benchmark Engine
  v2 no ha empezado.
- El pase de móvil se ha validado por CSS/estructura (sin scroll horizontal
  global, texto largo con salto de línea, popovers por tap, tablas con
  columna sticky en el comparador) pero no con un navegador real en
  dispositivos físicos — no hay smoke tests Playwright todavía (ver el
  propio documento de arquitectura, que lo deja como opcional).

Ver `DAILY_AI_RADAR_CLAUDE_PLAN.md`, `DAILY_AI_RADAR_CONTINUACION_AUDITORIA_2.md`,
`DAILY_AI_RADAR_CONTINUACION_AUDITORIA_3.md`,
`DAILY_AI_RADAR_PRE_BENCH_V2_FINAL_CLEANUP.md` y
`DAILY_AI_RADAR_FINAL_PRE_BENCH_V2_UX_ARCHITECTURE.md` para el historial completo de
auditoría y las mejoras pendientes (histórico por ruta/endpoint expuesto en
UI, "ruta ganadora" guardada explícitamente en el histórico, señales de
alerta 7/30d, simulador de cache hit, comparador multi-benchmark completo,
cupos de monitorización, Benchmark Engine v2, etc.).
