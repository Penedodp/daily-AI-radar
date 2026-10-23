# Daily AI Radar — 2026-10-23

> Generado 23/10/2026 13:39 WEST · **673 modelos únicos** · **1254 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **279 endpoints de 35 modelos OpenRouter monitorizados** · **81 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 81 modelos con benchmark propio, 313 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_114 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 461 |
| cheaperinference | `ok` | 236 |
| together | `ok` | 192 |
| novita | `ok` | 95 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 148 |
| openrouter_routes | `ok` | 279 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling** | 5.8/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **CheaperInference** | $0.00472 | $0.1123 | $0.2246 | 8.5/10 | 81.3 |

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
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **qwen3-235b-a22b-thinking-2507** | **CheaperInference** | $0.01476 | $0.1495 | $1.4950 | OpenRouter ($0.03779) | **60.9%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **qwen3.8-27b** | **OpenRouter → Tenstorrent (tenstorrent/fp4)** | $0.00397 | $0.0200 | $0.5000 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **58.5%** |
| **gpt-oss-20b** | **OpenRouter** | $0.00118 | $0.0180 | $0.0900 | CheaperInference ($0.00277) | **57.4%** |
| **llama-3.1-8b-instruct** | **Novita AI** | $0.00098 | $0.0200 | $0.0500 | OpenRouter ($0.00215) | **54.4%** |
| **ling-3.0-flash-fin** | **CheaperInference** | $0.00185 | $0.0357 | $0.1046 | Novita AI ($0.00388) | **52.4%** |
| **ling-3.0-flash-sante** | **CheaperInference** | $0.00185 | $0.0357 | $0.1046 | Novita AI ($0.00388) | **52.4%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.07020 (\$1.3000 in / \$5.2000 out) · Radar Value 49.7
3. **o4-mini-high** vía **OpenRouter** — calidad 7.2/10 · coste/tarea $0.05940 (\$1.1000 in / \$4.4000 out) · Radar Value 48.7
4. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02627 (\$0.4845 in / \$1.9550 out) · Radar Value 47.8
5. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.5/10 · coste/tarea $0.00472 (\$0.1123 in / \$0.2246 out) · Radar Value 81.3
2. **glm-5.3-flash** vía **OpenRouter** — calidad 8.2/10 · coste/tarea $0.00135 (\$0.0052 in / \$0.1985 out) · Radar Value 80.9
3. **qwen3.8-27b** vía **OpenRouter → Tenstorrent (tenstorrent/fp4)** — calidad 8.0/10 · coste/tarea $0.00360 (\$0.0200 in / \$0.5000 out) · Radar Value 77.3
4. **minimax-m3.1-flash** vía **OpenRouter → InferenceNet (inference-net/fp4)** — calidad 8.0/10 · coste/tarea $0.00630 (\$0.1000 in / \$0.5500 out) · Radar Value 75.4
5. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01518 (\$0.3615 in / \$0.7230 out) · Radar Value 73.6

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-pro** vía **OpenRouter** — **-90.4%** (ahora \$0.2561 in / \$0.7682 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Morph (morph/fp8)** — **-77.8%** (ahora \$0.0600 in / \$0.6000 out)
- **kimi-k3** vía **OpenRouter → InferenceNet (inference-net/fast)** — **-75.5%** (ahora \$0.5000 in / \$11.8800 out)
- **kimi** vía **OpenRouter** — **-33.3%** (ahora \$0.2380 in / \$16.0000 out)
- **mimo-v2.6-flash** vía **OpenRouter → Io Net (io-net/fp8)** — **-33.3%** (ahora \$0.1000 in / \$0.2800 out)
- **glm-5.3-flash** vía **OpenRouter → NextBit (nextbit/fp4)** — **-33.3%** (ahora \$0.1250 in / \$0.5000 out)
- **kimi-k3** vía **OpenRouter → Wafer** — **-33.3%** (ahora \$0.2380 in / \$16.0000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → DigitalOcean** — **-26.7%** (ahora \$0.1650 in / \$0.6600 out)
- **minimax-m3.1-flash** vía **CheaperInference** — **-25.8%** (ahora \$0.1275 in / \$0.5100 out)
- **grok-4.6** vía **CheaperInference** — **-23.5%** (ahora \$1.3000 in / \$3.9000 out)
- **qwen3.7-flash** vía **CheaperInference** — **-22.3%** (ahora \$0.0195 in / \$0.0845 out)
- **glm-5.3** vía **OpenRouter → Morph (morph/fp8)** — **-20.3%** (ahora \$0.1850 in / \$4.4000 out)

### Subidas

- **qwen3.8-27b** vía **OpenRouter** — +400.0% (ahora \$0.2000 in / \$2.5000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Baidu (baidu/fp8)** — +329.2% (ahora \$0.3000 in / \$1.2000 out)
- **deepseek-v4-pro** vía **OpenRouter** — +114.1% (ahora \$0.9553 in / \$1.9105 out)
- **qwen3.5-9b** vía **OpenRouter** — +112.5% (ahora \$0.1700 in / \$0.2500 out)
- **glm-5.3-flash** vía **OpenRouter → Reka** — +50.0% (ahora \$0.0800 in / \$2.4000 out)
- **glm-4.7** vía **CheaperInference** — +42.6% (ahora \$0.4707 in / \$1.7260 out)
- **glm-5.3** vía **OpenRouter → DekaLLM** — +38.9% (ahora \$0.2500 in / \$2.9500 out)
- **gpt-5.6-luna** vía **CheaperInference** — +31.7% (ahora \$0.1054 in / \$0.6324 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
