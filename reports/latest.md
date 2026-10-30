# Daily AI Radar — 2026-10-30

> Generado 30/10/2026 15:04 WET · **755 modelos únicos** · **1412 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **324 endpoints de 35 modelos OpenRouter monitorizados** · **83 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 83 modelos con benchmark propio, 312 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_120 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 413 |
| cheaperinference | `ok` | 396 |
| together | `ok` | 191 |
| novita | `ok` | 98 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 151 |
| openrouter_routes | `ok` | 324 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling** | 5.8/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **OpenRouter → Relace (relace/mxfp4)** | $0.00373 | $0.0870 | $0.1870 | 8.6/10 | 83.0 |

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
| **gpt-5.6-sol-pro** | **CheaperInference** | $0.08518 | $1.3000 | $6.5000 | OpenRouter ($0.26210) | **67.5%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **qwen3.5-9b** | **CheaperInference** | $0.00275 | $0.0650 | $0.0975 | OpenRouter ($0.00715) | **61.6%** |
| **qwen3-235b-a22b-thinking-2507** | **CheaperInference** | $0.01476 | $0.1495 | $1.4950 | OpenRouter ($0.03779) | **60.9%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **sonar** | **CheaperInference** | $0.01605 | $0.1625 | $1.6250 | OpenRouter ($0.03895) | **58.8%** |
| **gpt-oss-20b** | **OpenRouter** | $0.00118 | $0.0180 | $0.0900 | CheaperInference ($0.00277) | **57.4%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02008 (\$0.3705 in / \$1.4950 out) · Radar Value 49.8
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.07020 (\$1.3000 in / \$5.2000 out) · Radar Value 49.7
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **OpenRouter → Relace (relace/mxfp4)** — calidad 8.6/10 · coste/tarea $0.00373 (\$0.0870 in / \$0.1870 out) · Radar Value 83.0
2. **glm-5.3-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — calidad 8.2/10 · coste/tarea $0.00094 (\$0.0189 in / \$0.0625 out) · Radar Value 81.2
3. **minimax-m3.1-flash** vía **OpenRouter → SambaNova** — calidad 7.9/10 · coste/tarea $0.00324 (\$0.0600 in / \$0.2400 out) · Radar Value 76.6
4. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01188 (\$0.2829 in / \$0.5658 out) · Radar Value 75.5
5. **qwen3.8-27b** vía **OpenRouter → Chutes (chutes/fp8)** — calidad 8.0/10 · coste/tarea $0.00867 (\$0.0390 in / \$1.2500 out) · Radar Value 73.9

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-v4.1-flash-1017** vía **OpenRouter** — **-89.3%** (ahora \$0.0220 in / \$0.1920 out)
- **deepseek-flash** vía **OpenRouter** — **-89.3%** (ahora \$0.0220 in / \$0.1920 out)
- **glm-5.3-flash** vía **OpenRouter → Morph (morph/fp8)** — **-69.6%** (ahora \$0.0420 in / \$0.3000 out)
- **kimi-k3** vía **OpenRouter → Wafer (wafer/fast)** — **-66.0%** (ahora \$0.1700 in / \$22.0000 out)
- **glm-5.3-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — **-60.7%** (ahora \$0.0189 in / \$0.0625 out)
- **particle-1** vía **OpenRouter** — **-60.0%** (ahora \$0.1000 in / \$1.0000 out)
- **minimax-m3.1-flash** vía **OpenRouter → SambaNova** — **-60.0%** (ahora \$0.0600 in / \$0.2400 out)
- **minimax-m3.1-flash** vía **OpenRouter** — **-50.0%** (ahora \$0.0750 in / \$0.3000 out)
- **deepseek-pro** vía **OpenRouter** — **-50.0%** (ahora \$0.1035 in / \$4.0000 out)
- **deepseek-v4-pro-0813** vía **OpenRouter** — **-50.0%** (ahora \$0.1035 in / \$4.0000 out)
- **minimax-m3.1-flash** vía **OpenRouter → Minimax** — **-50.0%** (ahora \$0.0750 in / \$0.3000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Morph (morph/fp8)** — **-50.0%** (ahora \$0.0220 in / \$0.1920 out)

### Subidas

- **deepseek-v4.1-flash** vía **OpenRouter → Baidu (baidu/fp8)** — +571.1% (ahora \$0.3000 in / \$1.2000 out)
- **qwen3.8-27b** vía **OpenRouter** — +284.6% (ahora \$0.1500 in / \$1.8750 out)
- **glm-5.3** vía **OpenRouter** — +157.1% (ahora \$0.0800 in / \$3.6000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — +154.7% (ahora \$0.0433 in / \$1.0400 out)
- **deepseek-v4-flash** vía **OpenRouter** — +101.7% (ahora \$0.0486 in / \$0.3000 out)
- **glm-flash** vía **OpenRouter** — +88.9% (ahora \$0.0180 in / \$0.1402 out)
- **glm-5.3-flash** vía **OpenRouter** — +88.9% (ahora \$0.0180 in / \$0.1402 out)
- **glm-5.3-flash** vía **OpenRouter → Relace** — +88.9% (ahora \$0.0180 in / \$0.1402 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
