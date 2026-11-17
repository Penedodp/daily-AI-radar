# Daily AI Radar — 2026-11-17

> Generado 17/11/2026 17:39 WET · **751 modelos únicos** · **1415 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **349 endpoints de 35 modelos OpenRouter monitorizados** · **79 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 79 modelos con benchmark propio, 325 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_121 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 427 |
| cheaperinference | `ok` | 351 |
| together | `ok` | 193 |
| novita | `ok` | 103 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 156 |
| openrouter_routes | `ok` | 349 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling-2-small** | 8.7/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **CheaperInference** | $0.00382 | $0.0910 | $0.1820 | 8.6/10 | 82.9 |

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
| **qwen3.8-27b** | **CheaperInference** | $0.00226 | $0.0350 | $0.1700 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **76.4%** |
| **llama-3.3-70b-instruct** | **Novita AI** | $0.00702 | $0.1350 | $0.4000 | OpenRouter ($0.02765) | **74.6%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **glm-5.2** | **CheaperInference** | $0.01336 | $0.1025 | $1.5125 | OpenRouter ($0.04541) | **70.6%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **ling-3.0-flash-sante** | **CheaperInference** | $0.00141 | $0.0273 | $0.0799 | Novita AI ($0.00388) | **63.6%** |
| **deepseek-v4-flash-vision-exp** | **CheaperInference** | $0.00848 | $0.1440 | $0.5760 | OpenRouter ($0.02298) | **63.1%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00577 | $0.0800 | $0.4800 | OpenRouter ($0.01443) | **60.0%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **sonar** | **CheaperInference** | $0.01605 | $0.1625 | $1.6250 | OpenRouter ($0.03895) | **58.8%** |
| **hy4** | **CheaperInference** | $0.00980 | $0.1877 | $0.5627 | OpenRouter ($0.02178) | **55.0%** |
| **qwen3.5-9b** | **CheaperInference** | $0.00338 | $0.0800 | $0.1200 | OpenRouter ($0.00715) | **52.7%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02472 (\$0.4560 in / \$1.8400 out) · Radar Value 48.3
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.08556 (\$1.5844 in / \$6.3378 out) · Radar Value 46.8
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.6/10 · coste/tarea $0.00382 (\$0.0910 in / \$0.1820 out) · Radar Value 82.9
2. **inkling-2-small** vía **OpenRouter → PrimeIntellect (primeintellect/fp4)** — calidad 8.7/10 · coste/tarea $0.00750 (\$0.1500 in / \$0.5000 out) · Radar Value 81.1
3. **glm-5.3-flash** vía **CheaperInference** — calidad 8.2/10 · coste/tarea $0.00122 (\$0.0300 in / \$0.0534 out) · Radar Value 81.0
4. **qwen3.8-27b** vía **CheaperInference** — calidad 8.0/10 · coste/tarea $0.00207 (\$0.0350 in / \$0.1700 out) · Radar Value 78.4
5. **minimax-m3.1-flash** vía **OpenRouter** — calidad 7.9/10 · coste/tarea $0.00405 (\$0.0750 in / \$0.3000 out) · Radar Value 76.0

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-v4-flash-0731** vía **OpenRouter → Baidu (baidu/fp8)** — **-86.4%** (ahora \$0.0598 in / \$0.1795 out)
- **hy4-flash** vía **CheaperInference** — **-77.6%** (ahora \$0.0171 in / \$0.0688 out)
- **gpt-oss-20b** vía **OpenRouter** — **-76.0%** (ahora \$0.0180 in / \$0.0900 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Makora (makora/fp8)** — **-66.7%** (ahora \$0.1200 in / \$0.4000 out)
- **glm-5.3-flash:batch** vía **OpenRouter** — **-61.7%** (ahora \$0.0240 in / \$0.0690 out)
- **deepseek-v4.1-flash-1017:batch** vía **OpenRouter** — **-51.8%** (ahora \$0.0360 in / \$0.1500 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Sail Research (sail-research/fp4/us)** — **-42.9%** (ahora \$0.0400 in / \$0.0700 out)
- **glm-5.3-prime** vía **OpenRouter** — **-40.0%** (ahora \$1.6800 in / \$5.2800 out)
- **deepseek-v4-pro-0813** vía **CheaperInference** — **-38.4%** (ahora \$0.3437 in / \$1.0310 out)
- **glm-5.3:batch** vía **OpenRouter** — **-37.6%** (ahora \$0.2810 in / \$1.2500 out)
- **mistral-small-3.2-24b-instruct** vía **OpenRouter** — **-33.3%** (ahora \$0.0750 in / \$0.2000 out)
- **gpt-5.6-terra** vía **CheaperInference** — **-31.5%** (ahora \$0.8000 in / \$4.8000 out)

### Subidas

- **glm-5.3-flash** vía **OpenRouter** — +537.8% (ahora \$0.1500 in / \$0.5000 out)
- **qwen3.8-27b** vía **OpenRouter → PrimeIntellect (primeintellect/fp8)** — +260.1% (ahora \$0.2080 in / \$1.4800 out)
- **deepseek-v4.1-flash** vía **OpenRouter** — +185.7% (ahora \$0.3000 in / \$1.2000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → Baidu (baidu/fp8)** — +105.8% (ahora \$0.1498 in / \$0.6046 out)
- **glm-5.3-flash** vía **OpenRouter → Morph (morph/fp8)** — +86.2% (ahora \$0.0890 in / \$0.2570 out)
- **glm-5.3-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — +66.7% (ahora \$0.0600 in / \$0.5000 out)
- **gpt-oss-120b** vía **CheaperInference** — +60.9% (ahora \$0.0837 in / \$0.4184 out)
- **deepseek-v4-flash-0731** vía **OpenRouter → StreamLake (streamlake/fp8)** — +50.0% (ahora \$0.1320 in / \$0.3960 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
