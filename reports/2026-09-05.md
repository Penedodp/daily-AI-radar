# Daily AI Radar — 2026-09-05

> Generado 05/09/2026 11:48 WEST · **605 modelos únicos** · **1051 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **237 rutas OpenRouter analizadas** · **376 rutas puntuadas**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_3 ruta(s) duplicada(s) exacta(s) detectada(s) y eliminada(s) antes de publicar._

_124 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 426 |
| cheaperinference | `ok` | 58 |
| together | `ok` | 187 |
| novita | `ok` | 156 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 121 |
| openrouter_routes | `ok` | 237 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| — | — | Ningún modelo gratuito puntuado todavía | — | — | — | — |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **OpenRouter** | $0.02790 | $0.5000 | $2.1500 | 7.1/10 | 56.9 |
| 💻 Coding | LMArena WebDev Arena | **glm-5.3-flash** | **CheaperInference** | $0.00334 | $0.0668 | $0.2227 | 8.2/10 | 79.4 |

## 🧠 Mayor puntuación entre modelos de pago (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad |
|---|---|---|---|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **gemini-2.5-pro-preview-05-06** | OpenRouter | $0.09750 | $1.2500 | $10.0000 | 7.7/10 |
| 💻 Coding | LMArena WebDev Arena | **qwen3.8-max-0902** | OpenRouter | $0.09600 | $2.0000 | $6.0000 | 9.3/10 |

_Próximamente: 🤖 Agentic coding · 🧠 Razonamiento · ⚡ General (sin benchmark automatizado todavía)._

\* *Aider Polyglot Leaderboard (pass-rate de un test de corrección fijo) y LMArena WebDev Arena (rating Elo por voto humano) son benchmarks distintos, escalados a 0–10 cada uno por separado. **Nunca se ordenan entre sí como si fueran la misma escala** — cada tabla indica la fuente exacta junto al dato, no solo al pasar el ratón por encima. Emparejados automáticamente por nombre de modelo; sin match fiable, el modelo queda sin puntuar en vez de estimarse.*

\*\* *Radar Value es un índice propio (no un benchmark) que combina calidad medida y coste estimado: `calidad × 10 / sqrt(1 + coste_tarea / 0.05)`. El ancla de 0.05 USD/tarea es el punto en el que empieza a penalizar el coste; es configurable en `config.json`.*

## 🔀 Mismo modelo, proveedor/ruta más barata

| Modelo | Más barato | Coste perfil | $/M input | $/M output | Siguiente | Ahorro vs siguiente |
|---|---|---:|---:|---:|---|---:|
| **deepseek-r1-distill-qwen-14b** | **Novita AI** | $0.00584 | $0.1500 | $0.1500 | Together AI ($0.06231) | **90.6%** |
| **qwen3-vl-32b-instruct** | **OpenRouter** | $0.00612 | $0.1040 | $0.4160 | Together AI ($0.02612) | **76.6%** |
| **deepseek-r1** | **OpenRouter** | $0.03922 | $0.7000 | $2.5000 | Novita AI ($0.15578) | **74.8%** |
| **glm-5.3** | **CheaperInference** | $0.02048 | $0.3850 | $1.2100 | OpenRouter ($0.07446) | **72.5%** |
| **mistral-nemo** | **OpenRouter** | $0.00081 | $0.0190 | $0.0300 | Novita AI ($0.00242) | **66.4%** |
| **ling-3.0-flash** | **OpenRouter** | $0.00110 | $0.0210 | $0.0630 | Novita AI ($0.00313) | **65.0%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00577 | $0.0800 | $0.4800 | OpenRouter ($0.01443) | **60.0%** |
| **qwen3-max** | **OpenRouter** | $0.05111 | $0.7800 | $3.9000 | Novita AI ($0.12430) | **58.9%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **deepseek-v4-pro-0813** | **CheaperInference** | $0.02413 | $0.4620 | $1.3860 | OpenRouter ($0.05854) | **58.8%** |
| **llama-3.1-8b-instruct** | **Novita AI** | $0.00098 | $0.0200 | $0.0500 | OpenRouter ($0.00215) | **54.4%** |
| **glm-5.2** | **CheaperInference** | $0.02353 | $0.4400 | $1.4025 | OpenRouter ($0.05138) | **54.2%** |
| **deepseek-v4-flash-vision-exp** | **OpenRouter** | $0.01149 | $0.2200 | $0.6600 | Novita AI ($0.02298) | **50.0%** |
| **gemini-3.1-flash-lite-preview** | **OpenRouter → Google AI Studio (google-ai-studio/flex)** | $0.00902 | $0.1250 | $0.7500 | OpenRouter ($0.01804) | **50.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **OpenRouter** — calidad 7.1/10 · coste/tarea $0.02790 (\$0.5000 in / \$2.1500 out) · Radar Value 56.9
2. **o4-mini-high** vía **OpenRouter** — calidad 7.2/10 · coste/tarea $0.05940 (\$1.1000 in / \$4.4000 out) · Radar Value 48.7
3. **deepseek-v3-0324** vía **Novita AI** — calidad 5.5/10 · coste/tarea $0.01482 (\$0.2700 in / \$1.1200 out) · Radar Value 48.3
4. **kimi-k2** vía **OpenRouter** — calidad 5.9/10 · coste/tarea $0.03090 (\$0.5700 in / \$2.3000 out) · Radar Value 46.4
5. **gemini-2.5-pro-preview-05-06** vía **OpenRouter** — calidad 7.7/10 · coste/tarea $0.09750 (\$1.2500 in / \$10.0000 out) · Radar Value 44.8

### 💻 Coding · LMArena WebDev Arena
1. **glm-5.3-flash** vía **CheaperInference** — calidad 8.2/10 · coste/tarea $0.00334 (\$0.0668 in / \$0.2227 out) · Radar Value 79.4
2. **qwen3.8-27b** vía **OpenRouter → Parasail (parasail/fp8)** — calidad 8.1/10 · coste/tarea $0.02040 (\$0.2400 in / \$2.2000 out) · Radar Value 68.3
3. **hy3** vía **OpenRouter → GMICloud (gmicloud/bf16)** — calidad 7.0/10 · coste/tarea $0.00691 (\$0.1260 in / \$0.5220 out) · Radar Value 65.6
4. **hy4-preview** vía **OpenRouter** — calidad 8.5/10 · coste/tarea $0.04003 (\$0.8340 in / \$2.5010 out) · Radar Value 63.3
5. **minimax-m3** vía **OpenRouter → CoreWeave (coreweave/fp4)** — calidad 6.7/10 · coste/tarea $0.01266 (\$0.2300 in / \$0.9600 out) · Radar Value 59.9

## 🔥 Bajadas reales de precio (vs ayer)

- **grok-4.5** vía **OpenRouter → xAI** — **-50.0%** (ahora \$2.0000 in / \$6.0000 out)
- **claude-opus-4.8** vía **OpenRouter → Anthropic** — **-50.0%** (ahora \$5.0000 in / \$25.0000 out)
- **grok-4.3** vía **OpenRouter → xAI** — **-50.0%** (ahora \$1.2500 in / \$2.5000 out)
- **gemini-3.7-flash** vía **CheaperInference** — **-28.6%** (ahora \$0.5250 in / \$2.6250 out)
- **deepseek-v4-pro** vía **OpenRouter** — **-10.1%** (ahora \$0.9004 in / \$1.8009 out)

### Subidas

- **deepseek-v4-pro-0813** vía **OpenRouter** — +93.4% (ahora \$1.1207 in / \$3.3620 out)
- **hy3** vía **OpenRouter** — +60.0% (ahora \$0.1320 in / \$0.5280 out)
- **qwen3-235b-a22b-2507** vía **OpenRouter** — +27.4% (ahora \$0.0900 in / \$0.5500 out)
- **gpt-5.6-terra** vía **CheaperInference** — +24.4% (ahora \$1.8800 in / \$11.2800 out)
- **gpt-5.6-sol** vía **CheaperInference** — +16.3% (ahora \$1.1628 in / \$5.8140 out)
- **gemini-2.5-flash** vía **CheaperInference** — +16.3% (ahora \$0.2442 in / \$2.0349 out)
- **aion-labs.aion-2-0** vía **CheaperInference** — +13.0% (ahora \$0.7907 in / \$1.5814 out)
- **deepseek-v4-flash-0731** vía **CheaperInference** — +11.7% (ahora \$0.0509 in / \$0.1025 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
