# Daily AI Radar — 2026-11-24

> Generado 24/11/2026 19:31 WET · **735 modelos únicos** · **1286 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **244 endpoints de 35 modelos OpenRouter monitorizados** · **79 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 79 modelos con benchmark propio, 318 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_115 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 426 |
| cheaperinference | `ok` | 348 |
| together | `ok` | 196 |
| novita | `ok` | 80 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 161 |
| openrouter_routes | `ok` | 244 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| — | — | Ningún modelo gratuito puntuado todavía | — | — | — | — |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **inkling-2-small** | **OpenRouter → PrimeIntellect (primeintellect/flex)** | $0.00375 | $0.0750 | $0.2500 | 8.7/10 | 83.9 |

## 🧠 Mayor puntuación entre modelos de pago (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad |
|---|---|---|---|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **o3** | OpenRouter | $0.10800 | $2.0000 | $8.0000 | 7.7/10 |
| 💻 Coding | LMArena WebDev Arena | **qwen3.8-max-0902** | OpenRouter | $0.09600 | $2.0000 | $6.0000 | 9.0/10 |

_Próximamente: 🤖 Agentic coding · 🧠 Razonamiento · ⚡ General (sin benchmark automatizado todavía)._

\* *Aider Polyglot Leaderboard (pass-rate de un test de corrección fijo) y LMArena WebDev Arena (rating Elo por voto humano) son benchmarks distintos, escalados a 0–10 cada uno por separado. **Nunca se ordenan entre sí como si fueran la misma escala** — cada tabla indica la fuente exacta junto al dato, no solo al pasar el ratón por encima. Emparejados automáticamente por nombre de modelo; sin match fiable, el modelo queda sin puntuar en vez de estimarse.*

\*\* *Radar Value es un índice propio (no un benchmark) que combina calidad medida y coste estimado: `calidad × 10 / sqrt(1 + coste_tarea / 0.05)`. El ancla de 0.05 USD/tarea es el punto en el que empieza a penalizar el coste; es configurable en `config.json`.*

## 🔀 Mismo modelo, proveedor/ruta más barata

| Modelo | Más barato | Coste perfil | $/M input | $/M output | Siguiente | Ahorro vs siguiente |
|---|---|---:|---:|---:|---|---:|
| **qwen-mt-plus** | **Novita AI** | $0.01306 | $0.2500 | $0.7500 | CheaperInference ($0.08348) | **84.4%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02765) | **74.6%** |
| **mythomax-l2-13b** | **Novita AI** | $0.00350 | $0.0900 | $0.0900 | OpenRouter ($0.01301) | **73.1%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **deepseek-v4-flash-vision-exp** | **CheaperInference** | $0.00777 | $0.1320 | $0.5280 | OpenRouter ($0.02298) | **66.2%** |
| **llama-4-maverick** | **CheaperInference** | $0.00654 | $0.1222 | $0.3900 | OpenRouter ($0.01795) | **63.6%** |
| **deepseek-v4-pro** | **CheaperInference** | $0.02241 | $0.4290 | $1.2870 | OpenRouter ($0.05835) | **61.6%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00577 | $0.0800 | $0.4800 | OpenRouter ($0.01443) | **60.0%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **qwen3.5-9b** | **CheaperInference** | $0.00292 | $0.0690 | $0.1035 | OpenRouter ($0.00715) | **59.2%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **sonar** | **CheaperInference** | $0.01605 | $0.1625 | $1.6250 | OpenRouter ($0.03895) | **58.8%** |
| **qwen3.8-27b** | **CheaperInference** | $0.00408 | $0.0750 | $0.2500 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **57.3%** |
| **hy4-flash** | **CheaperInference** | $0.00093 | $0.0158 | $0.0632 | OpenRouter ($0.00206) | **55.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02627 (\$0.4845 in / \$1.9550 out) · Radar Value 47.8
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.09180 (\$1.7000 in / \$6.8000 out) · Radar Value 45.7
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **inkling-2-small** vía **OpenRouter → PrimeIntellect (primeintellect/flex)** — calidad 8.7/10 · coste/tarea $0.00375 (\$0.0750 in / \$0.2500 out) · Radar Value 83.9
2. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.6/10 · coste/tarea $0.00382 (\$0.0910 in / \$0.1820 out) · Radar Value 82.9
3. **glm-5.3-flash** vía **CheaperInference** — calidad 8.3/10 · coste/tarea $0.00118 (\$0.0281 in / \$0.0565 out) · Radar Value 82.0
4. **hy4** vía **CheaperInference** — calidad 8.8/10 · coste/tarea $0.00901 (\$0.1877 in / \$0.5627 out) · Radar Value 81.0
5. **qwen3.8-27b** vía **CheaperInference** — calidad 8.0/10 · coste/tarea $0.00375 (\$0.0750 in / \$0.2500 out) · Radar Value 77.2

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-v4-pro-0813** vía **OpenRouter** — **-91.6%** (ahora \$0.1110 in / \$4.4400 out)
- **deepseek-v4.1-flash** vía **OpenRouter** — **-83.1%** (ahora \$0.0507 in / \$0.2028 out)
- **deepseek-v4-flash** vía **OpenRouter** — **-54.7%** (ahora \$0.0453 in / \$0.1360 out)
- **hy3** vía **OpenRouter** — **-43.1%** (ahora \$0.0825 in / \$0.3300 out)
- **mimo-v2.6-flash** vía **OpenRouter → Makora (makora/fp8)** — **-30.0%** (ahora \$0.1400 in / \$0.2800 out)
- **glm-5.3-flash** vía **CheaperInference** — **-29.8%** (ahora \$0.0281 in / \$0.0565 out)
- **nemotron-3.5-lightning** vía **OpenRouter** — **-28.6%** (ahora \$0.0500 in / \$0.2000 out)
- **glm-4.5** vía **CheaperInference** — **-25.9%** (ahora \$0.3300 in / \$1.2100 out)
- **glm-flash** vía **OpenRouter** — **-25.1%** (ahora \$0.0356 in / \$0.0815 out)
- **glm-5.3-flash** vía **OpenRouter → Relace (relace/fp4)** — **-25.1%** (ahora \$0.0356 in / \$0.0815 out)
- **glm-5.1** vía **CheaperInference** — **-24.4%** (ahora \$0.6149 in / \$2.3200 out)
- **apex** vía **CheaperInference** — **-23.5%** (ahora \$0.3250 in / \$1.9500 out)

### Subidas

- **llama-3.1-8b-instruct** vía **OpenRouter** — +150.0% (ahora \$0.0500 in / \$0.0800 out)
- **deepseek-v4-flash-vision-exp** vía **OpenRouter** — +104.1% (ahora \$0.4400 in / \$1.3200 out)
- **qwen3.8-27b** vía **OpenRouter** — +71.4% (ahora \$0.0600 in / \$1.9600 out)
- **deepseek-v4-pro** vía **OpenRouter** — +70.7% (ahora \$1.2800 in / \$2.5600 out)
- **deepseek-v4-pro-0813** vía **CheaperInference** — +60.8% (ahora \$0.5306 in / \$1.5919 out)
- **qwen3.8-27b** vía **CheaperInference** — +47.1% (ahora \$0.0750 in / \$0.2500 out)
- **qwen4-max** vía **Together AI** — +42.9% (ahora \$1.5000 in / \$4.5000 out)
- **hy4** vía **OpenRouter → DeepInfra (deepinfra/fp4)** — +33.3% (ahora \$0.8340 in / \$2.5010 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
