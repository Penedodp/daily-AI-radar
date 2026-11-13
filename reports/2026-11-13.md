# Daily AI Radar — 2026-11-13

> Generado 13/11/2026 16:29 WET · **752 modelos únicos** · **1346 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **282 endpoints de 35 modelos OpenRouter monitorizados** · **82 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 82 modelos con benchmark propio, 313 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_119 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 427 |
| cheaperinference | `ok` | 353 |
| together | `ok` | 193 |
| novita | `ok` | 99 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `cached_stale` | 155 |
| openrouter_routes | `ok` | 282 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling-2-small** | 8.7/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **CheaperInference** | $0.00441 | $0.1050 | $0.2100 | 8.6/10 | 82.4 |

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
| **mimo-v2.5** | **CheaperInference** | $0.00538 | $0.1180 | $0.2361 | OpenRouter ($0.02621) | **79.5%** |
| **qwen3.8-27b** | **CheaperInference** | $0.00226 | $0.0350 | $0.1700 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **76.4%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02765) | **74.6%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **glm-5.2** | **CheaperInference** | $0.01336 | $0.1025 | $1.5125 | OpenRouter ($0.04541) | **70.6%** |
| **glm-5.3** | **CheaperInference** | $0.00785 | $0.0003 | $1.1800 | OpenRouter ($0.02663) | **70.5%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **deepseek-v4-flash-vision-exp** | **CheaperInference** | $0.00777 | $0.1320 | $0.5280 | OpenRouter ($0.02298) | **66.2%** |
| **ling-3.0-flash-fin** | **CheaperInference** | $0.00141 | $0.0273 | $0.0799 | Novita AI ($0.00388) | **63.6%** |
| **ling-3.0-flash-sante** | **CheaperInference** | $0.00141 | $0.0273 | $0.0799 | Novita AI ($0.00388) | **63.6%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00577 | $0.0800 | $0.4800 | OpenRouter ($0.01443) | **60.0%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **gemini-4-carbon** | **CheaperInference** | $0.05897 | $0.9000 | $4.5000 | OpenRouter ($0.13105) | **55.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.07020 (\$1.3000 in / \$5.2000 out) · Radar Value 49.7
3. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02554 (\$0.4711 in / \$1.9008 out) · Radar Value 48.0
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.6/10 · coste/tarea $0.00441 (\$0.1050 in / \$0.2100 out) · Radar Value 82.4
2. **inkling-2-small** vía **OpenRouter → PrimeIntellect (primeintellect/fp4)** — calidad 8.7/10 · coste/tarea $0.00750 (\$0.1500 in / \$0.5000 out) · Radar Value 81.1
3. **glm-5.3-flash** vía **CheaperInference** — calidad 8.2/10 · coste/tarea $0.00122 (\$0.0300 in / \$0.0534 out) · Radar Value 81.0
4. **qwen3.8-27b** vía **CheaperInference** — calidad 8.0/10 · coste/tarea $0.00207 (\$0.0350 in / \$0.1700 out) · Radar Value 78.4
5. **minimax-m3.1-flash** vía **OpenRouter** — calidad 7.9/10 · coste/tarea $0.00405 (\$0.0750 in / \$0.3000 out) · Radar Value 76.0

## 🔥 Bajadas reales de precio (vs ayer)

- **glm-5.3** vía **CheaperInference** — **-100.0%** (ahora \$0.0003 in / \$1.1800 out)
- **kimi-k3** vía **CheaperInference** — **-98.3%** (ahora \$0.0324 in / \$9.2500 out)
- **qwen3.8-27b** vía **CheaperInference** — **-91.3%** (ahora \$0.0350 in / \$0.1700 out)
- **kimi-k3.1-pro** vía **CheaperInference** — **-89.4%** (ahora \$0.1375 in / \$6.5000 out)
- **glm-5.2** vía **CheaperInference** — **-89.4%** (ahora \$0.1025 in / \$1.5125 out)
- **qwen3-coder** vía **CheaperInference** — **-85.1%** (ahora \$0.1450 in / \$1.4250 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Baidu (baidu/fp8)** — **-83.1%** (ahora \$0.0507 in / \$0.2028 out)
- **deepseek-v4.1-flash** vía **CheaperInference** — **-82.4%** (ahora \$0.0145 in / \$0.3300 out)
- **deepseek-v4.1-flash-1017** vía **CheaperInference** — **-78.0%** (ahora \$0.0145 in / \$0.2640 out)
- **deepseek-v4-flash-0731** vía **CheaperInference** — **-78.0%** (ahora \$0.0290 in / \$0.1070 out)
- **mistral-nemo** vía **CheaperInference** — **-77.9%** (ahora \$0.0215 in / \$0.0225 out)
- **deepseek-v3.2** vía **CheaperInference** — **-76.1%** (ahora \$0.2290 in / \$0.2875 out)

### Subidas

- **kimi-k3.1-pro** vía **OpenRouter** — +742.1% (ahora \$2.0000 in / \$10.0000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Morph (morph/fp8)** — +336.4% (ahora \$0.0960 in / \$0.5400 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Morph (morph/fp8)** — +336.4% (ahora \$0.0960 in / \$0.5400 out)
- **beam** vía **CheaperInference** — +306.4% (ahora \$0.0656 in / \$0.2605 out)
- **glm-5.3** vía **OpenRouter** — +157.1% (ahora \$0.0840 in / \$3.6000 out)
- **gemini-flash** vía **OpenRouter** — +100.0% (ahora \$1.5000 in / \$7.5000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter** — +72.7% (ahora \$0.0380 in / \$0.5000 out)
- **deepseek-flash** vía **OpenRouter** — +72.7% (ahora \$0.0380 in / \$0.5000 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
