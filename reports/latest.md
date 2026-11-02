# Daily AI Radar — 2026-11-02

> Generado 02/11/2026 18:26 WET · **726 modelos únicos** · **1375 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **338 endpoints de 35 modelos OpenRouter monitorizados** · **81 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 81 modelos con benchmark propio, 324 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_119 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 408 |
| cheaperinference | `ok` | 351 |
| together | `ok` | 191 |
| novita | `ok` | 98 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 151 |
| openrouter_routes | `ok` | 338 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling** | 5.8/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **OpenRouter → Io Net (io-net/fp8)** | $0.00468 | $0.1000 | $0.2800 | 8.6/10 | 82.2 |

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
| **qwen3.8-27b** | **OpenRouter → PrimeIntellect (primeintellect/fp8)** | $0.00159 | $0.0040 | $0.2200 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **83.4%** |
| **mimo-v2.5** | **CheaperInference** | $0.00543 | $0.1190 | $0.2380 | OpenRouter ($0.02621) | **79.3%** |
| **qwen3-coder-30b-a3b-instruct** | **OpenRouter** | $0.00412 | $0.0700 | $0.2800 | CheaperInference ($0.01917) | **78.5%** |
| **nemotron-3-super-120b-a12b** | **CheaperInference** | $0.00596 | $0.0975 | $0.4225 | OpenRouter ($0.02564) | **76.8%** |
| **qwen3-coder** | **OpenRouter** | $0.01633 | $0.3000 | $1.0000 | CheaperInference ($0.06389) | **74.4%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **mistral-nemo** | **OpenRouter** | $0.00114 | $0.0290 | $0.0300 | CheaperInference ($0.00380) | **70.1%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **deepseek-v4-pro** | **CheaperInference** | $0.02241 | $0.4290 | $1.2870 | OpenRouter ($0.07294) | **69.3%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **qwen3.5-9b** | **CheaperInference** | $0.00275 | $0.0650 | $0.0975 | OpenRouter ($0.00715) | **61.6%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **llama-3.1-8b-instruct** | **Novita AI** | $0.00098 | $0.0200 | $0.0500 | OpenRouter ($0.00215) | **54.4%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02472 (\$0.4560 in / \$1.8400 out) · Radar Value 48.3
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.09180 (\$1.7000 in / \$6.8000 out) · Radar Value 45.7
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **OpenRouter → Io Net (io-net/fp8)** — calidad 8.6/10 · coste/tarea $0.00468 (\$0.1000 in / \$0.2800 out) · Radar Value 82.2
2. **glm-5.3-flash** vía **OpenRouter** — calidad 8.2/10 · coste/tarea $0.00141 (\$0.0285 in / \$0.0923 out) · Radar Value 80.9
3. **qwen3.8-27b** vía **OpenRouter → PrimeIntellect (primeintellect/fp8)** — calidad 8.0/10 · coste/tarea $0.00144 (\$0.0040 in / \$0.2200 out) · Radar Value 78.9
4. **minimax-m3.1-flash** vía **OpenRouter → Tenstorrent (tenstorrent/fp8)** — calidad 7.9/10 · coste/tarea $0.00270 (\$0.0500 in / \$0.2000 out) · Radar Value 76.9
5. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01543 (\$0.3674 in / \$0.7347 out) · Radar Value 73.4

## 🔥 Bajadas reales de precio (vs ayer)

- **beam** vía **CheaperInference** — **-100.0%** (ahora \$0.0000 in / \$0.0002 out)
- **qwen3.8-27b** vía **OpenRouter → PrimeIntellect (primeintellect/fp8)** — **-61.8%** (ahora \$0.0040 in / \$0.2200 out)
- **glm-5.3** vía **OpenRouter → Io Net (io-net/fp8)** — **-54.5%** (ahora \$0.1500 in / \$2.6000 out)
- **glm-5.3** vía **OpenRouter → PrimeIntellect** — **-49.0%** (ahora \$0.5000 in / \$3.0800 out)
- **glm-5.3-flash** vía **OpenRouter → Makora** — **-48.9%** (ahora \$0.1400 in / \$0.2400 out)
- **hy3** vía **OpenRouter** — **-37.5%** (ahora \$0.0825 in / \$0.3300 out)
- **hy3** vía **OpenRouter → Tencent (tencent/fp8)** — **-37.5%** (ahora \$0.0825 in / \$0.3300 out)
- **gpt-oss-20b** vía **CheaperInference** — **-36.7%** (ahora \$0.0325 in / \$0.1235 out)
- **kimi-k3** vía **OpenRouter → Wafer (wafer/us)** — **-31.4%** (ahora \$0.2760 in / \$9.6000 out)
- **gpt-5.6-terra** vía **CheaperInference** — **-26.2%** (ahora \$0.8000 in / \$4.8000 out)
- **apex** vía **CheaperInference** — **-23.5%** (ahora \$0.3250 in / \$1.9500 out)
- **gpt-4o-mini-fast** vía **CheaperInference** — **-23.5%** (ahora \$0.1625 in / \$0.6500 out)

### Subidas

- **deepseek-v4.1-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — +3788.9% (ahora \$0.0350 in / \$0.5000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Relace (relace/fp4)** — +3788.9% (ahora \$0.0350 in / \$0.5000 out)
- **gpt-oss-120b** vía **OpenRouter** — +650.0% (ahora \$0.1500 in / \$0.6000 out)
- **deepseek-v4-pro-0813** vía **OpenRouter → Baidu (baidu/fp8)** — +365.1% (ahora \$1.3200 in / \$3.9600 out)
- **qwen3.8-27b** vía **OpenRouter → Reka (reka/fp8)** — +275.0% (ahora \$0.1500 in / \$2.5000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Wafer (wafer/mxfp4)** — +97.0% (ahora \$0.1300 in / \$0.5000 out)
- **glm-4.7** vía **CheaperInference** — +88.6% (ahora \$0.6050 in / \$2.2825 out)
- **gemma-4-31b-it** vía **CheaperInference** — +87.5% (ahora \$0.1625 in / \$0.4875 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
