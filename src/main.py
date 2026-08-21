from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json

from providers.openrouter import fetch_models
from scoring import weighted_daily_cost, price_change
from report_ai import generate_summary

ROOT = Path(__file__).resolve().parents[1]

def load_json(path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    config = load_json(ROOT / "config.json", {})
    tz = ZoneInfo(config.get("timezone", "Europe/Lisbon"))
    now = datetime.now(tz)
    day = now.date().isoformat()

    data_dir = ROOT / "data"
    reports_dir = ROOT / "reports"
    data_dir.mkdir(exist_ok=True)
    reports_dir.mkdir(exist_ok=True)

    previous = None
    existing = sorted(data_dir.glob("*.json"))
    if existing:
        previous = load_json(existing[-1], {})
    prev_map = {}
    if previous:
        for r in previous.get("models", []):
            prev_map[r["model_id"]] = r

    tracked = set(config.get("tracked_authors", []))
    models = []
    for row in fetch_models():
        author = (row["model_id"] or "").split("/", 1)[0]
        if tracked and author not in tracked:
            continue

        row["weighted_cost"] = weighted_daily_cost(
            row, config.get("usage_profiles", {})
        )
        old = prev_map.get(row["model_id"])
        old_cost = old.get("weighted_cost") if old else None
        row["change_pct"] = price_change(row["weighted_cost"], old_cost)
        models.append(row)

    models.sort(key=lambda x: x["weighted_cost"])
    snapshot = {
        "generated_at": now.isoformat(),
        "models": models
    }
    (data_dir / f"{day}.json").write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    lines = [
        f"# AI Price Radar — {day}",
        "",
        "## Modelos más baratos según tu perfil",
        ""
    ]
    for i, r in enumerate(models[:15], 1):
        change = ""
        if r.get("change_pct") is not None:
            change = f" | cambio: {r['change_pct']:+.1f}%"
        lines.append(
            f"{i}. **{r['model_id']}** — "
            f"in ${r['input_usd_per_million']:.3f}/M, "
            f"out ${r['output_usd_per_million']:.3f}/M, "
            f"coste perfil ${r['weighted_cost']:.5f}{change}"
        )

    ai = generate_summary(snapshot, config)
    if ai:
        lines += ["", "## Recomendación IA", "", ai]

    report = "\n".join(lines) + "\n"
    (reports_dir / f"{day}.md").write_text(report, encoding="utf-8")
    (reports_dir / "latest.md").write_text(report, encoding="utf-8")
    print(report)

if __name__ == "__main__":
    main()
