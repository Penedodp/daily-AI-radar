# Daily AI Radar — 2026-09-24

> Generado 24/09/2026 13:44 WEST · **613 modelos únicos** · **982 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **171 endpoints de 35 modelos OpenRouter monitorizados** · **73 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 73 modelos con benchmark propio, 221 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_4 ruta(s) duplicada(s) exacta(s) detectada(s) y eliminada(s) antes de publicar._

_115 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 453 |
| cheaperinference | `ok` | 62 |
| together | `ok` | 187 |
| novita | `ok` | 122 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 130 |
| openrouter_routes | `ok` | 171 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **qwen3.8-27b** | 8.0/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **OpenRouter** | $0.02790 | $0.5000 | $2.1500 | 7.1/10 | 56.9 |
| 💻 Coding | LMArena WebDev Arena | **glm-5.3-flash** | **OpenRouter → InferenceNet (inference-net/fp4)** | $0.00219 | $0.0450 | $0.1400 | 8.3/10 | 81.2 |

## 🧠 Mayor puntuación entre modelos de pago (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad |
|---|---|---|---|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **o3** | OpenRouter | $0.10800 | $2.0000 | $8.0000 | 7.7/10 |
| 💻 Coding | LMArena WebDev Arena | **qwen3.8-max** | CheaperInference | $0.08400 | $1.7500 | $5.2500 | 9.0/10 |

_Próximamente: 🤖 Agentic coding · 🧠 Razonamiento · ⚡ General (sin benchmark automatizado todavía)._

\* *Aider Polyglot Leaderboard (pass-rate de un test de corrección fijo) y LMArena WebDev Arena (rating Elo por voto humano) son benchmarks distintos, escalados a 0–10 cada uno por separado. **Nunca se ordenan entre sí como si fueran la misma escala** — cada tabla indica la fuente exacta junto al dato, no solo al pasar el ratón por encima. Emparejados automáticamente por nombre de modelo; sin match fiable, el modelo queda sin puntuar en vez de estimarse.*

\*\* *Radar Value es un índice propio (no un benchmark) que combina calidad medida y coste estimado: `calidad × 10 / sqrt(1 + coste_tarea / 0.05)`. El ancla de 0.05 USD/tarea es el punto en el que empieza a penalizar el coste; es configurable en `config.json`.*

## 🔀 Mismo modelo, proveedor/ruta más barata

| Modelo | Más barato | Coste perfil | $/M input | $/M output | Siguiente | Ahorro vs siguiente |
|---|---|---:|---:|---:|---|---:|
| **qwen3-vl-32b-instruct** | **OpenRouter** | $0.00612 | $0.1040 | $0.4160 | Together AI ($0.02612) | **76.6%** |
| **deepseek-r1** | **OpenRouter** | $0.03922 | $0.7000 | $2.5000 | Novita AI ($0.15578) | **74.8%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **mistral-nemo** | **OpenRouter** | $0.00081 | $0.0190 | $0.0300 | Novita AI ($0.00242) | **66.4%** |
| **ling-3.0-flash** | **OpenRouter** | $0.00110 | $0.0210 | $0.0630 | Novita AI ($0.00313) | **65.0%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **qwen3-max** | **OpenRouter** | $0.05111 | $0.7800 | $3.9000 | Novita AI ($0.12430) | **58.9%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **llama-3.1-8b-instruct** | **Novita AI** | $0.00098 | $0.0200 | $0.0500 | OpenRouter ($0.00215) | **54.4%** |
| **deepseek-v4-flash-vision-exp** | **OpenRouter** | $0.01149 | $0.2200 | $0.6600 | Novita AI ($0.02298) | **50.0%** |
| **deepseek-v3.1** | **Novita AI** | $0.01537 | $0.2700 | $1.0000 | Together AI ($0.03068) | **49.9%** |
| **gpt-oss-20b** | **OpenRouter** | $0.00118 | $0.0180 | $0.0900 | Novita AI ($0.00229) | **48.5%** |
| **glm-4.5** | **CheaperInference** | $0.01870 | $0.3300 | $1.2100 | OpenRouter ($0.03400) | **45.0%** |
| **qwen3-coder-next** | **OpenRouter** | $0.00919 | $0.1200 | $0.8000 | Novita AI ($0.01643) | **44.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **OpenRouter** — calidad 7.1/10 · coste/tarea $0.02790 (\$0.5000 in / \$2.1500 out) · Radar Value 56.9
2. **o4-mini-high** vía **OpenRouter** — calidad 7.2/10 · coste/tarea $0.05940 (\$1.1000 in / \$4.4000 out) · Radar Value 48.7
3. **kimi-k2** vía **OpenRouter** — calidad 5.9/10 · coste/tarea $0.03090 (\$0.5700 in / \$2.3000 out) · Radar Value 46.4
4. **deepseek-r1** vía **OpenRouter** — calidad 5.7/10 · coste/tarea $0.03600 (\$0.7000 in / \$2.5000 out) · Radar Value 43.5
5. **o3** vía **OpenRouter** — calidad 7.7/10 · coste/tarea $0.10800 (\$2.0000 in / \$8.0000 out) · Radar Value 43.3

### 💻 Coding · LMArena WebDev Arena
1. **glm-5.3-flash** vía **OpenRouter → InferenceNet (inference-net/fp4)** — calidad 8.3/10 · coste/tarea $0.00219 (\$0.0450 in / \$0.1400 out) · Radar Value 81.2
2. **glm-5.3-flashx** vía **OpenRouter** — calidad 8.3/10 · coste/tarea $0.01860 (\$0.3700 in / \$1.2500 out) · Radar Value 70.9
3. **qwen3.8-27b** vía **OpenRouter → Darkbloom (darkbloom/fp4)** — calidad 8.0/10 · coste/tarea $0.01380 (\$0.1000 in / \$1.8000 out) · Radar Value 70.8
4. **hy3** vía **OpenRouter** — calidad 7.0/10 · coste/tarea $0.00713 (\$0.1320 in / \$0.5280 out) · Radar Value 65.5
5. **hy4-preview** vía **OpenRouter** — calidad 8.5/10 · coste/tarea $0.04003 (\$0.8340 in / \$2.5010 out) · Radar Value 63.3

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-pro** vía **OpenRouter** — **-72.8%** (ahora \$0.3894 in / \$1.1682 out)
- **gpt-oss-120b** vía **CheaperInference** — **-52.9%** (ahora \$0.0400 in / \$0.2000 out)
- **deepseek-v4-flash-0731** vía **OpenRouter** — **-50.0%** (ahora \$0.0300 in / \$0.3200 out)
- **glm-5.3-flash** vía **OpenRouter → InferenceNet (inference-net/fp4)** — **-50.0%** (ahora \$0.0450 in / \$0.1400 out)
- **deepseek-v4-flash-0731** vía **OpenRouter → Relace (relace/fp4)** — **-50.0%** (ahora \$0.0300 in / \$0.3200 out)
- **glm-flash** vía **OpenRouter** — **-44.0%** (ahora \$0.0450 in / \$0.1400 out)
- **deepseek-v4-flash** vía **OpenRouter** — **-41.8%** (ahora \$0.0300 in / \$0.3200 out)
- **glm-5.3:batch** vía **OpenRouter** — **-37.5%** (ahora \$0.4500 in / \$2.0000 out)
- **deepseek-v4-pro-0813** vía **OpenRouter → Phala** — **-34.0%** (ahora \$0.9570 in / \$2.8776 out)
- **deepseek-v4-flash-0731** vía **OpenRouter → Inceptron (inceptron/fp4)** — **-32.5%** (ahora \$0.0828 in / \$0.4138 out)
- **qwen3.6-27b** vía **CheaperInference** — **-31.2%** (ahora \$0.2888 in / \$1.7328 out)
- **deepseek-v4.1-flash** vía **OpenRouter** — **-30.0%** (ahora \$0.1400 in / \$0.4200 out)

### Subidas

- **qwen3-6-35b-a3b** vía **CheaperInference** — +148.0% (ahora \$0.1736 in / \$1.0395 out)
- **qwen3-30b-a3b-instruct-2507** vía **OpenRouter** — +107.7% (ahora \$0.1000 in / \$0.3000 out)
- **qwen3.8-27b** vía **OpenRouter → Reka (reka/fp8)** — +102.3% (ahora \$0.0940 in / \$4.4000 out)
- **deepseek-flash** vía **OpenRouter** — +100.0% (ahora \$0.0400 in / \$1.0000 out)
- **qwen3.8-27b** vía **OpenRouter → DekaLLM** — +76.0% (ahora \$0.0960 in / \$4.4000 out)
- **deepseek-v4-flash-0731** vía **OpenRouter → OpenInference (open-inference/fp8)** — +40.0% (ahora \$0.1400 in / \$0.7000 out)
- **claude-opus-5.5** vía **CheaperInference** — +21.4% (ahora \$3.4000 in / \$17.0000 out)
- **claude-opus-4.7** vía **CheaperInference** — +21.4% (ahora \$4.2500 in / \$21.2500 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
