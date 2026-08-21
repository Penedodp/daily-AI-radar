# AI Price Radar

Radar diario de precios de modelos de IA.

## Qué hace la v1

- Lee el catálogo de OpenRouter.
- Normaliza precios a USD por millón de tokens.
- Calcula un coste estimado según perfiles de uso.
- Guarda un snapshot diario en `data/`.
- Compara con el snapshot anterior.
- Genera `reports/latest.md`.
- Usa `openrouter/free` opcionalmente para redactar el resumen diario.
- Se ejecuta cada día con GitHub Actions.

## Puesta en marcha

1. Crea un repositorio en GitHub y sube estos archivos.
2. Crea una API key en OpenRouter.
3. En GitHub: Settings → Secrets and variables → Actions → New repository secret.
4. Crea `OPENROUTER_API_KEY`.
5. Abre Actions → AI Price Radar → Run workflow.
6. Comprueba `reports/latest.md`.

## Próxima fase

Añadir collectors directos para proveedores/enrutadores:
- DeepSeek
- Moonshot/Kimi
- CheaperInference
- SiliconFlow
- Together
- Fireworks
- Novita

Cada collector devolverá el mismo esquema normalizado para poder comparar precios sin cambiar el motor.

## Nota

La v1 usa únicamente datos de precio para el ranking automático. No atribuye "calidad"
a un modelo sin una fuente explícita. En una fase posterior se puede añadir un fichero
de benchmarks/ratings para calcular una puntuación calidad/precio.
