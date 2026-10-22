# Daily AI Radar — 2026-10-22

> Generado 22/10/2026 14:00 WEST · **671 modelos únicos** · **1250 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **278 endpoints de 35 modelos OpenRouter monitorizados** · **81 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 81 modelos con benchmark propio, 287 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_114 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 461 |
| cheaperinference | `ok` | 232 |
| together | `ok` | 191 |
| novita | `ok` | 97 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `cached_stale` | 147 |
| openrouter_routes | `ok` | 278 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **minimax-m3.1-flash** | 8.0/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **CheaperInference** | $0.02371 | $0.4250 | $1.8275 | 7.1/10 | 58.5 |
| 💻 Coding | LMArena WebDev Arena | **mimo-v2.6-flash** | **OpenRouter → Darkbloom (darkbloom/fp4)** | $0.00468 | $0.1000 | $0.2800 | 8.5/10 | 81.3 |

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
| **qwen3-coder-30b-a3b-instruct** | **OpenRouter** | $0.00412 | $0.0700 | $0.2800 | CheaperInference ($0.01917) | **78.5%** |
| **nemotron-3-super-120b-a12b** | **CheaperInference** | $0.00596 | $0.0975 | $0.4225 | OpenRouter ($0.02564) | **76.8%** |
| **qwen3-coder** | **OpenRouter** | $0.01633 | $0.3000 | $1.0000 | CheaperInference ($0.06389) | **74.4%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **deepseek-v3.1** | **CheaperInference** | $0.00935 | $0.1625 | $0.6175 | Together AI ($0.03068) | **69.5%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **qwen3-235b-a22b-thinking-2507** | **CheaperInference** | $0.01476 | $0.1495 | $1.4950 | OpenRouter ($0.03779) | **60.9%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00577 | $0.0800 | $0.4800 | OpenRouter ($0.01443) | **60.0%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05864 | $0.8125 | $4.8751 | OpenRouter ($0.14434) | **59.4%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **gpt-5.6-sol-pro** | **CheaperInference** | $0.11139 | $1.7000 | $8.5000 | OpenRouter ($0.26210) | **57.5%** |
| **gpt-oss-20b** | **OpenRouter** | $0.00118 | $0.0180 | $0.0900 | CheaperInference ($0.00277) | **57.4%** |
| **llama-3.1-8b-instruct** | **Novita AI** | $0.00098 | $0.0200 | $0.0500 | OpenRouter ($0.00215) | **54.4%** |
| **ling-3.0-flash-fin** | **CheaperInference** | $0.00185 | $0.0357 | $0.1046 | Novita AI ($0.00388) | **52.4%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **CheaperInference** — calidad 7.1/10 · coste/tarea $0.02371 (\$0.4250 in / \$1.8275 out) · Radar Value 58.5
2. **o3** vía **CheaperInference** — calidad 7.7/10 · coste/tarea $0.07020 (\$1.3000 in / \$5.2000 out) · Radar Value 49.7
3. **o4-mini-high** vía **OpenRouter** — calidad 7.2/10 · coste/tarea $0.05940 (\$1.1000 in / \$4.4000 out) · Radar Value 48.7
4. **kimi-k2** vía **CheaperInference** — calidad 5.9/10 · coste/tarea $0.02627 (\$0.4845 in / \$1.9550 out) · Radar Value 47.8
5. **deepseek-r1** vía **CheaperInference** — calidad 5.7/10 · coste/tarea $0.04738 (\$0.8775 in / \$3.5100 out) · Radar Value 40.8

### 💻 Coding · LMArena WebDev Arena
1. **mimo-v2.6-flash** vía **OpenRouter → Darkbloom (darkbloom/fp4)** — calidad 8.5/10 · coste/tarea $0.00468 (\$0.1000 in / \$0.2800 out) · Radar Value 81.3
2. **glm-5.3-flash** vía **OpenRouter** — calidad 8.2/10 · coste/tarea $0.00135 (\$0.0052 in / \$0.1985 out) · Radar Value 80.9
3. **minimax-m3.1-flash** vía **Novita AI** — calidad 8.0/10 · coste/tarea $0.00810 (\$0.1500 in / \$0.6000 out) · Radar Value 74.2
4. **qwen3.8-27b** vía **OpenRouter → Chutes (chutes/fp8)** — calidad 8.0/10 · coste/tarea $0.00867 (\$0.0390 in / \$1.2500 out) · Radar Value 73.9
5. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01518 (\$0.3615 in / \$0.7230 out) · Radar Value 73.6

## 🔥 Bajadas reales de precio (vs ayer)

- **glm-5.3-flash** vía **OpenRouter** — **-96.5%** (ahora \$0.0052 in / \$0.1985 out)
- **glm-5.3-flash** vía **OpenRouter → Relace** — **-93.1%** (ahora \$0.0052 in / \$0.1985 out)
- **glm-flash** vía **OpenRouter** — **-89.9%** (ahora \$0.0052 in / \$0.1985 out)
- **glm-5.3-flash** vía **OpenRouter → OpenInference (open-inference/fp4)** — **-89.9%** (ahora \$0.0052 in / \$0.1985 out)
- **glm-5.3-flash** vía **OpenRouter → Morph (morph/fp8)** — **-81.8%** (ahora \$0.1500 in / \$0.6500 out)
- **deepseek-v4-pro-0813** vía **OpenRouter → Sail Research (sail-research/us)** — **-50.0%** (ahora \$0.4500 in / \$0.8000 out)
- **deepseek-v4-pro-0813** vía **OpenRouter → Sail Research (sail-research/fp4)** — **-50.0%** (ahora \$0.4500 in / \$0.8000 out)
- **glm-5.3-flash** vía **OpenRouter → StreamLake (streamlake/fp8)** — **-41.1%** (ahora \$0.0435 in / \$0.1450 out)
- **glm-5.3-flash** vía **OpenRouter → NextBit (nextbit/fp4)** — **-37.5%** (ahora \$0.1500 in / \$0.7500 out)
- **glm-5.3-flash** vía **CheaperInference** — **-35.3%** (ahora \$0.0825 in / \$0.2750 out)
- **glm-5.3-flash** vía **OpenRouter → Reka** — **-33.3%** (ahora \$0.0800 in / \$1.6000 out)
- **qwen3.6-plus** vía **CheaperInference** — **-23.5%** (ahora \$0.3250 in / \$1.9500 out)

### Subidas

- **deepseek-pro** vía **OpenRouter** — +1088.4% (ahora \$0.2020 in / \$8.0000 out)
- **deepseek-v4.1-flash** vía **OpenRouter** — +513.5% (ahora \$0.3000 in / \$1.2000 out)
- **nemotron-3-super-120b-a12b** vía **OpenRouter** — +433.3% (ahora \$0.3000 in / \$2.4000 out)
- **glm-5.3** vía **OpenRouter → Baidu (baidu/fp8)** — +100.2% (ahora \$1.3986 in / \$4.3956 out)
- **glm-5.3** vía **OpenRouter → Sail Research (sail-research/us)** — +100.0% (ahora \$0.5000 in / \$2.0000 out)
- **glm-5.3** vía **OpenRouter → Sail Research (sail-research/fp8)** — +100.0% (ahora \$0.5000 in / \$2.0000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Sail Research (sail-research/fp4/us)** — +66.7% (ahora \$0.0900 in / \$0.2500 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Sail Research (sail-research/fp4)** — +66.7% (ahora \$0.0900 in / \$0.2500 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.

## 🤖 Estrategia recomendada para hoy

## Informe diario de costes — 22/10/2026

_Precios en USD por millón de tokens; “coste de tarea” es la estimación ponderada del monitor._

### 1) Mejor opción GRATIS
**MiniMax-M3.1-Flash**, mediante la ruta OpenRouter `:free`, cuesta **$0** en entrada y salida. En **LMArena WebDev Arena** ([fuente exacta](https://lmarena.ai/leaderboard/webdev), captura del 21/10) registra **1587,5 Elo**. No se identificó ningún candidato gratuito en **Aider Polyglot**. LMArena está en estado `cached_stale`, por lo que conviene validar resultados críticos.

### 2) Mejor relación calidad/precio DE PAGO
- **Coding — Aider Polyglot:** **DeepSeek-R1-0528** vía CheaperInference, a **$0,425/$1,8275**, con coste estimado de **$0,023715/tarea** y **71,4% pass rate**. Fuente exacta: [Aider Polyglot Leaderboard](https://aider.chat/docs/leaderboards/).
- **WebDev — LMArena:** **MiMo-V2.6-Flash**, vía OpenRouter → Darkbloom `darkbloom/fp4`, a **$0,10/$0,28**, con **$0,00468/tarea** y **1633,6 Elo**. Fuente exacta: [LMArena WebDev Arena](https://lmarena.ai/leaderboard/webdev).

Los porcentajes de Aider y los ELO de WebDev son escalas distintas y no deben compararse entre sí.

### 3) Opción PREMIUM
**Qwen3.8-Max-0902** vía OpenRouter alcanza **1674,3 Elo** —fuente: LMArena WebDev Arena— por **$2/$6** y **$0,096/tarea**. Supera a MiMo en aproximadamente **40,7 Elo**, pero cuesta unas **20,5 veces** el coste de tarea: solo se justifica en WebDev crítico.

En coding, **o3** logra **76,9% pass rate** —fuente: Aider Polyglot—; sin embargo, su versión en CheaperInference conserva esa calidad por menos, por lo que la prima de OpenRouter no está justificada.

### 4) Mismo modelo por proveedor/ruta más barata
- **o3:** CheaperInference frente a OpenRouter, **35% menos coste de tarea**.
- **qwen3-coder-30b-a3b-instruct:** OpenRouter frente a CheaperInference, **78,5% menos coste ponderado**.
- **qwen-mt-plus:** Novita frente a CheaperInference, **84,4% menos**.
- **deepseek-v3.1:** CheaperInference frente a Together AI, **69,5% menos**.

Son diferencias entre proveedores, no bajadas históricas; para estos modelos no hay puntuación de calidad asociada.

### Cambios históricos
**Bajada real de la misma ruta OpenRouter:** `glm-5.3-flash`_DIRECT registra **−96,5% en entrada, −60,3% en salida y −81,8% ponderado**. También bajó un 12,2% `qwen3-235b-a22b-thinking-2507` en CheaperInference. En sentido contrario, evitan nuevas rutas de `deepseek-pro` y `deepseek-v4.1-flash` en OpenRouter: sus costes ponderados submarán.

### Estrategia para hoy
- **Normales:** MiniMax gratis para WebDev de bajo riesgo; GLM-5.3-Flash para trabajo web rutinario.
- **Coding:** DeepSeek-R1-0528 por defecto; o3 en CheaperInference para casos complejos.
- **Difíciles:** o3 en CheaperInference; Qwen3.8-Max solo cuando el resultado WebDev valere el coste premium.

OpenRouter, CheaperInference, Together y Novita están configurados y operational; las categorías agentic, reasoning y general no aportan recomendaciones.
