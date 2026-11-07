# Daily AI Radar — 2026-11-07

> Generado 07/11/2026 14:55 WET · **738 modelos únicos** · **1416 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **367 endpoints de 35 modelos OpenRouter monitorizados** · **81 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 81 modelos con benchmark propio, 345 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_120 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 416 |
| cheaperinference | `ok` | 351 |
| together | `ok` | 191 |
| novita | `ok` | 99 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 152 |
| openrouter_routes | `ok` | 367 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| — | — | Ningún modelo gratuito puntuado todavía | — | — | — | — |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **OpenRouter → Darkbloom (darkbloom/fp4)** | $0.00468 | $0.1000 | $0.2800 | 8.6/10 | 82.2 |

## 🧠 Mayor puntuación entre modelos de pago (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad |
|---|---|---|---|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **o3** | OpenRouter | $0.10800 | $2.0000 | $8.0000 | 7.7/10 |
| 💻 Coding | LMArena WebDev Arena | **qwen3.8-max-0902** | OpenRouter | $0.09600 | $2.0000 | $6.0000 | 9.1/10 |

_Próximamente: 🤖 Agentic coding · 🧠 Razonamiento · ⚡ General (sin benchmark automatizado todavía)._

\* *Aider Polyglot Leaderboard (pass-rate de un test de corrección fijo) y LMArena WebDev Arena (rating Elo por voto humano) son benchmarks distintos, escalados a 0–10 cada uno por separado. **Nunca se ordenan entre sí como si fueran la misma escala** — cada tabla indica la fuente exacta junto al dato, no solo al pasar el ratón por encima. Emparejados automáticamente por nombre de modelo; sin match fiable, el modelo queda sin puntuar en vez de estimarse.*

\*\* *Radar Value es un índice propio (no un benchmark) que combina calidad medida y coste estimado: `calidad × 10 / sqrt(1 + coste_tarea / 0.05)`. El ancla de 0.05 USD/tarea es el punto en el que empieza a penalizar el coste; es configurable en `config.json`.*

## 🔀 Mismo modelo, proveedor/ruta más barata

| Modelo | Más barato | Coste perfil | $/M input | $/M output | Siguiente | Ahorro vs siguiente |
|---|---|---:|---:|---:|---|---:|
| **mercury-2.5** | **CheaperInference** | $0.00034 | $0.0060 | $0.0225 | OpenRouter ($0.00229) | **85.0%** |
| **qwen-mt-plus** | **Novita AI** | $0.01306 | $0.2500 | $0.7500 | CheaperInference ($0.08348) | **84.4%** |
| **mimo-v2.5** | **CheaperInference** | $0.00543 | $0.1190 | $0.2380 | OpenRouter ($0.02621) | **79.3%** |
| **qwen3-coder** | **OpenRouter** | $0.01633 | $0.3000 | $1.0000 | CheaperInference ($0.06389) | **74.4%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02431) | **71.1%** |
| **gpt-oss-120b** | **OpenRouter** | $0.00097 | $0.0170 | $0.0630 | Novita AI ($0.00328) | **70.5%** |
| **mistral-nemo** | **OpenRouter** | $0.00114 | $0.0290 | $0.0300 | CheaperInference ($0.00380) | **70.1%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **deepseek-v4-flash** | **OpenRouter** | $0.00246 | $0.0471 | $0.1412 | CheaperInference ($0.00751) | **67.2%** |
| **particle-1** | **OpenRouter** | $0.00494 | $0.0500 | $0.5000 | CheaperInference ($0.01251) | **60.5%** |
| **deepseek-v4-flash-0731** | **OpenRouter** | $0.00390 | $0.0590 | $0.3000 | CheaperInference ($0.00977) | **60.1%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **gemini-4-argon** | **CheaperInference** | $0.05897 | $0.9000 | $4.5000 | OpenRouter ($0.13105) | **55.0%** |
| **gemini-3.8-flash** | **CheaperInference** | $0.02211 | $0.3375 | $1.6875 | OpenRouter ($0.04914) | **55.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02008 (\$0.3705 in / \$1.4950 out) · Radar Value 49.8
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.07020 (\$1.3000 in / \$5.2000 out) · Radar Value 49.7
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **OpenRouter → Darkbloom (darkbloom/fp4)** — calidad 8.6/10 · coste/tarea $0.00468 (\$0.1000 in / \$0.2800 out) · Radar Value 82.2
2. **glm-5.3-flash** vía **OpenRouter → Relace (relace/fp4)** — calidad 8.2/10 · coste/tarea $0.00141 (\$0.0285 in / \$0.0923 out) · Radar Value 80.9
3. **minimax-m3.1-flash** vía **CheaperInference** — calidad 7.9/10 · coste/tarea $0.00526 (\$0.0975 in / \$0.3900 out) · Radar Value 75.1
4. **mimo-v2.6-pro** vía **OpenRouter → GMICloud (gmicloud/bf16)** — calidad 8.4/10 · coste/tarea $0.01370 (\$0.3262 in / \$0.6525 out) · Radar Value 74.4
5. **qwen3.8-27b** vía **OpenRouter → Chutes (chutes/fp8)** — calidad 8.0/10 · coste/tarea $0.00867 (\$0.0390 in / \$1.2500 out) · Radar Value 73.9

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-v4.1-flash-1017** vía **OpenRouter → PrimaLabs** — **-73.3%** (ahora \$0.2400 in / \$0.9600 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Wafer (wafer/mxfp4)** — **-58.8%** (ahora \$0.0660 in / \$0.5000 out)
- **deepseek-v4-flash** vía **OpenRouter** — **-52.9%** (ahora \$0.0471 in / \$0.1412 out)
- **deepseek-v4-pro-0813** vía **OpenRouter → Baidu (baidu/fp8)** — **-50.1%** (ahora \$0.6587 in / \$1.9760 out)
- **ling-3.1-flash** vía **OpenRouter** — **-40.0%** (ahora \$0.0450 in / \$0.1350 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Baidu (baidu/fp8)** — **-34.8%** (ahora \$0.0977 in / \$0.3944 out)
- **gpt-oss-120b** vía **OpenRouter** — **-32.0%** (ahora \$0.0170 in / \$0.0630 out)
- **gemma-4-26b-a4b-it** vía **OpenRouter** — **-25.0%** (ahora \$0.0675 in / \$0.2250 out)
- **qwen3.8-27b** vía **OpenRouter → PrimeIntellect (primeintellect/fp8)** — **-25.0%** (ahora \$0.0300 in / \$1.6690 out)
- **glm-5.3-flashx-legal** vía **CheaperInference** — **-23.5%** (ahora \$0.2405 in / \$0.8125 out)
- **gpt-5-codex** vía **CheaperInference** — **-23.5%** (ahora \$0.8125 in / \$6.5000 out)
- **gpt-5-mini-fast** vía **CheaperInference** — **-23.5%** (ahora \$0.2925 in / \$2.3400 out)

### Subidas

- **glm-5.3** vía **OpenRouter → Baidu (baidu/fp8)** — +399.5% (ahora \$1.3986 in / \$4.3956 out)
- **minimax-m3.1-flash** vía **OpenRouter** — +100.0% (ahora \$0.1500 in / \$0.6000 out)
- **minimax-m3.1-flash** vía **OpenRouter → Minimax** — +100.0% (ahora \$0.1500 in / \$0.6000 out)
- **glm-5.3** vía **OpenRouter → Makora (makora/fp4)** — +66.7% (ahora \$0.3000 in / \$3.0000 out)
- **glm-5.3** vía **OpenRouter → Inceptron (inceptron/fp4)** — +59.1% (ahora \$1.0000 in / \$4.9000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → OpenInference (open-inference/fp4)** — +50.0% (ahora \$0.0175 in / \$0.6000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — +50.0% (ahora \$0.0175 in / \$0.6000 out)
- **deepseek-v4-flash-0731** vía **CheaperInference** — +37.7% (ahora \$0.1870 in / \$0.5610 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
