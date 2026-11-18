# Daily AI Radar — 2026-11-18

> Generado 18/11/2026 17:17 WET · **761 modelos únicos** · **1379 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **300 endpoints de 35 modelos OpenRouter monitorizados** · **79 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 79 modelos con benchmark propio, 309 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_120 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 435 |
| cheaperinference | `ok` | 350 |
| together | `ok` | 194 |
| novita | `ok` | 108 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 156 |
| openrouter_routes | `ok` | 300 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **inkling-2-small** | 8.7/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **CheaperInference** | $0.00398 | $0.0948 | $0.1896 | 8.6/10 | 82.8 |

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
| **qwen3.8-27b** | **CheaperInference** | $0.00291 | $0.0550 | $0.1700 | OpenRouter → Chutes (chutes/fp8) ($0.00957) | **69.6%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **deepseek-v4-flash-vision-exp** | **CheaperInference** | $0.00777 | $0.1320 | $0.5280 | OpenRouter ($0.02298) | **66.2%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00577 | $0.0800 | $0.4800 | OpenRouter ($0.01443) | **60.0%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **hy4-flash** | **CheaperInference** | $0.00093 | $0.0158 | $0.0632 | OpenRouter ($0.00206) | **55.0%** |
| **gemini-4-carbon** | **CheaperInference** | $0.05897 | $0.9000 | $4.5000 | OpenRouter ($0.13105) | **55.0%** |
| **hy4** | **CheaperInference** | $0.00980 | $0.1877 | $0.5627 | OpenRouter ($0.02178) | **55.0%** |
| **gemini-4-argon** | **CheaperInference** | $0.05897 | $0.9000 | $4.5000 | OpenRouter ($0.13105) | **55.0%** |
| **gemini-3.8-flash** | **CheaperInference** | $0.02211 | $0.3375 | $1.6875 | OpenRouter ($0.04914) | **55.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.07020 (\$1.3000 in / \$5.2000 out) · Radar Value 49.7
3. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02472 (\$0.4560 in / \$1.8400 out) · Radar Value 48.3
4. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **CheaperInference** — calidad 8.6/10 · coste/tarea $0.00398 (\$0.0948 in / \$0.1896 out) · Radar Value 82.8
2. **inkling-2-small** vía **OpenRouter → PrimeIntellect (primeintellect/fp4)** — calidad 8.7/10 · coste/tarea $0.00750 (\$0.1500 in / \$0.5000 out) · Radar Value 81.1
3. **glm-5.3-flash** vía **CheaperInference** — calidad 8.2/10 · coste/tarea $0.00129 (\$0.0324 in / \$0.0534 out) · Radar Value 81.0
4. **qwen3.8-27b** vía **CheaperInference** — calidad 8.0/10 · coste/tarea $0.00267 (\$0.0550 in / \$0.1700 out) · Radar Value 77.9
5. **minimax-m3.1-flash** vía **OpenRouter** — calidad 7.9/10 · coste/tarea $0.00405 (\$0.0750 in / \$0.3000 out) · Radar Value 76.0

## 🔥 Bajadas reales de precio (vs ayer)

- **deepseek-v4.1-flash** vía **OpenRouter** — **-83.1%** (ahora \$0.0507 in / \$0.2028 out)
- **qwen3.8-27b** vía **OpenRouter** — **-60.0%** (ahora \$0.0600 in / \$2.2000 out)
- **deepseek-v4.1-flash-1017** vía **OpenRouter → SiliconFlow (siliconflow/fp8)** — **-50.0%** (ahora \$0.1500 in / \$0.6000 out)
- **gpt-oss-120b** vía **CheaperInference** — **-37.9%** (ahora \$0.0520 in / \$0.2600 out)
- **gpt-5.6-sol** vía **CheaperInference** — **-27.9%** (ahora \$2.0000 in / \$10.0000 out)
- **arrow-2** vía **CheaperInference** — **-23.5%** (ahora \$2.6000 in / \$13.0000 out)
- **arrow-2-telos** vía **CheaperInference** — **-23.5%** (ahora \$3.9000 in / \$19.5000 out)
- **deepseek-v3.2-thinking** vía **CheaperInference** — **-23.5%** (ahora \$0.1820 in / \$0.2730 out)
- **gpt-5-fast** vía **CheaperInference** — **-23.5%** (ahora \$1.6250 in / \$13.0000 out)
- **gpt-5.1-thinking-fast** vía **CheaperInference** — **-23.5%** (ahora \$1.6250 in / \$13.0000 out)
- **gpt-5.2-fast** vía **CheaperInference** — **-23.5%** (ahora \$2.2750 in / \$18.2000 out)
- **gpt-6-sol-fast** vía **CheaperInference** — **-23.5%** (ahora \$2.6000 in / \$13.0000 out)

### Subidas

- **glm-5.3** vía **CheaperInference** — +36233.3% (ahora \$0.1090 in / \$1.1800 out)
- **kimi-k3.1-pro** vía **CheaperInference** — +826.6% (ahora \$1.3000 in / \$6.5000 out)
- **glm-5.2** vía **CheaperInference** — +363.4% (ahora \$0.4750 in / \$1.5125 out)
- **deepseek-v4.1-flash-1017** vía **CheaperInference** — +355.2% (ahora \$0.0660 in / \$0.2640 out)
- **mimo-v2.5-pro** vía **OpenRouter** — +106.9% (ahora \$0.4800 in / \$1.8000 out)
- **deepseek-v4-flash-0731** vía **CheaperInference** — +103.4% (ahora \$0.0590 in / \$0.1070 out)
- **minimax-m3.1-flash** vía **OpenRouter → Inferact vLLM (inferact-vllm/nvfp4)** — +100.0% (ahora \$0.1500 in / \$0.6000 out)
- **qwen3.8-27b** vía **OpenRouter → PrimeIntellect (primeintellect/fp8)** — +87.5% (ahora \$0.3900 in / \$2.7740 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.
