# Daily AI Radar — 2026-10-13

> Generado 13/10/2026 16:05 WEST · **611 modelos únicos** · **1107 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **298 endpoints de 35 modelos OpenRouter monitorizados** · **73 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 73 modelos con benchmark propio, 251 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_9 ruta(s) duplicada(s) exacta(s) detectada(s) y eliminada(s) antes de publicar._

_115 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 454 |
| cheaperinference | `ok` | 91 |
| together | `ok` | 187 |
| novita | `ok` | 95 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 140 |
| openrouter_routes | `ok` | 298 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling** | 5.8/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **OpenRouter** | $0.02790 | $0.5000 | $2.1500 | 7.1/10 | 56.9 |
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
| **qwen3-coder-30b-a3b-instruct** | **OpenRouter** | $0.00412 | $0.0700 | $0.2800 | CheaperInference ($0.01917) | **78.5%** |
| **ling-3.0-flash-vl** | **OpenRouter** | $0.00109 | $0.0210 | $0.0616 | Novita AI ($0.00388) | **72.0%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02431) | **71.1%** |
| **ling-3.0-flash** | **OpenRouter** | $0.00110 | $0.0210 | $0.0630 | Novita AI ($0.00313) | **65.0%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00577 | $0.0800 | $0.4800 | OpenRouter ($0.01443) | **60.0%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **gpt-oss-20b** | **OpenRouter** | $0.00118 | $0.0180 | $0.0900 | Together AI ($0.00294) | **59.9%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **qwen3.8-27b** | **OpenRouter → Tenstorrent (tenstorrent/fp4)** | $0.00397 | $0.0200 | $0.5000 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **58.5%** |
| **llama-3.1-8b-instruct** | **Novita AI** | $0.00098 | $0.0200 | $0.0500 | OpenRouter ($0.00215) | **54.4%** |
| **kimi-k2-thinking** | **CheaperInference** | $0.01851 | $0.3055 | $1.3000 | OpenRouter ($0.03599) | **48.6%** |
| **qwen3.6-35b-a3b** | **OpenRouter** | $0.00954 | $0.1000 | $0.9500 | CheaperInference ($0.01759) | **45.8%** |
| **qwen3.5-35b-a3b** | **OpenRouter** | $0.00757 | $0.0800 | $0.7500 | CheaperInference ($0.01389) | **45.5%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **OpenRouter** — calidad 7.1/10 · coste/tarea $0.02790 (\$0.5000 in / \$2.1500 out) · Radar Value 56.9
2. **o4-mini-high** vía **OpenRouter** — calidad 7.2/10 · coste/tarea $0.05940 (\$1.1000 in / \$4.4000 out) · Radar Value 48.7
3. **kimi-k2** vía **OpenRouter** — calidad 5.9/10 · coste/tarea $0.03090 (\$0.5700 in / \$2.3000 out) · Radar Value 46.4
4. **deepseek-r1** vía **OpenRouter** — calidad 5.7/10 · coste/tarea $0.03600 (\$0.7000 in / \$2.5000 out) · Radar Value 43.5
5. **o3** vía **OpenRouter** — calidad 7.7/10 · coste/tarea $0.10800 (\$2.0000 in / \$8.0000 out) · Radar Value 43.3

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.6/10 · coste/tarea $0.00382 (\$0.0910 in / \$0.1820 out) · Radar Value 82.9
2. **glm-5.3-flash** vía **OpenRouter → StreamLake (streamlake/fp8)** — calidad 8.2/10 · coste/tarea $0.00217 (\$0.0435 in / \$0.1450 out) · Radar Value 80.3
3. **qwen3.8-27b** vía **OpenRouter → Tenstorrent (tenstorrent/fp4)** — calidad 8.0/10 · coste/tarea $0.00360 (\$0.0200 in / \$0.5000 out) · Radar Value 77.3
4. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.5/10 · coste/tarea $0.01373 (\$0.3270 in / \$0.6540 out) · Radar Value 75.3
5. **glm-5.3-flashx** vía **OpenRouter** — calidad 8.2/10 · coste/tarea $0.01860 (\$0.3700 in / \$1.2500 out) · Radar Value 70.0

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-v4-pro-0813** vía **OpenRouter → Reka** — **-84.0%** (ahora \$0.4800 in / \$1.2800 out)
- **qwen3.8-27b** vía **OpenRouter → ModelRun (modelrun/fp4)** — **-71.4%** (ahora \$0.2000 in / \$2.5000 out)
- **deepseek-v4.1-flash** vía **OpenRouter** — **-70.6%** (ahora \$0.0441 in / \$0.6210 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Baidu (baidu/fp8)** — **-66.0%** (ahora \$0.1020 in / \$0.4080 out)
- **qwen3.8-27b** vía **OpenRouter → Tenstorrent (tenstorrent/fp4)** — **-63.0%** (ahora \$0.0200 in / \$0.5000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Wafer** — **-54.5%** (ahora \$0.0700 in / \$0.4500 out)
- **deepseek-flash** vía **OpenRouter** — **-47.7%** (ahora \$0.0441 in / \$0.6210 out)
- **deepseek-v4.1-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — **-47.7%** (ahora \$0.0441 in / \$0.6210 out)
- **glm-5.2** vía **OpenRouter → SiliconFlow (siliconflow/fp8)** — **-41.2%** (ahora \$0.7000 in / \$2.2000 out)
- **gpt-oss-120b** vía **CheaperInference** — **-38.8%** (ahora \$0.0400 in / \$0.2000 out)
- **glm-5.3** vía **OpenRouter → SiliconFlow (siliconflow/fp8)** — **-37.5%** (ahora \$0.7000 in / \$2.2000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → AtlasCloud (atlas-cloud/fp8)** — **-36.0%** (ahora \$0.1920 in / \$0.7680 out)

### Subidas

- **glm-5.2** vía **OpenRouter → Baidu (baidu/fp8)** — +351.7% (ahora \$0.7588 in / \$2.3848 out)
- **gpt-oss-120b** vía **OpenRouter** — +305.4% (ahora \$0.1500 in / \$0.6000 out)
- **glm-5.3** vía **OpenRouter → Inceptron (inceptron/fp4)** — +251.4% (ahora \$0.6000 in / \$2.1956 out)
- **glm-5.3** vía **OpenRouter → Baidu (baidu/fp8)** — +251.4% (ahora \$0.6986 in / \$2.1956 out)
- **deepseek-v4-flash** vía **OpenRouter** — +203.3% (ahora \$0.0910 in / \$0.1820 out)
- **glm-5.2** vía **OpenRouter → Baidu (baidu/fast)** — +196.7% (ahora \$2.2500 in / \$7.8800 out)
- **glm-5.2** vía **OpenRouter → Inceptron (inceptron/fp4)** — +178.4% (ahora \$0.6900 in / \$2.9400 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Ionstream** — +170.0% (ahora \$0.2700 in / \$1.1000 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
