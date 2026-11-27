# Daily AI Radar — 2026-11-27

> Generado 27/11/2026 18:14 WET · **727 modelos únicos** · **1221 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **219 endpoints de 35 modelos OpenRouter monitorizados** · **78 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 78 modelos con benchmark propio, 335 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_115 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 433 |
| cheaperinference | `ok` | 333 |
| together | `ok` | 196 |
| novita | `ok` | 46 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 161 |
| openrouter_routes | `ok` | 219 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| — | — | Ningún modelo gratuito puntuado todavía | — | — | — | — |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **OpenRouter** | $0.03085 | $0.5710 | $2.2860 | 7.1/10 | 55.8 |
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
| **deepseek-r1-0528** | **OpenRouter** | $0.03363 | $0.5710 | $2.2860 | Together AI ($0.14341) | **76.5%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **ling-3.0-flash-sante** | **CheaperInference** | $0.00141 | $0.0273 | $0.0799 | Novita AI ($0.00388) | **63.6%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00577 | $0.0800 | $0.4800 | OpenRouter ($0.01443) | **60.0%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **llama-4-maverick** | **CheaperInference** | $0.00724 | $0.1352 | $0.4316 | OpenRouter ($0.01795) | **59.7%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **sonar** | **CheaperInference** | $0.01605 | $0.1625 | $1.6250 | OpenRouter ($0.03895) | **58.8%** |
| **qwen3.8-27b** | **CheaperInference** | $0.00408 | $0.0750 | $0.2500 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **57.3%** |
| **hy4-flash** | **CheaperInference** | $0.00093 | $0.0158 | $0.0632 | OpenRouter ($0.00206) | **55.0%** |
| **gemini-4-carbon** | **CheaperInference** | $0.05897 | $0.9000 | $4.5000 | OpenRouter ($0.13105) | **55.0%** |
| **hy4** | **CheaperInference** | $0.00980 | $0.1877 | $0.5627 | OpenRouter ($0.02178) | **55.0%** |
| **gemini-4-argon** | **CheaperInference** | $0.05897 | $0.9000 | $4.5000 | OpenRouter ($0.13105) | **55.0%** |
| **gemini-3.8-flash** | **CheaperInference** | $0.02211 | $0.3375 | $1.6875 | OpenRouter ($0.04914) | **55.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **OpenRouter** — calidad 7.1/10 · coste/tarea $0.03085 (\$0.5710 in / \$2.2860 out) · Radar Value 55.8
2. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02256 (\$0.4161 in / \$1.6790 out) · Radar Value 49.0
3. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.08682 (\$1.6077 in / \$6.4308 out) · Radar Value 46.5
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **inkling-2-small** vía **OpenRouter → PrimeIntellect (primeintellect/flex)** — calidad 8.7/10 · coste/tarea $0.00375 (\$0.0750 in / \$0.2500 out) · Radar Value 83.9
2. **mimo-v2.6-flash** vía **OpenRouter → Darkbloom (darkbloom/fp4)** — calidad 8.6/10 · coste/tarea $0.00468 (\$0.1000 in / \$0.2800 out) · Radar Value 82.2
3. **glm-5.3-flash** vía **CheaperInference** — calidad 8.3/10 · coste/tarea $0.00118 (\$0.0281 in / \$0.0565 out) · Radar Value 82.0
4. **hy4** vía **CheaperInference** — calidad 8.8/10 · coste/tarea $0.00901 (\$0.1877 in / \$0.5627 out) · Radar Value 81.0
5. **qwen3.8-27b** vía **CheaperInference** — calidad 8.0/10 · coste/tarea $0.00375 (\$0.0750 in / \$0.2500 out) · Radar Value 77.2

## 🔥 Bajadas reales de precio (vs ayer)

- **gemma-3-27b-it** vía **OpenRouter** — **-64.4%** (ahora \$0.0800 in / \$0.1600 out)
- **deepseek-v4-flash-vision-exp** vía **OpenRouter** — **-51.0%** (ahora \$0.2156 in / \$0.6468 out)
- **qwen3.8-27b** vía **OpenRouter → PrimeIntellect (primeintellect/fp8)** — **-46.7%** (ahora \$0.2400 in / \$2.1960 out)
- **glm-5.3-flash** vía **OpenRouter → Inceptron (inceptron/fp8)** — **-40.0%** (ahora \$0.1500 in / \$0.3000 out)
- **inkling-2-mini** vía **OpenRouter → Io Net (io-net/nvfp4)** — **-33.3%** (ahora \$0.0800 in / \$0.3500 out)
- **beam** vía **CheaperInference** — **-27.5%** (ahora \$0.0855 in / \$0.2564 out)
- **arrow-2-telos** vía **CheaperInference** — **-23.5%** (ahora \$3.9000 in / \$19.5000 out)
- **codestral** vía **CheaperInference** — **-23.5%** (ahora \$0.1950 in / \$0.5850 out)
- **fugu-max** vía **CheaperInference** — **-23.5%** (ahora \$1.3000 in / \$3.9000 out)
- **fugu-ultra-v2** vía **CheaperInference** — **-23.5%** (ahora \$3.2500 in / \$19.5000 out)
- **gemini-2.5-pro** vía **CheaperInference** — **-23.5%** (ahora \$0.8125 in / \$6.5000 out)
- **gemini-4-neon-fast** vía **CheaperInference** — **-23.5%** (ahora \$3.5100 in / \$17.5500 out)

### Subidas

- **gemma-3-4b-it** vía **OpenRouter** — +100.0% (ahora \$0.0500 in / \$0.1000 out)
- **deepseek-v4.1-flash-1017-fast** vía **CheaperInference** — +30.8% (ahora \$0.5100 in / \$2.0400 out)
- **glm-5v-turbo** vía **CheaperInference** — +30.8% (ahora \$1.0200 in / \$3.4000 out)
- **gpt-6-sol** vía **CheaperInference** — +30.8% (ahora \$1.7000 in / \$8.5000 out)
- **inkling-small** vía **CheaperInference** — +30.8% (ahora \$0.2550 in / \$1.0200 out)
- **kimi-k3.1-pro-highspeed** vía **CheaperInference** — +30.8% (ahora \$3.4000 in / \$17.0000 out)
- **ling-3.0-flash-fin** vía **CheaperInference** — +30.8% (ahora \$0.0357 in / \$0.1046 out)
- **llama-4-scout** vía **CheaperInference** — +30.8% (ahora \$0.0850 in / \$0.2550 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
