# Daily AI Radar — 2026-10-25

> Generado 25/10/2026 13:12 WET · **724 modelos únicos** · **1349 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **298 endpoints de 35 modelos OpenRouter monitorizados** · **83 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 83 modelos con benchmark propio, 312 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_114 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 460 |
| cheaperinference | `ok` | 313 |
| together | `ok` | 191 |
| novita | `ok` | 97 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 149 |
| openrouter_routes | `ok` | 298 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling** | 5.8/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **CheaperInference** | $0.00382 | $0.0910 | $0.1820 | 8.6/10 | 82.9 |

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
| **qwen3-coder-30b-a3b-instruct** | **OpenRouter** | $0.00412 | $0.0700 | $0.2800 | CheaperInference ($0.01917) | **78.5%** |
| **nemotron-3-super-120b-a12b** | **CheaperInference** | $0.00596 | $0.0975 | $0.4225 | OpenRouter ($0.02564) | **76.8%** |
| **qwen3-coder** | **OpenRouter** | $0.01633 | $0.3000 | $1.0000 | CheaperInference ($0.06389) | **74.4%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **deepseek-v4-pro-0813** | **OpenRouter → Baidu (baidu/fp8)** | $0.00690 | $0.1320 | $0.3960 | OpenRouter → Sail Research (sail-research/us) ($0.01985) | **65.3%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **qwen3-235b-a22b-thinking-2507** | **CheaperInference** | $0.01476 | $0.1495 | $1.4950 | OpenRouter ($0.03779) | **60.9%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05850 | $0.8106 | $4.8638 | OpenRouter ($0.14434) | **59.5%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00586 | $0.0812 | $0.4869 | OpenRouter ($0.01443) | **59.4%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **qwen3.8-27b** | **OpenRouter → Tenstorrent (tenstorrent/fp4)** | $0.00397 | $0.0200 | $0.5000 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **58.5%** |
| **deepseek-v4-pro** | **OpenRouter** | $0.00952 | $0.2088 | $0.4176 | CheaperInference ($0.02241) | **57.5%** |
| **gpt-oss-20b** | **OpenRouter** | $0.00118 | $0.0180 | $0.0900 | CheaperInference ($0.00277) | **57.4%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.07020 (\$1.3000 in / \$5.2000 out) · Radar Value 49.7
3. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02190 (\$0.4039 in / \$1.6299 out) · Radar Value 49.2
4. **o4-mini-high** vía **OpenRouter** — calidad 7.2/10 · coste/tarea $0.05940 (\$1.1000 in / \$4.4000 out) · Radar Value 48.7
5. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.6/10 · coste/tarea $0.00382 (\$0.0910 in / \$0.1820 out) · Radar Value 82.9
2. **glm-5.3-flash** vía **OpenRouter → Relace** — calidad 8.2/10 · coste/tarea $0.00196 (\$0.0513 in / \$0.0701 out) · Radar Value 80.4
3. **qwen3.8-27b** vía **OpenRouter → Tenstorrent (tenstorrent/fp4)** — calidad 8.0/10 · coste/tarea $0.00360 (\$0.0200 in / \$0.5000 out) · Radar Value 77.3
4. **minimax-m3.1-flash** vía **CheaperInference** — calidad 8.0/10 · coste/tarea $0.00547 (\$0.1013 in / \$0.4051 out) · Radar Value 76.0
5. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01516 (\$0.3608 in / \$0.7217 out) · Radar Value 73.6

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-v4.1-flash** vía **OpenRouter → Morph (morph/fp8)** — **-76.9%** (ahora \$0.1050 in / \$0.6000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Wafer (wafer/mxfp4)** — **-54.5%** (ahora \$0.1000 in / \$0.6500 out)
- **kimi-k3** vía **OpenRouter → Morph (morph/fp8)** — **-33.7%** (ahora \$0.9000 in / \$14.9000 out)
- **beam** vía **CheaperInference** — **-32.8%** (ahora \$0.0104 in / \$0.0411 out)
- **gpt-5.6-sol** vía **CheaperInference** — **-28.4%** (ahora \$2.0000 in / \$10.0000 out)
- **deepseek-v4-pro** vía **OpenRouter** — **-27.3%** (ahora \$0.2088 in / \$0.4176 out)
- **glm-5.3-flash** vía **OpenRouter → Wafer (wafer/nvfp4)** — **-27.0%** (ahora \$0.0540 in / \$0.2000 out)
- **kimi-k3.1-pro-highspeed** vía **CheaperInference** — **-25.7%** (ahora \$3.4000 in / \$17.0000 out)
- **kimi-k3.1-pro** vía **CheaperInference** — **-23.5%** (ahora \$1.3000 in / \$6.5000 out)
- **muse-glimmer-30b** vía **CheaperInference** — **-23.5%** (ahora \$0.2275 in / \$0.9750 out)
- **deepseek-v4-pro** vía **CheaperInference** — **-23.5%** (ahora \$0.4290 in / \$1.2870 out)
- **gpt-5.3-codex** vía **CheaperInference** — **-23.5%** (ahora \$1.1375 in / \$9.1000 out)

### Subidas

- **glm-5.3-flash** vía **OpenRouter** — +757.1% (ahora \$0.1500 in / \$0.5000 out)
- **glm-5.3-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — +232.7% (ahora \$0.0665 in / \$0.0698 out)
- **glm-flash** vía **OpenRouter** — +193.1% (ahora \$0.0513 in / \$0.0701 out)
- **ling-3.0-flash** vía **CheaperInference** — +118.5% (ahora \$0.0390 in / \$0.1170 out)
- **kimi** vía **OpenRouter** — +107.8% (ahora \$0.1910 in / \$16.0000 out)
- **glm-5.3-flash** vía **OpenRouter → Reka** — +87.5% (ahora \$0.1500 in / \$2.4000 out)
- **mercury-3** vía **CheaperInference** — +53.8% (ahora \$0.1000 in / \$0.3500 out)
- **glm-5.3** vía **OpenRouter → Morph (morph/fp8)** — +38.2% (ahora \$0.5570 in / \$4.4000 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
