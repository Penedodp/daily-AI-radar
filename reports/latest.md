# Daily AI Radar — 2026-11-16

> Generado 16/11/2026 18:37 WET · **748 modelos únicos** · **1315 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **252 endpoints de 35 modelos OpenRouter monitorizados** · **79 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 79 modelos con benchmark propio, 309 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_119 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 426 |
| cheaperinference | `ok` | 351 |
| together | `ok` | 193 |
| novita | `ok` | 101 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 156 |
| openrouter_routes | `ok` | 252 |

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
| **mimo-v2.5** | **CheaperInference** | $0.00543 | $0.1190 | $0.2380 | OpenRouter ($0.02621) | **79.3%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02765) | **74.6%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **glm-5.2** | **CheaperInference** | $0.01336 | $0.1025 | $1.5125 | OpenRouter ($0.04541) | **70.6%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **deepseek-v4-flash-vision-exp** | **CheaperInference** | $0.00777 | $0.1320 | $0.5280 | OpenRouter ($0.02298) | **66.2%** |
| **deepseek-v4.1-flash** | **CheaperInference** | $0.00266 | $0.0145 | $0.3300 | OpenRouter ($0.00731) | **63.6%** |
| **ling-3.0-flash-sante** | **CheaperInference** | $0.00141 | $0.0273 | $0.0799 | Novita AI ($0.00388) | **63.6%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00579 | $0.0802 | $0.4813 | OpenRouter ($0.01443) | **59.9%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **gemini-4-carbon** | **CheaperInference** | $0.05897 | $0.9000 | $4.5000 | OpenRouter ($0.13105) | **55.0%** |
| **hy4** | **CheaperInference** | $0.00980 | $0.1877 | $0.5627 | OpenRouter ($0.02178) | **55.0%** |
| **gemini-4-argon** | **CheaperInference** | $0.05897 | $0.9000 | $4.5000 | OpenRouter ($0.13105) | **55.0%** |
| **gemini-3.8-flash** | **CheaperInference** | $0.02211 | $0.3375 | $1.6875 | OpenRouter ($0.04914) | **55.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02503 (\$0.4617 in / \$1.8630 out) · Radar Value 48.2
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.08556 (\$1.5844 in / \$6.3378 out) · Radar Value 46.8
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.6/10 · coste/tarea $0.00441 (\$0.1050 in / \$0.2100 out) · Radar Value 82.4
2. **inkling-2-small** vía **OpenRouter → PrimeIntellect (primeintellect/fp4)** — calidad 8.7/10 · coste/tarea $0.00750 (\$0.1500 in / \$0.5000 out) · Radar Value 81.1
3. **glm-5.3-flash** vía **CheaperInference** — calidad 8.2/10 · coste/tarea $0.00122 (\$0.0300 in / \$0.0534 out) · Radar Value 81.0
4. **qwen3.8-27b** vía **CheaperInference** — calidad 8.0/10 · coste/tarea $0.00207 (\$0.0350 in / \$0.1700 out) · Radar Value 78.4
5. **minimax-m3.1-flash** vía **OpenRouter** — calidad 7.9/10 · coste/tarea $0.00405 (\$0.0750 in / \$0.3000 out) · Radar Value 76.0

## 🔥 Bajadas reales de precio (vs ayer)

- **glm-5.3-flash** vía **OpenRouter → Morph (morph/fp8)** — **-72.4%** (ahora \$0.0480 in / \$0.1380 out)
- **glm-5.3** vía **OpenRouter** — **-61.1%** (ahora \$0.0699 in / \$1.4000 out)
- **deepseek-v4-flash-0731** vía **OpenRouter** — **-40.0%** (ahora \$0.0600 in / \$0.1800 out)
- **hy3** vía **OpenRouter** — **-37.5%** (ahora \$0.0825 in / \$0.3300 out)
- **hy3** vía **OpenRouter → Tencent (tencent/fp8)** — **-37.5%** (ahora \$0.0825 in / \$0.3300 out)
- **glm-4.5-air** vía **OpenRouter** — **-35.0%** (ahora \$0.1300 in / \$0.8500 out)
- **deepseek-v4-flash-0731** vía **OpenRouter → StreamLake (streamlake/fp8)** — **-33.3%** (ahora \$0.0880 in / \$0.2640 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Novita (novita/fp8)** — **-27.3%** (ahora \$0.1200 in / \$0.4800 out)
- **qwen3.5-397b-a17b** vía **OpenRouter** — **-25.0%** (ahora \$0.4500 in / \$3.0000 out)
- **deepseek-v3** vía **CheaperInference** — **-23.5%** (ahora \$0.1755 in / \$0.7150 out)
- **gemini-2.5-flash-lite** vía **CheaperInference** — **-23.5%** (ahora \$0.0650 in / \$0.2600 out)
- **inkling-2-small** vía **CheaperInference** — **-23.5%** (ahora \$0.1950 in / \$0.6500 out)

### Subidas

- **deepseek-v4-flash-0731** vía **OpenRouter → Baidu (baidu/fp8)** — +635.3% (ahora \$0.4400 in / \$1.3200 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter** — +363.0% (ahora \$0.0360 in / \$0.5000 out)
- **deepseek-flash** vía **OpenRouter** — +363.0% (ahora \$0.0360 in / \$0.5000 out)
- **deepseek-v4.1-flash** vía **OpenRouter** — +176.1% (ahora \$0.1400 in / \$0.4200 out)
- **gpt-oss-20b** vía **OpenRouter** — +150.0% (ahora \$0.0750 in / \$0.3000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Sail Research (sail-research/fp4)** — +150.0% (ahora \$0.0500 in / \$0.1000 out)
- **qwen3.5-9b** vía **OpenRouter** — +50.9% (ahora \$0.1190 in / \$0.1750 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → OpenInference (open-inference/fp4)** — +50.0% (ahora \$0.0700 in / \$1.2000 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
