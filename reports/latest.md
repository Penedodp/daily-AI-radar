# Daily AI Radar — 2026-11-25

> Generado 25/11/2026 18:40 WET · **735 modelos únicos** · **1259 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **218 endpoints de 35 modelos OpenRouter monitorizados** · **79 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 79 modelos con benchmark propio, 311 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_115 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 426 |
| cheaperinference | `ok` | 347 |
| together | `ok` | 196 |
| novita | `ok` | 80 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 161 |
| openrouter_routes | `ok` | 218 |

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
| **qwen-mt-plus** | **Novita AI** | $0.01306 | $0.2500 | $0.7500 | CheaperInference ($0.08348) | **84.4%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02765) | **74.6%** |
| **mythomax-l2-13b** | **Novita AI** | $0.00350 | $0.0900 | $0.0900 | OpenRouter ($0.01301) | **73.1%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **llama-4-maverick** | **CheaperInference** | $0.00654 | $0.1222 | $0.3900 | OpenRouter ($0.01795) | **63.6%** |
| **ling-3.0-flash-sante** | **CheaperInference** | $0.00141 | $0.0273 | $0.0799 | Novita AI ($0.00388) | **63.6%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00577 | $0.0800 | $0.4800 | OpenRouter ($0.01443) | **60.0%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **ling-3.0-flash-fin** | **CheaperInference** | $0.00159 | $0.0307 | $0.0898 | Novita AI ($0.00388) | **59.1%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **sonar** | **CheaperInference** | $0.01605 | $0.1625 | $1.6250 | OpenRouter ($0.03895) | **58.8%** |
| **qwen3.8-27b** | **CheaperInference** | $0.00408 | $0.0750 | $0.2500 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **57.3%** |
| **hy4-flash** | **CheaperInference** | $0.00093 | $0.0158 | $0.0632 | OpenRouter ($0.00206) | **55.0%** |
| **gemini-4-carbon** | **CheaperInference** | $0.05897 | $0.9000 | $4.5000 | OpenRouter ($0.13105) | **55.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02627 (\$0.4845 in / \$1.9550 out) · Radar Value 47.8
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.09180 (\$1.7000 in / \$6.8000 out) · Radar Value 45.7
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **inkling-2-small** vía **OpenRouter → PrimeIntellect (primeintellect/flex)** — calidad 8.7/10 · coste/tarea $0.00375 (\$0.0750 in / \$0.2500 out) · Radar Value 83.9
2. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.6/10 · coste/tarea $0.00396 (\$0.0944 in / \$0.1888 out) · Radar Value 82.8
3. **glm-5.3-flash** vía **CheaperInference** — calidad 8.3/10 · coste/tarea $0.00118 (\$0.0281 in / \$0.0565 out) · Radar Value 82.0
4. **hy4** vía **CheaperInference** — calidad 8.8/10 · coste/tarea $0.00901 (\$0.1877 in / \$0.5627 out) · Radar Value 81.0
5. **qwen3.8-27b** vía **CheaperInference** — calidad 8.0/10 · coste/tarea $0.00375 (\$0.0750 in / \$0.2500 out) · Radar Value 77.2

## 🔥 Bajadas reales de precio (vs ayer)

- **minimax-m3.1-flash** vía **OpenRouter → Inferact vLLM (inferact-vllm/nvfp4)** — **-50.0%** (ahora \$0.0750 in / \$0.3000 out)
- **deepseek-v4-pro** vía **OpenRouter** — **-43.5%** (ahora \$0.7234 in / \$1.5228 out)
- **gemini-4-neon-fast** vía **CheaperInference** — **-43.2%** (ahora \$3.5100 in / \$17.5500 out)
- **qwen3.8-27b** vía **OpenRouter** — **-41.7%** (ahora \$0.0350 in / \$1.5000 out)
- **minimax-m3.1-flash** vía **OpenRouter** — **-25.0%** (ahora \$0.0750 in / \$0.3000 out)
- **glm-5.3-flash** vía **OpenRouter** — **-24.0%** (ahora \$0.1200 in / \$0.3800 out)
- **deepseek-v3** vía **CheaperInference** — **-23.5%** (ahora \$0.1755 in / \$0.7150 out)
- **gemini-2.5-pro** vía **CheaperInference** — **-23.5%** (ahora \$0.8125 in / \$6.5000 out)
- **glm-4.5v** vía **CheaperInference** — **-23.5%** (ahora \$0.3900 in / \$1.1700 out)
- **gpt-4.1-mini-fast** vía **CheaperInference** — **-23.5%** (ahora \$0.4550 in / \$1.8200 out)
- **gpt-5.6-luna-fast** vía **CheaperInference** — **-23.5%** (ahora \$0.2600 in / \$1.5600 out)
- **gpt-6-luna-fast** vía **CheaperInference** — **-23.5%** (ahora \$0.1300 in / \$0.6500 out)

### Subidas

- **deepseek-v4.1-flash-1017** vía **OpenRouter** — +150.0% (ahora \$0.0360 in / \$0.5000 out)
- **deepseek-flash** vía **OpenRouter** — +150.0% (ahora \$0.0360 in / \$0.5000 out)
- **qwen3.6-35b-a3b** vía **OpenRouter** — +100.0% (ahora \$0.1000 in / \$0.8900 out)
- **minimax-m3.1-flash** vía **OpenRouter → Makora (makora/fp4)** — +50.0% (ahora \$0.1500 in / \$0.6000 out)
- **nemotron-3.5-lightning** vía **OpenRouter** — +40.0% (ahora \$0.0700 in / \$0.2000 out)
- **arrow-2** vía **CheaperInference** — +30.8% (ahora \$3.4000 in / \$17.0000 out)
- **claude-fable-5.2-fast** vía **CheaperInference** — +30.8% (ahora \$13.6000 in / \$68.0000 out)
- **codestral** vía **CheaperInference** — +30.8% (ahora \$0.2550 in / \$0.7650 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
