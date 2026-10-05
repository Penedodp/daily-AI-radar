# Daily AI Radar — 2026-10-05

> Generado 05/10/2026 17:05 WEST · **621 modelos únicos** · **1123 rutas/precios** · **4 proveedores de precios** · **2 benchmarks activos** · **283 endpoints de 35 modelos OpenRouter monitorizados** · **74 modelos con benchmark**.

_Coste estimado a partir de un perfil de tokens fijo (ver sección de Coding: 30K entrada + 6K salida). Es una estimación, no el coste real de tu carga de trabajo._

_Cobertura de benchmark: 74 modelos con benchmark propio, 246 endpoints heredan ese score de su modelo, 0 endpoints benchmarkeados de forma específica (0 es lo esperado hoy — ver Metodología)._

_8 ruta(s) duplicada(s) exacta(s) detectada(s) y eliminada(s) antes de publicar._

_117 ruta(s) con precio `unknown` (0/0 sin señal explícita de gratis) — no entran en ningún ranking por coste._

## 📡 Fuentes

| Fuente | Estado | Registros |
|---|---|---:|
| openrouter | `ok` | 458 |
| cheaperinference | `ok` | 91 |
| together | `ok` | 187 |
| novita | `ok` | 121 |
| aider_polyglot | `ok` | 68 |
| lmarena_webdev | `ok` | 137 |
| openrouter_routes | `ok` | 283 |

## 🆓 Mejor opción gratuita puntuada

| Uso | Fuente | Modelo | Calidad | Proveedor/ruta | $/M input | $/M output |
|---|---|---|---:|---|---:|---:|
| 💻 Coding | LMArena WebDev Arena | **qwen3.8-27b** | 8.0/10 | OpenRouter | $0.0000 | $0.0000 |

## 💰 Mejor relación calidad/precio (por fuente de benchmark)

| Uso | Fuente | Modelo | Proveedor/ruta | Coste estimado | $/M input | $/M output | Calidad | Radar Value** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 💻 Coding | Aider Polyglot Leaderboard | **deepseek-r1-0528** | **OpenRouter** | $0.02790 | $0.5000 | $2.1500 | 7.1/10 | 56.9 |
| 💻 Coding | LMArena WebDev Arena | **glm-5.3-flash** | **OpenRouter → DeepInfra (deepinfra/fp4)** | $0.00375 | $0.0750 | $0.2500 | 8.3/10 | 80.1 |

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
| **qwen3-vl-32b-instruct** | **OpenRouter** | $0.00612 | $0.1040 | $0.4160 | Together AI ($0.02612) | **76.6%** |
| **ling-3.0-flash-vl** | **OpenRouter** | $0.00109 | $0.0210 | $0.0616 | Novita AI ($0.00388) | **72.0%** |
| **qwen2.5-vl-72b-instruct** | **OpenRouter** | $0.03248 | $0.8000 | $1.0000 | Together AI ($0.11614) | **72.0%** |
| **mistral-nemo** | **OpenRouter** | $0.00081 | $0.0190 | $0.0300 | Novita AI ($0.00242) | **66.4%** |
| **ling-3.0-flash** | **OpenRouter** | $0.00110 | $0.0210 | $0.0630 | Novita AI ($0.00313) | **65.0%** |
| **llama-3.2-1b-instruct** | **Novita AI** | $0.00078 | $0.0200 | $0.0200 | OpenRouter ($0.00221) | **64.7%** |
| **gpt-5.6-terra** | **CheaperInference** | $0.05774 | $0.8000 | $4.8000 | OpenRouter ($0.14434) | **60.0%** |
| **qwen3-max** | **OpenRouter** | $0.05111 | $0.7800 | $3.9000 | Novita AI ($0.12430) | **58.9%** |
| **mistral-small-24b-instruct-2501** | **OpenRouter** | $0.00215 | $0.0500 | $0.0800 | Together AI ($0.00522) | **58.9%** |
| **gpt-5.6-luna** | **CheaperInference** | $0.00600 | $0.0831 | $0.4988 | OpenRouter ($0.01443) | **58.4%** |
| **deepseek-v4-pro** | **OpenRouter** | $0.00952 | $0.2088 | $0.4176 | CheaperInference ($0.02241) | **57.5%** |
| **llama-3.1-8b-instruct** | **Novita AI** | $0.00098 | $0.0200 | $0.0500 | OpenRouter ($0.00215) | **54.4%** |
| **deepseek-v4-flash-vision-exp** | **OpenRouter** | $0.01126 | $0.2156 | $0.6468 | Novita AI ($0.02298) | **51.0%** |
| **gpt-oss-20b** | **OpenRouter** | $0.00118 | $0.0180 | $0.0900 | Novita AI ($0.00229) | **48.5%** |
| **aion-3.0-mini** | **CheaperInference** | $0.01755 | $0.3850 | $0.7700 | OpenRouter ($0.03191) | **45.0%** |

## 🏆 Top 5 de pago por calidad/precio (por fuente)

### 💻 Coding · Aider Polyglot Leaderboard
1. **deepseek-r1-0528** vía **OpenRouter** — calidad 7.1/10 · coste/tarea $0.02790 (\$0.5000 in / \$2.1500 out) · Radar Value 56.9
2. **o4-mini-high** vía **OpenRouter** — calidad 7.2/10 · coste/tarea $0.05940 (\$1.1000 in / \$4.4000 out) · Radar Value 48.7
3. **kimi-k2** vía **OpenRouter** — calidad 5.9/10 · coste/tarea $0.03090 (\$0.5700 in / \$2.3000 out) · Radar Value 46.4
4. **deepseek-r1** vía **OpenRouter** — calidad 5.7/10 · coste/tarea $0.03600 (\$0.7000 in / \$2.5000 out) · Radar Value 43.5
5. **o3** vía **OpenRouter** — calidad 7.7/10 · coste/tarea $0.10800 (\$2.0000 in / \$8.0000 out) · Radar Value 43.3

### 💻 Coding · LMArena WebDev Arena
1. **glm-5.3-flash** vía **OpenRouter → DeepInfra (deepinfra/fp4)** — calidad 8.3/10 · coste/tarea $0.00375 (\$0.0750 in / \$0.2500 out) · Radar Value 80.1
2. **mimo-v2.6-pro** vía **CheaperInference** — calidad 8.4/10 · coste/tarea $0.01536 (\$0.3658 in / \$0.7316 out) · Radar Value 73.5
3. **glm-5.3-flashx** vía **OpenRouter** — calidad 8.3/10 · coste/tarea $0.01860 (\$0.3700 in / \$1.2500 out) · Radar Value 70.9
4. **qwen3.8-27b** vía **OpenRouter → Darkbloom (darkbloom/fp4)** — calidad 8.0/10 · coste/tarea $0.01470 (\$0.0500 in / \$2.2000 out) · Radar Value 70.3
5. **hy3** vía **OpenRouter** — calidad 7.0/10 · coste/tarea $0.00445 (\$0.0825 in / \$0.3300 out) · Radar Value 67.1

## 🔥 Bajadas reales de precio (vs ayer)

- **glm-5.3** vía **OpenRouter** — **-96.4%** (ahora \$0.0500 in / \$7.0000 out)
- **deepseek-v4-pro-0813** vía **OpenRouter** — **-52.9%** (ahora \$0.4000 in / \$5.0000 out)
- **deepseek-v4-pro-0813** vía **OpenRouter → Wafer** — **-52.9%** (ahora \$0.4000 in / \$5.0000 out)
- **gpt-5.6-sol-pro** vía **OpenRouter** — **-50.0%** (ahora \$2.0000 in / \$10.0000 out)
- **deepseek-v4.1-flash** vía **OpenRouter → Alibaba** — **-50.0%** (ahora \$0.1500 in / \$0.6000 out)
- **deepseek-v4-flash-0731** vía **OpenRouter → Alibaba** — **-50.0%** (ahora \$0.1760 in / \$0.5280 out)
- **deepseek-v4-pro-0813** vía **OpenRouter → Alibaba** — **-48.2%** (ahora \$0.5808 in / \$1.7424 out)
- **qwen3-coder-next** vía **CheaperInference** — **-42.5%** (ahora \$0.1984 in / \$0.9918 out)
- **glm-5.3-flash** vía **OpenRouter → Wafer** — **-40.0%** (ahora \$0.0600 in / \$0.6500 out)
- **hy3** vía **OpenRouter** — **-37.5%** (ahora \$0.0825 in / \$0.3300 out)
- **hy3** vía **OpenRouter → Tencent (tencent/fp8)** — **-37.5%** (ahora \$0.0825 in / \$0.3300 out)
- **glm-4.7** vía **CheaperInference** — **-35.3%** (ahora \$0.3300 in / \$1.2100 out)

### Subidas

- **deepseek-v4.1-flash** vía **OpenRouter** — +9900.0% (ahora \$0.3000 in / \$1.2000 out)
- **qwen3-coder-30b-a3b-instruct** vía **CheaperInference** — +703.6% (ahora \$0.2925 in / \$1.4625 out)
- **glm-5.2** vía **OpenRouter** — +358.5% (ahora \$0.0192 in / \$16.0000 out)
- **deepseek-v4-flash-0731** vía **CheaperInference** — +331.4% (ahora \$0.1320 in / \$0.3960 out)
- **deepseek-v4.1-flash** vía **OpenRouter → InferenceNet (inference-net)** — +250.0% (ahora \$0.0700 in / \$0.3000 out)
- **glm-5.3** vía **OpenRouter → Relace** — +172.7% (ahora \$0.0300 in / \$12.0000 out)
- **glm** vía **OpenRouter** — +140.0% (ahora \$0.0300 in / \$12.0000 out)
- **glm-5.3** vía **OpenRouter → InferenceNet (inference-net)** — +140.0% (ahora \$0.1200 in / \$4.4000 out)

## 🧪 Notas

- **Gratis** y **pago** se rankean por separado; los modelos `$0` ya no dominan el ranking de compra.
- Una diferencia entre proveedores se llama **ahorro entre rutas**, no descuento.
- **Bajada/descuento** solo se marca cuando el mismo proveedor/ruta baja frente al histórico — un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.
- Los proveedores opcionales sin API key simplemente se omiten; el workflow sigue funcionando.
- El resumen IA redacta la conclusión, pero no calcula precios ni rankings.
- La calidad de **coding** se obtiene automáticamente de dos fuentes públicas sin API key, **rankeadas siempre por separado**: **Aider Polyglot Leaderboard** (test de corrección fijo) y **LMArena WebDev Arena** (ranking Elo por voto humano, cobertura mucho más amplia y rápida para modelos recién publicados). No requiere mantenimiento manual. **Agentic/razonamiento/general** aún no tienen una fuente de benchmark automatizada igual de fiable — se añadirán cuando se identifique una.
- Un precio en `$0.0000` en las tablas siempre corresponde a `pricing_status = free`; un precio desconocido nunca se muestra como `$0.0000`, se excluye del ranking y aparece como `—` en el explorador.

## 🤖 Estrategia recomendada para hoy

Informe diario 2026-10-05. Todos los proveedores opcionales monitorizados (OpenRouter, CheaperInference, Together, Novita) están OK.

1) Mejor opción GRATIS: qwen3.8-27b:free por OpenRouter. En LMArena WebDev Arena tiene Elo 1591.24. En Aider Polyglot Leaderboard no aparece opción gratuita monitorizada.

2) Mejor relación calidad/precio DE PAGO:
- Coding: deepseek-r1-0528 por OpenRouter. Aider Polyglot Leaderboard: 71.4% pass rate; input 0.50 $/M, output 2.15 $/M; coste de tarea 0.0279 $.
- WebDev: glm-5.3-flash por OpenRouter → DeepInfra (fp4). LMArena WebDev Arena: Elo 1615.57; input 0.075 $/M, output 0.25 $/M; coste de tarea 0.00375 $.

3) Opción PREMIUM:
- Coding: o3 por OpenRouter. Aider Polyglot Leaderboard: 76.9% pass rate; input 2.00 $/M, output 8.00 $/M; coste de tarea 0.108 $. Justifica el coste si la calidad de código es crítica.
- WebDev: qwen3.8-max-0902 por OpenRouter. LMArena WebDev Arena: Elo 1670.01; input 2.00 $/M, output 6.00 $/M; coste de tarea 0.096 $. Justifica el coste para webdev de alta exigencia.

4) Mismo modelo por ruta/proveedor más barato:
- qwen3-vl-32b-instruct: OpenRouter 0.104/0.416 $/M frente a Together AI 0.50/1.50 $/M; ahorro 76.6% frente a la siguiente ruta.
- ling-3.0-flash-vl: OpenRouter 0.021/0.0616 $/M frente a Novita AI 0.075/0.22 $/M; ahorro 72.0%.
- gpt-5.6-terra: CheaperInference 0.80/4.80 $/M frente a OpenRouter 2.00/12.00 $/M; ahorro 60.0%.
- deepseek-v4-pro: OpenRouter 0.2088/0.4176 $/M frente a CheaperInference 0.429/1.287 $/M; ahorro 57.5%.
Estas son diferencias entre proveedores, no descuentos.

Cambios de precio del mismo proveedor/ruta: bajadas relevantes: glm-5.3 en OpenRouter, coste estimado -35.4%; deepseek-v4-pro-0813 en OpenRouter, -24.0%; gpt-5.6-sol-pro en OpenRouter, -50.0%. Subidas relevantes: qwen3-coder-30b-a3b-instruct en CheaperInference, coste estimado +615.4%; glm-5.2 en OpenRouter, +245.6%; deepseek-v4.1-flash en OpenRouter, +10.1%.

Estrategia para hoy:
- Tareas normales: qwen3.8-27b:free para webdev; si prefieres pago, glm-5.3-flash vía DeepInfra fp4.
- Coding: deepseek-r1-0528 por OpenRouter como base; usa o3 solo para cambios críticos o debugging complejo.
- Problemas difíciles: o3 para coding (Aider Polyglot) y qwen3.8-max-0902 para webdev (LMArena WebDev Arena), solo si el presupuesto lo permite.
