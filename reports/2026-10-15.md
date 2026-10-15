# Daily AI Radar — 2026-10-15

> Generado 15/10/2026 13:41 WEST · **615 modelos únicos** · **1121 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **303 endpoints de 35 modelos OpenRouter monitorizados** · **73 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 73 modelos con benchmark propio, 255 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_113 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 455 |
| cheaperinference | `ok` | 91 |
| together | `ok` | 187 |
| novita | `ok` | 95 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `cached_stale` | 141 |
| openrouter_routes | `ok` | 303 |

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
| **ling-3.1-flash** | **OpenRouter** | $0.00392 | $0.0750 | $0.2250 | Novita AI ($0.01567) | **75.0%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02431) | **71.1%** |
| **ling-3.0-flash** | **OpenRouter** | $0.00110 | $0.0210 | $0.0630 | Novita AI ($0.00313) | **65.0%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **gpt-oss-20b** | **OpenRouter** | $0.00118 | $0.0180 | $0.0900 | Together AI ($0.00294) | **59.9%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00585 | $0.0810 | $0.4863 | OpenRouter ($0.01443) | **59.5%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **qwen3.8-27b** | **OpenRouter → Tenstorrent (tenstorrent/fp4)** | $0.00397 | $0.0200 | $0.5000 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **58.5%** |
| **llama-3.1-8b-instruct** | **Novita AI** | $0.00098 | $0.0200 | $0.0500 | OpenRouter ($0.00215) | **54.4%** |
| **deepseek-v4-pro-0813** | **OpenRouter → Baidu (baidu/fp8)** | $0.01172 | $0.2244 | $0.6732 | CheaperInference ($0.02448) | **52.1%** |
| **gpt-5.6-sol** | **CheaperInference** | $0.13105 | $2.0000 | $10.0000 | OpenRouter ($0.26210) | **50.0%** |
| **kimi-k2-thinking** | **CheaperInference** | $0.01851 | $0.3055 | $1.3000 | OpenRouter ($0.03599) | **48.6%** |

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
3. **qwen3.8-27b** vía **OpenRouter → Tenstorrent (tenstorrent/fp4)** — calidad 8.1/10 · coste/tarea $0.00360 (\$0.0200 in / \$0.5000 out) · Radar Value 78.2
4. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01553 (\$0.3697 in / \$0.7394 out) · Radar Value 73.4
5. **glm-5.3-flashx** vía **OpenRouter** — calidad 8.2/10 · coste/tarea $0.01860 (\$0.3700 in / \$1.2500 out) · Radar Value 70.0

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-pro** vía **OpenRouter** — **-91.6%** (ahora \$0.2244 in / \$0.6732 out)
- **kimi-k3** vía **OpenRouter → Wafer (wafer/us)** — **-88.2%** (ahora \$0.3300 in / \$14.9000 out)
- **glm-5.2** vía **OpenRouter** — **-60.0%** (ahora \$0.0200 in / \$7.0000 out)
- **glm-5.2** vía **OpenRouter → Wafer (wafer/us)** — **-60.0%** (ahora \$0.0200 in / \$7.0000 out)
- **kimi-k3** vía **OpenRouter → Wafer** — **-56.9%** (ahora \$0.3100 in / \$24.0000 out)
- **kimi-k3** vía **OpenRouter → Relace (relace/fp4)** — **-40.3%** (ahora \$0.3200 in / \$14.0000 out)
- **kimi-k3** vía **OpenRouter** — **-35.7%** (ahora \$0.4500 in / \$15.0000 out)
- **kimi-k3** vía **OpenRouter → InferenceNet (inference-net/fp4)** — **-35.7%** (ahora \$0.4500 in / \$15.0000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Wafer** — **-34.3%** (ahora \$0.1000 in / \$0.6500 out)
- **glm-5.1** vía **OpenRouter** — **-27.4%** (ahora \$0.9660 in / \$3.0360 out)
- **kimi-k3** vía **OpenRouter → Morph (morph/fp8)** — **-25.5%** (ahora \$0.8000 in / \$14.9000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Morph (morph/fp8)** — **-25.0%** (ahora \$0.0330 in / \$0.6000 out)

### Subidas

- **qwen3.8-27b** vía **OpenRouter** — +500.0% (ahora \$0.2400 in / \$2.2000 out)
- **glm-5.3-flash** vía **OpenRouter** — +316.7% (ahora \$0.1500 in / \$0.5000 out)
- **gpt-oss-120b** vía **OpenRouter** — +305.4% (ahora \$0.1500 in / \$0.6000 out)
- **gemma-4-31b-it** vía **OpenRouter** — +122.2% (ahora \$0.2000 in / \$0.4000 out)
- **deepseek-v4-pro** vía **OpenRouter** — +113.3% (ahora \$0.9553 in / \$1.9105 out)
- **glm-5.3** vía **OpenRouter → Baidu (baidu/fp8)** — +100.4% (ahora \$1.4000 in / \$4.4000 out)
- **gpt-5.6-sol-pro** vía **OpenRouter** — +100.0% (ahora \$4.0000 in / \$20.0000 out)
- **gpt-5.6-sol-pro:batch** vía **OpenRouter** — +100.0% (ahora \$2.0000 in / \$10.0000 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
