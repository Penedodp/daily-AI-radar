# Daily AI Radar — 2026-11-23

> Generado 23/11/2026 20:17 WET · **737 modelos únicos** · **1230 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **183 endpoints de 35 modelos OpenRouter monitorizados** · **78 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 78 modelos con benchmark propio, 341 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_115 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 433 |
| cheaperinference | `ok` | 348 |
| together | `ok` | 196 |
| novita | `ok` | 78 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `cached_stale` | 160 |
| openrouter_routes | `ok` | 183 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| — | — | Ningún modelo gratuito puntuado todavía | — | — | — | — |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **inkling-2-small** | **OpenRouter → PrimeIntellect (primeintellect/flex)** | $0.00375 | $0.0750 | $0.2500 | 8.7/10 | 83.9 |

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
| **deepseek-v4.1-flash** | **CheaperInference** | $0.00266 | $0.0145 | $0.3300 | OpenRouter ($0.01766) | **84.9%** |
| **qwen-mt-plus** | **Novita AI** | $0.01306 | $0.2500 | $0.7500 | CheaperInference ($0.08348) | **84.4%** |
| **mimo-v2.5** | **CheaperInference** | $0.00531 | $0.1165 | $0.2330 | OpenRouter ($0.02621) | **79.7%** |
| **deepseek-v4-pro-0813** | **CheaperInference** | $0.01724 | $0.3300 | $0.9900 | OpenRouter ($0.06895) | **75.0%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02765) | **74.6%** |
| **mythomax-l2-13b** | **Novita AI** | $0.00350 | $0.0900 | $0.0900 | OpenRouter ($0.01301) | **73.1%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **qwen3.8-27b** | **CheaperInference** | $0.00291 | $0.0550 | $0.1700 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **69.6%** |
| **llama-4-maverick** | **CheaperInference** | $0.00654 | $0.1222 | $0.3900 | OpenRouter ($0.01795) | **63.6%** |
| **ling-3.0-flash-sante** | **CheaperInference** | $0.00141 | $0.0273 | $0.0799 | Novita AI ($0.00388) | **63.6%** |
| **deepseek-v3.1** | **CheaperInference** | $0.01165 | $0.2025 | $0.7695 | Together AI ($0.03068) | **62.0%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00577 | $0.0800 | $0.4800 | OpenRouter ($0.01443) | **60.0%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **hy4-flash** | **CheaperInference** | $0.00093 | $0.0158 | $0.0632 | OpenRouter ($0.00206) | **55.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02627 (\$0.4845 in / \$1.9550 out) · Radar Value 47.8
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.09180 (\$1.7000 in / \$6.8000 out) · Radar Value 45.7
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **inkling-2-small** vía **OpenRouter → PrimeIntellect (primeintellect/flex)** — calidad 8.7/10 · coste/tarea $0.00375 (\$0.0750 in / \$0.2500 out) · Radar Value 83.9
2. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.6/10 · coste/tarea $0.00382 (\$0.0910 in / \$0.1820 out) · Radar Value 82.9
3. **glm-5.3-flash** vía **CheaperInference** — calidad 8.3/10 · coste/tarea $0.00149 (\$0.0400 in / \$0.0479 out) · Radar Value 81.8
4. **hy4** vía **CheaperInference** — calidad 8.8/10 · coste/tarea $0.00901 (\$0.1877 in / \$0.5627 out) · Radar Value 81.0
5. **qwen3.8-27b** vía **CheaperInference** — calidad 8.0/10 · coste/tarea $0.00267 (\$0.0550 in / \$0.1700 out) · Radar Value 77.9

## 🔥 Bajadas reales de precio (vs ayer)

- **gemma-3-27b-it** vía **OpenRouter** — **-64.4%** (ahora \$0.0800 in / \$0.1600 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter** — **-60.0%** (ahora \$0.0300 in / \$0.2000 out)
- **deepseek-flash** vía **OpenRouter** — **-60.0%** (ahora \$0.0300 in / \$0.2000 out)
- **gpt-oss-20b** vía **OpenRouter** — **-60.0%** (ahora \$0.0300 in / \$0.1300 out)
- **qwen3.6-35b-a3b** vía **OpenRouter** — **-50.0%** (ahora \$0.0500 in / \$0.7000 out)
- **gpt-oss-120b** vía **OpenRouter** — **-44.4%** (ahora \$0.0500 in / \$0.2500 out)
- **deepseek-v4-pro-0813** vía **CheaperInference** — **-41.2%** (ahora \$0.3300 in / \$0.9900 out)
- **minimax-m3.1-flash** vía **OpenRouter → Makora (makora/fp4)** — **-41.2%** (ahora \$0.1000 in / \$0.4000 out)
- **deepseek-pro** vía **OpenRouter** — **-37.5%** (ahora \$0.0999 in / \$5.0000 out)
- **minimax-m3.1-flash** vía **OpenRouter** — **-25.9%** (ahora \$0.1000 in / \$0.4000 out)
- **hy4** vía **OpenRouter → DeepInfra (deepinfra/fp4)** — **-25.0%** (ahora \$0.6255 in / \$1.8758 out)
- **beam** vía **CheaperInference** — **-24.1%** (ahora \$0.0510 in / \$0.1529 out)

### Subidas

- **glm-5.3-flash** vía **OpenRouter** — +537.8% (ahora \$0.1500 in / \$0.5000 out)
- **deepseek-v4.1-flash** vía **OpenRouter** — +502.4% (ahora \$0.3000 in / \$1.2000 out)
- **qwen3.8-27b** vía **OpenRouter → Reka (reka/fp8)** — +200.0% (ahora \$0.4500 in / \$3.2000 out)
- **deepseek-v4-flash** vía **OpenRouter** — +127.3% (ahora \$0.0434 in / \$0.3000 out)
- **glm-5.1** vía **CheaperInference** — +34.4% (ahora \$0.8130 in / \$3.0674 out)
- **apex** vía **CheaperInference** — +30.8% (ahora \$0.4250 in / \$2.5500 out)
- **claude-fable-5.2-batch** vía **CheaperInference** — +30.8% (ahora \$3.4000 in / \$17.0000 out)
- **claude-opus-5** vía **CheaperInference** — +30.8% (ahora \$4.2500 in / \$21.2500 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
