# Daily AI Radar — 2026-11-05

> Generado 05/11/2026 16:30 WET · **730 modelos únicos** · **1393 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **353 endpoints de 35 modelos OpenRouter monitorizados** · **81 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 81 modelos con benchmark propio, 331 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_119 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 408 |
| cheaperinference | `ok` | 350 |
| together | `ok` | 192 |
| novita | `ok` | 100 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 151 |
| openrouter_routes | `ok` | 353 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| — | — | Ningún modelo gratuito puntuado todavía | — | — | — | — |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **CheaperInference** | $0.00441 | $0.1050 | $0.2100 | 8.6/10 | 82.4 |

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
| **mimo-v2.5** | **CheaperInference** | $0.00543 | $0.1190 | $0.2380 | OpenRouter ($0.02621) | **79.3%** |
| **nemotron-3-super-120b-a12b** | **CheaperInference** | $0.00596 | $0.0975 | $0.4225 | OpenRouter ($0.02564) | **76.8%** |
| **gemma-4-26b-a4b-it** | **OpenRouter** | $0.00136 | $0.0260 | $0.0790 | CheaperInference ($0.00574) | **76.2%** |
| **qwen3-coder** | **OpenRouter** | $0.01633 | $0.3000 | $1.0000 | CheaperInference ($0.06389) | **74.4%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02431) | **71.1%** |
| **mistral-nemo** | **OpenRouter** | $0.00114 | $0.0290 | $0.0300 | CheaperInference ($0.00380) | **70.1%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **ling-3.0-flash-fin** | **CheaperInference** | $0.00141 | $0.0273 | $0.0799 | Novita AI ($0.00388) | **63.6%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **deepseek-v4-pro** | **CheaperInference** | $0.02930 | $0.5610 | $1.6830 | OpenRouter ($0.07294) | **59.8%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **sonar** | **CheaperInference** | $0.01605 | $0.1625 | $1.6250 | OpenRouter ($0.03895) | **58.8%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02456 (\$0.4531 in / \$1.8283 out) · Radar Value 48.3
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.09180 (\$1.7000 in / \$6.8000 out) · Radar Value 45.7
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.6/10 · coste/tarea $0.00441 (\$0.1050 in / \$0.2100 out) · Radar Value 82.4
2. **glm-5.3-flash** vía **OpenRouter → Relace (relace/fp4)** — calidad 8.2/10 · coste/tarea $0.00141 (\$0.0285 in / \$0.0923 out) · Radar Value 80.9
3. **minimax-m3.1-flash** vía **OpenRouter** — calidad 7.9/10 · coste/tarea $0.00405 (\$0.0750 in / \$0.3000 out) · Radar Value 76.0
4. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01370 (\$0.3262 in / \$0.6525 out) · Radar Value 74.4
5. **qwen3.8-27b** vía **OpenRouter → Chutes (chutes/fp8)** — calidad 8.0/10 · coste/tarea $0.00867 (\$0.0390 in / \$1.2500 out) · Radar Value 73.9

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-v4.1-flash-1017** vía **OpenRouter → Relace (relace/fp4)** — **-82.9%** (ahora \$0.0060 in / \$0.5000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Relace (relace/fp4)** — **-82.9%** (ahora \$0.0060 in / \$0.5000 out)
- **gemma-4-26b-a4b-it** vía **OpenRouter** — **-74.0%** (ahora \$0.0260 in / \$0.0790 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter** — **-72.7%** (ahora \$0.0060 in / \$0.5000 out)
- **deepseek-flash** vía **OpenRouter** — **-72.7%** (ahora \$0.0060 in / \$0.5000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — **-71.4%** (ahora \$0.0100 in / \$0.5000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → OpenInference (open-inference/fp4)** — **-70.0%** (ahora \$0.0100 in / \$0.5000 out)
- **beam** vía **CheaperInference** — **-69.0%** (ahora \$0.0026 in / \$0.0102 out)
- **glm-5.3** vía **OpenRouter** — **-61.1%** (ahora \$0.0699 in / \$1.4000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Particle AI (particle-ai/us)** — **-56.1%** (ahora \$0.0219 in / \$0.2195 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → SiliconFlow (siliconflow/fp8)** — **-54.2%** (ahora \$0.3000 in / \$0.5500 out)
- **hy4** vía **Novita AI** — **-50.0%** (ahora \$0.4170 in / \$1.2505 out)

### Subidas

- **gpt-oss-120b** vía **OpenRouter** — +589.7% (ahora \$0.1500 in / \$0.6000 out)
- **llama-3.3-70b-instruct** vía **OpenRouter** — +490.0% (ahora \$0.5900 in / \$0.7900 out)
- **glm-5.3-flash** vía **OpenRouter** — +457.6% (ahora \$0.1500 in / \$0.5000 out)
- **glm-5.3** vía **OpenRouter → Morph (morph/fp8)** — +259.2% (ahora \$0.7400 in / \$3.0000 out)
- **deepseek-v4.1-flash:batch** vía **OpenRouter** — +124.0% (ahora \$0.1120 in / \$0.3360 out)
- **llama-4-maverick** vía **OpenRouter** — +86.7% (ahora \$0.3500 in / \$1.0000 out)
- **deepseek-v4-pro-0813** vía **CheaperInference** — +42.5% (ahora \$0.5610 in / \$1.6830 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Baidu (baidu/fp8)** — +40.6% (ahora \$0.0447 in / \$0.1788 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
