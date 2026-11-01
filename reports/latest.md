# Daily AI Radar — 2026-11-01

> Generado 01/11/2026 15:14 WET · **728 modelos únicos** · **1374 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **334 endpoints de 35 modelos OpenRouter monitorizados** · **82 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 82 modelos con benchmark propio, 326 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_119 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 409 |
| cheaperinference | `ok` | 352 |
| together | `ok` | 191 |
| novita | `ok` | 98 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 151 |
| openrouter_routes | `ok` | 334 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling** | 5.8/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **OpenRouter → Relace (relace/fp4)** | $0.00373 | $0.0870 | $0.1870 | 8.6/10 | 83.0 |

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
| **qwen-mt-plus** | **Novita AI** | $0.01306 | $0.2500 | $0.7500 | CheaperInference ($0.08348) | **84.4%** |
| **mimo-v2.5** | **CheaperInference** | $0.00511 | $0.1120 | $0.2240 | OpenRouter ($0.02621) | **80.5%** |
| **qwen3-coder-30b-a3b-instruct** | **OpenRouter** | $0.00412 | $0.0700 | $0.2800 | CheaperInference ($0.01917) | **78.5%** |
| **nemotron-3-super-120b-a12b** | **CheaperInference** | $0.00596 | $0.0975 | $0.4225 | OpenRouter ($0.02564) | **76.8%** |
| **qwen3-coder** | **OpenRouter** | $0.01633 | $0.3000 | $1.0000 | CheaperInference ($0.06389) | **74.4%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **mistral-nemo** | **OpenRouter** | $0.00114 | $0.0290 | $0.0300 | CheaperInference ($0.00380) | **70.1%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **qwen3.5-9b** | **CheaperInference** | $0.00275 | $0.0650 | $0.0975 | OpenRouter ($0.00715) | **61.6%** |
| **deepseek-v4-pro** | **CheaperInference** | $0.02883 | $0.5519 | $1.6556 | OpenRouter ($0.07294) | **60.5%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **sonar** | **CheaperInference** | $0.01605 | $0.1625 | $1.6250 | OpenRouter ($0.03895) | **58.8%** |
| **qwen3.8-27b** | **OpenRouter → PrimeIntellect (primeintellect/fp8)** | $0.00415 | $0.0100 | $0.5760 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **56.6%** |
| **llama-3.1-8b-instruct** | **Novita AI** | $0.00098 | $0.0200 | $0.0500 | OpenRouter ($0.00215) | **54.4%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02008 (\$0.3705 in / \$1.4950 out) · Radar Value 49.8
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.09180 (\$1.7000 in / \$6.8000 out) · Radar Value 45.7
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **OpenRouter → Relace (relace/fp4)** — calidad 8.6/10 · coste/tarea $0.00373 (\$0.0870 in / \$0.1870 out) · Radar Value 83.0
2. **glm-5.3-flash** vía **OpenRouter** — calidad 8.2/10 · coste/tarea $0.00141 (\$0.0285 in / \$0.0923 out) · Radar Value 80.9
3. **qwen3.8-27b** vía **OpenRouter → PrimeIntellect (primeintellect/fp8)** — calidad 8.0/10 · coste/tarea $0.00376 (\$0.0100 in / \$0.5760 out) · Radar Value 77.2
4. **minimax-m3.1-flash** vía **OpenRouter → Tenstorrent (tenstorrent/fp8)** — calidad 7.9/10 · coste/tarea $0.00270 (\$0.0500 in / \$0.2000 out) · Radar Value 76.9
5. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01543 (\$0.3674 in / \$0.7347 out) · Radar Value 73.4

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-v4.1-flash** vía **OpenRouter → Relace (relace/fp4)** — **-93.3%** (ahora \$0.0009 in / \$0.7294 out)
- **gpt-oss-120b** vía **OpenRouter** — **-86.7%** (ahora \$0.0220 in / \$0.0800 out)
- **minimax-m3.1-flash** vía **OpenRouter** — **-50.0%** (ahora \$0.0750 in / \$0.3000 out)
- **deepseek-v4-pro-0813** vía **OpenRouter** — **-50.0%** (ahora \$0.1150 in / \$4.0000 out)
- **minimax-m3.1-flash** vía **OpenRouter → Minimax** — **-50.0%** (ahora \$0.0750 in / \$0.3000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Particle AI (particle-ai)** — **-50.0%** (ahora \$0.0500 in / \$0.5000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → InferenceNet (inference-net/us)** — **-40.8%** (ahora \$0.1030 in / \$0.6000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → InferenceNet (inference-net/fp8)** — **-40.8%** (ahora \$0.1030 in / \$0.6000 out)
- **glm-5.3-flash** vía **OpenRouter → Sail Research (sail-research/fp4)** — **-37.5%** (ahora \$0.3500 in / \$1.2500 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Baidu (baidu/fp8)** — **-34.8%** (ahora \$0.0977 in / \$0.3944 out)
- **glm-5.3-flash** vía **OpenRouter → Particle AI (particle-ai/nvfp4)** — **-33.3%** (ahora \$0.1000 in / \$0.5000 out)
- **glm-4.5** vía **CheaperInference** — **-32.3%** (ahora \$0.3300 in / \$1.2100 out)

### Subidas

- **deepseek-v4.1-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — +396.9% (ahora \$0.0009 in / \$0.7155 out)
- **glm-5.3-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — +350.7% (ahora \$0.0300 in / \$0.1600 out)
- **qwen3.8-27b** vía **OpenRouter** — +275.0% (ahora \$0.1500 in / \$1.8750 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter** — +247.2% (ahora \$0.0350 in / \$0.5000 out)
- **deepseek-flash** vía **OpenRouter** — +247.2% (ahora \$0.0350 in / \$0.5000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → OpenInference (open-inference/fp4)** — +247.2% (ahora \$0.0350 in / \$0.5000 out)
- **glm-5.3** vía **OpenRouter** — +157.1% (ahora \$0.0800 in / \$3.6000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Morph (morph/fp8)** — +127.3% (ahora \$0.0500 in / \$0.1920 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
