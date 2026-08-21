from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
from statistics import mean

from providers.openrouter import fetch_models
from filters import is_relevant_text_model
from quality import match_quality_profile
from scoring import (
    weighted_daily_cost,
    costs_by_task,
    price_change,
    value_score,
)
from report_ai import generate_summary

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_LABELS = {
    "coding": "💻 Coding",
    "agentic": "🤖 Agentic coding",
    "reasoning": "🧠 Razonamiento",
    "general": "⚡ General",
}

def load_json(path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))

def load_history(data_dir, today, limit=30):
    snapshots = []
    for path in sorted(data_dir.glob("*.json"), reverse=True):
        if path.stem == today:
            continue
        data = load_json(path, {})
        if data:
            snapshots.append(data)
        if len(snapshots) >= limit:
            break
    return snapshots

def model_map(snapshot):
    return {
        r["model_id"]: r
        for r in snapshot.get("models", [])
        if r.get("model_id")
    }

def compact_row(row, category=None):
    d = {
        "model": row["model_id"],
        "cost": round(
            row["costs_by_task"].get(category, row["weighted_cost"])
            if category
            else row["weighted_cost"],
            6,
        ),
        "free": row["input_usd_per_million"] == 0 and row["output_usd_per_million"] == 0,
    }
    if category and row.get("quality"):
        d["quality_score"] = row["quality"]["scores"].get(category)
        d["value_score"] = row["value_scores"].get(category)
        d["quality_confidence"] = row["quality"].get("confidence")
    if row.get("change_pct") is not None:
        d["change_pct"] = round(row["change_pct"], 1)
    return d

def build_recommendations(models, config):
    only_scored = config.get("recommendation_candidates_only_scored", True)
    recs = {}

    for category in CATEGORY_LABELS:
        candidates = []
        for row in models:
            q = row.get("quality")
            score = q.get("scores", {}).get(category) if q else None
            if only_scored and score is None:
                continue
            if score is None:
                continue
            candidates.append(row)

        by_value = sorted(
            candidates,
            key=lambda r: (
                r["value_scores"].get(category) or -1,
                r["quality"]["scores"].get(category, 0),
            ),
            reverse=True,
        )
        free = [
            r for r in candidates
            if r["input_usd_per_million"] == 0
            and r["output_usd_per_million"] == 0
        ]
        free = sorted(
            free,
            key=lambda r: r["quality"]["scores"].get(category, 0),
            reverse=True,
        )
        by_quality = sorted(
            candidates,
            key=lambda r: r["quality"]["scores"].get(category, 0),
            reverse=True,
        )

        recs[category] = {
            "best_value": compact_row(by_value[0], category) if by_value else None,
            "best_free": compact_row(free[0], category) if free else None,
            "best_quality": compact_row(by_quality[0], category) if by_quality else None,
            "top_value": [compact_row(r, category) for r in by_value[:5]],
        }
    return recs

def main():
    config = load_json(ROOT / "config.json", {})
    quality_config = load_json(ROOT / "quality_profiles.json", {"rules": []})

    tz = ZoneInfo(config.get("timezone", "Europe/Lisbon"))
    now = datetime.now(tz)
    day = now.date().isoformat()

    data_dir = ROOT / "data"
    reports_dir = ROOT / "reports"
    data_dir.mkdir(exist_ok=True)
    reports_dir.mkdir(exist_ok=True)

    history = load_history(data_dir, day)
    previous = history[0] if history else None
    previous_map = model_map(previous or {})
    history_maps = [model_map(s) for s in history]

    task_profiles = config.get("task_profiles", {})
    anchor = config.get("value_cost_anchor_usd", 0.05)

    models = []
    filtered_count = 0

    for row in fetch_models():
        relevant, _reason = is_relevant_text_model(row, config)
        if not relevant:
            filtered_count += 1
            continue

        row["costs_by_task"] = costs_by_task(row, task_profiles)
        row["weighted_cost"] = weighted_daily_cost(row, task_profiles)

        old = previous_map.get(row["model_id"])
        old_cost = old.get("weighted_cost") if old else None
        row["change_pct"] = price_change(row["weighted_cost"], old_cost)

        past_costs = []
        for hmap in history_maps[:7]:
            old_row = hmap.get(row["model_id"])
            if old_row and old_row.get("weighted_cost") is not None:
                past_costs.append(old_row["weighted_cost"])

        row["avg_7d_cost"] = mean(past_costs) if past_costs else None
        row["historical_min_cost"] = min(past_costs) if past_costs else None
        row["vs_avg_7d_pct"] = price_change(
            row["weighted_cost"],
            row["avg_7d_cost"],
        )

        row["quality"] = match_quality_profile(
            row["model_id"],
            quality_config,
        )
        row["value_scores"] = {}
        if row["quality"]:
            for category in CATEGORY_LABELS:
                q = row["quality"]["scores"].get(category)
                row["value_scores"][category] = value_score(
                    q,
                    row["costs_by_task"].get(category, row["weighted_cost"]),
                    anchor,
                )

        models.append(row)

    models.sort(key=lambda x: x["weighted_cost"])

    has_history = bool(previous)
    drop_threshold = -abs(config.get("discount_threshold_pct", 10))
    up_threshold = abs(config.get("price_increase_threshold_pct", 10))

    drops = []
    increases = []
    new_free = []

    if has_history:
        for row in models:
            ch = row.get("change_pct")
            if ch is not None and ch <= drop_threshold:
                drops.append(compact_row(row))
            if ch is not None and ch >= up_threshold:
                increases.append(compact_row(row))

            if (
                row["model_id"] not in previous_map
                and row["input_usd_per_million"] == 0
                and row["output_usd_per_million"] == 0
            ):
                new_free.append(compact_row(row))

    drops.sort(key=lambda x: x.get("change_pct", 0))
    increases.sort(key=lambda x: x.get("change_pct", 0), reverse=True)

    recommendations = build_recommendations(models, config)

    snapshot = {
        "generated_at": now.isoformat(),
        "stats": {
            "models_kept": len(models),
            "models_filtered": filtered_count,
            "quality_scored": sum(1 for r in models if r.get("quality")),
            "history_days_loaded": len(history),
        },
        "changes": {
            "drops": drops,
            "increases": increases,
            "new_free": new_free,
        },
        "recommendations": recommendations,
        "models": models,
    }

    # Guardamos primero los datos deterministas.
    (data_dir / f"{day}.json").write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    lines = [
        f"# AI Price Radar — {day}",
        "",
        f"> Analizados **{len(models)}** modelos de texto; "
        f"filtrados **{filtered_count}** no relevantes. "
        f"Con score de calidad: **{snapshot['stats']['quality_scored']}**.",
        "",
        "## 🎯 Recomendación por tipo de uso",
        "",
        "| Uso | Mejor calidad/precio | Coste/tarea | Calidad* | Value | Mejor gratis |",
        "|---|---|---:|---:|---:|---|",
    ]

    for category, label in CATEGORY_LABELS.items():
        rec = recommendations.get(category, {})
        best = rec.get("best_value")
        free = rec.get("best_free")
        if best:
            lines.append(
                f"| {label} | **{best['model']}** | "
                f"${best['cost']:.5f} | {best.get('quality_score', '—')} | "
                f"{best.get('value_score', '—')} | "
                f"{('**' + free['model'] + '**') if free else '—'} |"
            )
        else:
            lines.append(f"| {label} | — | — | — | — | — |")

    lines += [
        "",
        "\\* *Calidad = score heurístico curado (0–10), no benchmark oficial.*",
        "",
        "## 🏆 Top calidad/precio",
        "",
    ]

    for category, label in CATEGORY_LABELS.items():
        lines.append(f"### {label}")
        top = recommendations.get(category, {}).get("top_value", [])
        if not top:
            lines.append("- Sin modelos puntuados para esta categoría.")
        for i, r in enumerate(top[:5], 1):
            free_txt = " · **GRATIS**" if r["free"] else ""
            lines.append(
                f"{i}. **{r['model']}** — value **{r.get('value_score', '—')}**, "
                f"calidad {r.get('quality_score', '—')}/10, "
                f"coste/tarea ${r['cost']:.5f}{free_txt}"
            )
        lines.append("")

    lines += ["## 🔥 Cambios de precio", ""]
    if not has_history:
        lines.append(
            "Todavía no hay un día anterior para comparar. "
            "A partir de la próxima ejecución podremos detectar bajadas y subidas."
        )
    else:
        if drops:
            lines.append("### Bajadas destacadas")
            for r in drops[:10]:
                lines.append(
                    f"- **{r['model']}** — {r['change_pct']:.1f}% "
                    f"(coste perfil ${r['cost']:.5f})"
                )
        else:
            lines.append("- No se detectaron bajadas ≥ al umbral configurado.")

        if new_free:
            lines += ["", "### Nuevos modelos gratuitos"]
            for r in new_free[:10]:
                lines.append(f"- **{r['model']}**")

        if increases:
            lines += ["", "### Subidas destacadas"]
            for r in increases[:5]:
                lines.append(
                    f"- **{r['model']}** — +{r['change_pct']:.1f}%"
                )

    lines += [
        "",
        "## 🆓 Mejores gratuitos puntuados",
        "",
    ]
    free_scored = [
        r for r in models
        if r.get("quality")
        and r["input_usd_per_million"] == 0
        and r["output_usd_per_million"] == 0
    ]
    free_scored.sort(
        key=lambda r: max(r["quality"]["scores"].values() or [0]),
        reverse=True,
    )
    for r in free_scored[:10]:
        s = r["quality"]["scores"]
        lines.append(
            f"- **{r['model_id']}** — coding {s.get('coding','—')}, "
            f"agentic {s.get('agentic','—')}, reasoning {s.get('reasoning','—')}, "
            f"general {s.get('general','—')}"
        )
    if not free_scored:
        lines.append("- No hay modelos gratuitos con score curado hoy.")

    lines += [
        "",
        "## 💸 Modelos de texto más baratos",
        "",
    ]
    for i, r in enumerate(models[:12], 1):
        quality_txt = ""
        if r.get("quality"):
            quality_txt = f" · score conocido: {r['quality']['label']}"
        lines.append(
            f"{i}. **{r['model_id']}** — "
            f"in ${r['input_usd_per_million']:.4f}/M, "
            f"out ${r['output_usd_per_million']:.4f}/M, "
            f"coste perfil ${r['weighted_cost']:.5f}{quality_txt}"
        )

    lines += [
        "",
        "## 🧪 Cómo interpretar el ranking",
        "",
        "- El **coste/tarea** usa los tamaños de prompt/respuesta definidos en `config.json`.",
        "- El **Value Score** combina el score de calidad con el coste estimado de esa tarea.",
        "- Los scores de calidad viven en `quality_profiles.json` y son editables/auditables.",
        "- Un modelo sin score puede aparecer entre los baratos, pero no se recomienda automáticamente.",
        "- Los modelos gratuitos pueden tener límites de velocidad, cuota o disponibilidad.",
    ]

    # El LLM sólo redacta; no decide los números.
    ai = generate_summary(snapshot, config)
    if ai:
        lines += ["", "## 🤖 Resumen y recomendación IA", "", ai]

    report = "\n".join(lines) + "\n"
    (reports_dir / f"{day}.md").write_text(report, encoding="utf-8")
    (reports_dir / "latest.md").write_text(report, encoding="utf-8")
    print(report)

if __name__ == "__main__":
    main()
