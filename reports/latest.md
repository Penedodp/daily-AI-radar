# Daily AI Radar — 2026-11-10

> Generado 10/11/2026 16:27 WET · **750 modelos únicos** · **1357 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **297 endpoints de 35 modelos OpenRouter monitorizados** · **81 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 81 modelos con benchmark propio, 316 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_119 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 423 |
| cheaperinference | `ok` | 354 |
| together | `ok` | 192 |
| novita | `ok` | 99 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `cached_stale` | 152 |
| openrouter_routes | `ok` | 297 |

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
| **qwen-mt-plus** | **Novita AI** | $0.01306 | $0.2500 | $0.7500 | CheaperInference ($0.08348) | **84.4%** |
| **mimo-v2.5** | **CheaperInference** | $0.00415 | $0.0910 | $0.1820 | OpenRouter ($0.02621) | **84.2%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02765) | **74.6%** |
| **qwen3-coder** | **OpenRouter** | $0.01633 | $0.3000 | $1.0000 | CheaperInference ($0.06389) | **74.4%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **glm-5.3** | **OpenRouter** | $0.01156 | $0.0699 | $1.4000 | CheaperInference ($0.04095) | **71.8%** |
| **mistral-nemo** | **OpenRouter** | $0.00114 | $0.0290 | $0.0300 | CheaperInference ($0.00380) | **70.1%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **deepseek-v4-flash-vision-exp** | **CheaperInference** | $0.00777 | $0.1320 | $0.5280 | OpenRouter ($0.02298) | **66.2%** |
| **ling-3.0-flash-fin** | **CheaperInference** | $0.00141 | $0.0273 | $0.0799 | Novita AI ($0.00388) | **63.6%** |
| **ling-3.0-flash-sante** | **CheaperInference** | $0.00141 | $0.0273 | $0.0799 | Novita AI ($0.00388) | **63.6%** |
| **qwen3.8-27b** | **OpenRouter → PrimeIntellect (primeintellect/fp8)** | $0.00364 | $0.0460 | $0.3250 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **61.9%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05888 | $0.8158 | $4.8949 | OpenRouter ($0.14434) | **59.2%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **particle-1** | **OpenRouter** | $0.00494 | $0.0500 | $0.5000 | CheaperInference ($0.01192) | **58.6%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02493 (\$0.4598 in / \$1.8555 out) · Radar Value 48.2
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.09180 (\$1.7000 in / \$6.8000 out) · Radar Value 45.7
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **OpenRouter → Darkbloom (darkbloom/fp4)** — calidad 8.6/10 · coste/tarea $0.00468 (\$0.1000 in / \$0.2800 out) · Radar Value 82.2
2. **glm-5.3-flash** vía **OpenRouter** — calidad 8.2/10 · coste/tarea $0.00167 (\$0.0399 in / \$0.0784 out) · Radar Value 80.7
3. **qwen3.8-27b** vía **OpenRouter → PrimeIntellect (primeintellect/fp8)** — calidad 8.0/10 · coste/tarea $0.00333 (\$0.0460 in / \$0.3250 out) · Radar Value 77.5
4. **minimax-m3.1-flash** vía **OpenRouter** — calidad 7.9/10 · coste/tarea $0.00405 (\$0.0750 in / \$0.3000 out) · Radar Value 76.0
5. **mimo-v2.6-pro** vía **OpenRouter → GMICloud (gmicloud/bf16)** — calidad 8.4/10 · coste/tarea $0.01370 (\$0.3262 in / \$0.6525 out) · Radar Value 74.4

## 🔥 Bajadas reales de precio (vs ayer)

- **ming-image-0.1-design-layer** vía **Novita AI** — **-100.0%** (ahora \$0.0000 in / \$2.0000 out)
- **ming-image-0.1-design** vía **Novita AI** — **-100.0%** (ahora \$0.0000 in / \$2.0000 out)
- **deepseek-v4-flash-0731** vía **OpenRouter → Baidu (baidu/fp8)** — **-86.4%** (ahora \$0.0598 in / \$0.1795 out)
- **glm-5.3-flash** vía **OpenRouter** — **-84.3%** (ahora \$0.0399 in / \$0.0784 out)
- **gemma-4-26b-a4b-it** vía **OpenRouter** — **-66.7%** (ahora \$0.0800 in / \$0.1000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Baidu (baidu/fp8)** — **-53.4%** (ahora \$0.1398 in / \$0.5592 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Baidu (baidu/fp8)** — **-46.5%** (ahora \$0.1498 in / \$0.6046 out)
- **qwen3.8-27b** vía **OpenRouter → PrimeIntellect (primeintellect/fp8)** — **-37.3%** (ahora \$0.0460 in / \$0.3250 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Wafer (wafer/mxfp4)** — **-36.4%** (ahora \$0.0700 in / \$0.5000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Reka** — **-33.3%** (ahora \$0.1200 in / \$0.6400 out)
- **deepseek-v4-flash** vía **CheaperInference** — **-29.4%** (ahora \$0.0900 in / \$0.3600 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Cohere (cohere/fp8)** — **-24.2%** (ahora \$0.1500 in / \$0.5000 out)

### Subidas

- **deepseek-v4.1-flash** vía **OpenRouter** — +488.2% (ahora \$0.3000 in / \$1.2000 out)
- **kimi-k3** vía **OpenRouter → Makora (makora/fp4)** — +300.0% (ahora \$1.2000 in / \$15.0000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → OpenInference (open-inference/fp4)** — +108.3% (ahora \$0.0500 in / \$0.8000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — +108.3% (ahora \$0.0500 in / \$0.8000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Mancer 2 (mancer/fp8)** — +60.0% (ahora \$0.2000 in / \$0.7500 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Alibaba** — +40.0% (ahora \$0.1050 in / \$0.4200 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Alibaba** — +40.0% (ahora \$0.1050 in / \$0.4200 out)
- **deepseek-v4-flash-0731** vía **CheaperInference** — +31.3% (ahora \$0.1743 in / \$0.5229 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
