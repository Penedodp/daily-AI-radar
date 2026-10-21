# Daily AI Radar — 2026-10-21

> Generado 21/10/2026 13:57 WEST · **664 modelos únicos** · **1237 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **281 endpoints de 35 modelos OpenRouter monitorizados** · **79 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 79 modelos con benchmark propio, 280 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_113 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 461 |
| cheaperinference | `ok` | 217 |
| together | `ok` | 191 |
| novita | `ok` | 96 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 147 |
| openrouter_routes | `ok` | 281 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling** | 5.8/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **OpenRouter → Relace (relace/mxfp4)** | $0.00444 | $0.1000 | $0.2400 | 8.5/10 | 81.5 |

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
| **qwen3-coder-30b-a3b-instruct** | **OpenRouter** | $0.00412 | $0.0700 | $0.2800 | CheaperInference ($0.01917) | **78.5%** |
| **qwen3-coder** | **OpenRouter** | $0.01633 | $0.3000 | $1.0000 | CheaperInference ($0.06389) | **74.4%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **mistral-nemo** | **OpenRouter** | $0.00114 | $0.0290 | $0.0300 | CheaperInference ($0.00380) | **70.1%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **deepseek-v4-pro-0813** | **OpenRouter → Baidu (baidu/fp8)** | $0.01172 | $0.2244 | $0.6732 | CheaperInference ($0.02930) | **60.0%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00594 | $0.0822 | $0.4935 | OpenRouter ($0.01443) | **58.9%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **gpt-oss-20b** | **OpenRouter** | $0.00118 | $0.0180 | $0.0900 | CheaperInference ($0.00277) | **57.4%** |
| **qwen3-235b-a22b-thinking-2507** | **CheaperInference** | $0.01681 | $0.1702 | $1.7022 | OpenRouter ($0.03779) | **55.5%** |
| **llama-4-scout-17b-16e-instruct** | **CheaperInference** | $0.00444 | $0.0850 | $0.2550 | Together AI ($0.00974) | **54.4%** |
| **ling-3.0-flash-fin** | **CheaperInference** | $0.00185 | $0.0357 | $0.1046 | Novita AI ($0.00388) | **52.4%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.07020 (\$1.3000 in / \$5.2000 out) · Radar Value 49.7
3. **o4-mini-high** vía **OpenRouter** — calidad 7.2/10 · coste/tarea $0.05940 (\$1.1000 in / \$4.4000 out) · Radar Value 48.7
4. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02627 (\$0.4845 in / \$1.9550 out) · Radar Value 47.8
5. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04787 (\$0.8864 in / \$3.5458 out) · Radar Value 40.7

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **OpenRouter → Relace (relace/mxfp4)** — calidad 8.5/10 · coste/tarea $0.00444 (\$0.1000 in / \$0.2400 out) · Radar Value 81.5
2. **glm-5.3-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — calidad 8.2/10 · coste/tarea $0.00227 (\$0.0517 in / \$0.1200 out) · Radar Value 80.2
3. **qwen3.8-27b** vía **OpenRouter → Chutes (chutes/fp8)** — calidad 8.0/10 · coste/tarea $0.00867 (\$0.0390 in / \$1.2500 out) · Radar Value 73.9
4. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01519 (\$0.3617 in / \$0.7234 out) · Radar Value 73.6
5. **glm-5.3-flashx** vía **OpenRouter** — calidad 8.2/10 · coste/tarea $0.01860 (\$0.3700 in / \$1.2500 out) · Radar Value 70.0

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-pro** vía **OpenRouter** — **-91.6%** (ahora \$0.2244 in / \$0.6732 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Baidu (baidu/fp8)** — **-83.7%** (ahora \$0.0489 in / \$0.1956 out)
- **beam-1.0-501b-a23b** vía **OpenRouter → BaseTen (baseten/fp4)** — **-72.1%** (ahora \$0.4000 in / \$1.2000 out)
- **glm-5.3-flash** vía **OpenRouter → Relace** — **-68.0%** (ahora \$0.0750 in / \$0.1600 out)
- **glm-5.3-flash** vía **OpenRouter → Sail Research (sail-research/us)** — **-50.0%** (ahora \$0.0900 in / \$0.1500 out)
- **glm-5.3-flash** vía **OpenRouter → Sail Research (sail-research/fp4)** — **-50.0%** (ahora \$0.0900 in / \$0.1500 out)
- **kimi-k3** vía **OpenRouter → Sail Research (sail-research/fp4/us)** — **-38.9%** (ahora \$1.2000 in / \$5.5000 out)
- **glm-4.5-air** vía **CheaperInference** — **-35.3%** (ahora \$0.1100 in / \$0.6050 out)
- **deepseek-flash** vía **OpenRouter** — **-30.0%** (ahora \$0.0490 in / \$0.3750 out)
- **mimo-v2.5-pro** vía **OpenRouter** — **-30.0%** (ahora \$0.3045 in / \$0.6090 out)
- **aion-3.0** vía **CheaperInference** — **-27.7%** (ahora \$1.6500 in / \$3.3000 out)
- **glm-flash** vía **OpenRouter** — **-25.0%** (ahora \$0.0517 in / \$0.1200 out)

### Subidas

- **glm-5.3-flash** vía **OpenRouter → Morph (morph/fp8)** — +472.9% (ahora \$0.8250 in / \$0.6500 out)
- **kimi-k3** vía **OpenRouter → Relace (relace/fp4)** — +300.0% (ahora \$0.3000 in / \$12.0000 out)
- **deepseek-v4-flash** vía **OpenRouter** — +293.2% (ahora \$0.0475 in / \$0.1568 out)
- **mimo-v2.6-flash** vía **OpenRouter → Relace (relace/mxfp4)** — +233.3% (ahora \$0.1000 in / \$0.2400 out)
- **glm-5.3-flash** vía **OpenRouter** — +218.6% (ahora \$0.1500 in / \$0.5000 out)
- **deepseek-v4-flash-0731** vía **OpenRouter → Relace (relace/fp4)** — +214.6% (ahora \$0.0475 in / \$0.1568 out)
- **deepseek-v4.1-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — +212.5% (ahora \$0.0490 in / \$0.3750 out)
- **glm-5.3-flash** vía **OpenRouter → NextBit (nextbit/fp4)** — +200.0% (ahora \$0.2000 in / \$1.2000 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
