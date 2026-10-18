# Daily AI Radar — 2026-10-18

> Generado 18/10/2026 13:04 WEST · **626 modelos únicos** · **1104 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **272 endpoints de 35 modelos OpenRouter monitorizados** · **75 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 75 modelos con benchmark propio, 248 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_114 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 464 |
| cheaperinference | `ok` | 91 |
| together | `ok` | 191 |
| novita | `ok` | 95 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 143 |
| openrouter_routes | `ok` | 272 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling** | 5.8/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **OpenRouter** | $0.02790 | $0.5000 | $2.1500 | 7.1/10 | 56.9 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **OpenRouter → Darkbloom (darkbloom/fp4)** | $0.00468 | $0.1000 | $0.2800 | 8.6/10 | 82.2 |

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
| **deepseek-v4-flash** | **OpenRouter** | $0.00108 | $0.0039 | $0.1436 | CheaperInference ($0.00530) | **79.6%** |
| **qwen3-coder-30b-a3b-instruct** | **OpenRouter** | $0.00412 | $0.0700 | $0.2800 | CheaperInference ($0.01917) | **78.5%** |
| **ling-3.1-flash** | **OpenRouter** | $0.00392 | $0.0750 | $0.2250 | Novita AI ($0.01567) | **75.0%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **deepseek-v4-flash-0731** | **OpenRouter → OpenInference (open-inference/fp4)** | $0.00108 | $0.0039 | $0.1436 | OpenRouter → Baidu (baidu/fp8) ($0.00313) | **65.4%** |
| **ling-3.0-flash** | **OpenRouter** | $0.00110 | $0.0210 | $0.0630 | Novita AI ($0.00313) | **65.0%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **deepseek-v4-pro** | **OpenRouter** | $0.00952 | $0.2088 | $0.4176 | CheaperInference ($0.02517) | **62.2%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **gpt-oss-20b** | **OpenRouter** | $0.00118 | $0.0180 | $0.0900 | Together AI ($0.00294) | **59.9%** |
| **deepseek-v4-pro-0813** | **OpenRouter → Baidu (baidu/fp8)** | $0.00696 | $0.1333 | $0.4000 | CheaperInference ($0.01726) | **59.6%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00585 | $0.0810 | $0.4863 | OpenRouter ($0.01443) | **59.5%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **qwen3.8-27b** | **OpenRouter → Tenstorrent (tenstorrent/fp4)** | $0.00397 | $0.0200 | $0.5000 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **58.5%** |
| **llama-3.1-8b-instruct** | **Novita AI** | $0.00098 | $0.0200 | $0.0500 | OpenRouter ($0.00215) | **54.4%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **OpenRouter** — calidad 7.1/10 · coste/tarea $0.02790 (\$0.5000 in / \$2.1500 out) · Radar Value 56.9
2. **o4-mini-high** vía **OpenRouter** — calidad 7.2/10 · coste/tarea $0.05940 (\$1.1000 in / \$4.4000 out) · Radar Value 48.7
3. **kimi-k2** vía **OpenRouter** — calidad 5.9/10 · coste/tarea $0.03090 (\$0.5700 in / \$2.3000 out) · Radar Value 46.4
4. **deepseek-r1** vía **OpenRouter** — calidad 5.7/10 · coste/tarea $0.03600 (\$0.7000 in / \$2.5000 out) · Radar Value 43.5
5. **o3** vía **OpenRouter** — calidad 7.7/10 · coste/tarea $0.10800 (\$2.0000 in / \$8.0000 out) · Radar Value 43.3

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **OpenRouter → Darkbloom (darkbloom/fp4)** — calidad 8.6/10 · coste/tarea $0.00468 (\$0.1000 in / \$0.2800 out) · Radar Value 82.2
2. **glm-5.3-flash** vía **OpenRouter** — calidad 8.2/10 · coste/tarea $0.00264 (\$0.0480 in / \$0.2000 out) · Radar Value 79.9
3. **qwen3.8-27b** vía **OpenRouter → Tenstorrent (tenstorrent/fp4)** — calidad 8.0/10 · coste/tarea $0.00360 (\$0.0200 in / \$0.5000 out) · Radar Value 77.3
4. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01548 (\$0.3687 in / \$0.7373 out) · Radar Value 73.4
5. **glm-5.3-flashx** vía **OpenRouter** — calidad 8.2/10 · coste/tarea $0.01860 (\$0.3700 in / \$1.2500 out) · Radar Value 70.0

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-v4-flash** vía **OpenRouter** — **-88.8%** (ahora \$0.0039 in / \$0.1436 out)
- **deepseek-v4-flash-0731** vía **OpenRouter → OpenInference (open-inference/fp4)** — **-88.8%** (ahora \$0.0039 in / \$0.1436 out)
- **glm-flash** vía **OpenRouter** — **-87.5%** (ahora \$0.0480 in / \$0.2000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — **-80.0%** (ahora \$0.0400 in / \$0.1440 out)
- **deepseek-v4.1-flash** vía **OpenRouter** — **-76.0%** (ahora \$0.0400 in / \$0.1440 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Relace** — **-75.0%** (ahora \$0.0500 in / \$0.6000 out)
- **pareto** vía **OpenRouter** — **-68.0%** (ahora \$0.8000 in / \$3.2000 out)
- **glm-5.3-flash** vía **OpenRouter** — **-68.0%** (ahora \$0.0480 in / \$0.2000 out)
- **deepseek-v4-flash-0731** vía **OpenRouter** — **-64.8%** (ahora \$0.0049 in / \$0.4500 out)
- **deepseek-v4-flash-0731** vía **OpenRouter → Relace (relace/fp4)** — **-64.8%** (ahora \$0.0049 in / \$0.4500 out)
- **kimi-k3** vía **OpenRouter → Morph (morph/fp8)** — **-60.7%** (ahora \$0.3140 in / \$14.9000 out)
- **glm-5.3-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — **-60.0%** (ahora \$0.0480 in / \$0.2000 out)

### Subidas

- **deepseek-pro** vía **OpenRouter** — +1900.2% (ahora \$0.1200 in / \$8.0000 out)
- **deepseek-v4-pro-0813** vía **OpenRouter → Wafer (wafer/mxfp4)** — +100.0% (ahora \$0.2500 in / \$5.0000 out)
- **glm-5.3-flash** vía **OpenRouter → Morph (morph/fp8)** — +51.8% (ahora \$0.1290 in / \$0.6500 out)
- **deepseek-v4.1-flash** vía **CheaperInference** — +31.1% (ahora \$0.0675 in / \$0.2700 out)
- **mimo-v2.6-flash** vía **CheaperInference** — +30.8% (ahora \$0.1190 in / \$0.2380 out)
- **minimax-m3** vía **CheaperInference** — +30.8% (ahora \$0.2550 in / \$1.0199 out)
- **claude-opus-5** vía **CheaperInference** — +25.9% (ahora \$4.2500 in / \$21.2500 out)
- **glm-4.5-air** vía **CheaperInference** — +21.8% (ahora \$0.1340 in / \$0.7370 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
