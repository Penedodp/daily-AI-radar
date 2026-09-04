"""Builds the static dashboard published via GitHub Pages (docs/index.html).

Pure stdlib string templating — no extra dependency, no client-side build step.
Reuses the exact same `snapshot`/`recs` data structures as the Markdown report,
so the two never drift apart.
"""
import html as html_lib

LABELS = {
    "coding": "💻 Coding",
    "agentic": "🤖 Agentic coding",
    "reasoning": "🧠 Razonamiento",
    "general": "⚡ General",
}

NO_BENCH_NOTE = "Sin benchmark automatizado disponible todavía para esta categoría."


def _esc(v):
    return html_lib.escape(str(v))


def _money(v):
    return f"${v:.4f}" if v is not None else "—"


def _cost(v):
    return f"${v:.5f}" if v is not None else "—"


def _row_price_cells(r):
    return f"<td>{_money(r['input'])}</td><td>{_money(r['output'])}</td>"


def _section_free(recs, scored_categories):
    rows = []
    for cat, label in LABELS.items():
        if cat not in scored_categories:
            rows.append(f"<tr><td>{label}</td><td colspan='4' class='muted'>{NO_BENCH_NOTE}</td></tr>")
            continue
        r = recs[cat]["best_free"]
        if not r:
            rows.append(f"<tr><td>{label}</td><td colspan='4' class='muted'>—</td></tr>")
            continue
        rows.append(
            f"<tr><td>{label}</td><td><strong>{_esc(r['model'])}</strong></td>"
            f"<td>{r.get('quality_score','—')}/10</td><td>{_esc(r['provider'])}</td>"
            f"<td>{_money(r['input'])} / {_money(r['output'])}</td></tr>"
        )
    return "".join(rows)


def _section_paid_value(recs, scored_categories):
    rows = []
    for cat, label in LABELS.items():
        if cat not in scored_categories:
            rows.append(f"<tr><td>{label}</td><td colspan='6' class='muted'>{NO_BENCH_NOTE}</td></tr>")
            continue
        r = recs[cat]["best_paid_value"]
        if not r:
            rows.append(f"<tr><td>{label}</td><td colspan='6' class='muted'>—</td></tr>")
            continue
        rows.append(
            f"<tr><td>{label}</td><td><strong>{_esc(r['model'])}</strong></td>"
            f"<td>{_esc(r['provider'])}</td><td>{_cost(r['task_cost'])}</td>"
            f"{_row_price_cells(r)}<td>{r.get('quality_score','—')}/10</td>"
            f"<td>{r.get('value_score','—')}</td></tr>"
        )
    return "".join(rows)


def _section_paid_quality(recs, scored_categories):
    rows = []
    for cat, label in LABELS.items():
        if cat not in scored_categories:
            rows.append(f"<tr><td>{label}</td><td colspan='5' class='muted'>{NO_BENCH_NOTE}</td></tr>")
            continue
        r = recs[cat]["best_paid_quality"]
        if not r:
            rows.append(f"<tr><td>{label}</td><td colspan='5' class='muted'>—</td></tr>")
            continue
        rows.append(
            f"<tr><td>{label}</td><td><strong>{_esc(r['model'])}</strong></td>"
            f"<td>{_esc(r['provider'])}</td><td>{_cost(r['task_cost'])}</td>"
            f"{_row_price_cells(r)}<td>{r.get('quality_score','—')}/10</td></tr>"
        )
    return "".join(rows)


def _section_top5(recs, scored_categories):
    blocks = []
    for cat, label in LABELS.items():
        blocks.append(f"<h3>{label}</h3>")
        if cat not in scored_categories:
            blocks.append(f"<p class='muted'>{NO_BENCH_NOTE}</p>")
            continue
        top = recs[cat]["top_paid_value"]
        if not top:
            blocks.append("<p class='muted'>Sin candidatos de pago que superen el mínimo de calidad configurado.</p>")
            continue
        items = "".join(
            f"<li><strong>{_esc(r['model'])}</strong> vía <strong>{_esc(r['provider'])}</strong> — "
            f"calidad {r.get('quality_score','—')}/10 · coste/tarea {_cost(r['task_cost'])} "
            f"({_money(r['input'])} in / {_money(r['output'])} out) · value {r.get('value_score','—')}</li>"
            for r in top
        )
        blocks.append(f"<ol>{items}</ol>")
    return "".join(blocks)


def _section_opportunities(opportunities):
    if not opportunities:
        return "<p class='muted'>Aún no hay suficientes fuentes configuradas con el mismo modelo, o no hay diferencias ≥ al umbral.</p>"
    rows = []
    for o in opportunities[:15]:
        a, b = o["cheapest"], o["next"]
        rows.append(
            f"<tr><td><strong>{_esc(o['model'])}</strong></td><td><strong>{_esc(a['provider'])}</strong></td>"
            f"<td>{_cost(a['weighted_cost'])}</td>{_row_price_cells(a)}"
            f"<td>{_esc(b['provider'])} ({_cost(b['weighted_cost'])})</td>"
            f"<td class='pos'>{o['saving_vs_next_pct']:.1f}%</td></tr>"
        )
    return (
        "<table><thead><tr><th>Modelo</th><th>Más barato</th><th>Coste perfil</th>"
        "<th>$/M input</th><th>$/M output</th><th>Siguiente</th><th>Ahorro</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def _section_changes(previous, drops, increases):
    if not previous:
        return "<p class='muted'>Todavía no hay snapshot de un día anterior para comparar.</p>"
    parts = []
    if drops:
        items = "".join(
            f"<li><strong>{_esc(r['model'])}</strong> vía <strong>{_esc(r['provider'])}</strong> — "
            f"<span class='pos'>{r['change_pct']:.1f}%</span> "
            f"(ahora {_money(r['input'])} in / {_money(r['output'])} out)</li>"
            for r in drops[:12]
        )
        parts.append(f"<h3>Bajadas</h3><ul>{items}</ul>")
    else:
        parts.append("<p class='muted'>No se detectaron bajadas ≥ al umbral en la misma ruta/proveedor.</p>")
    if increases:
        items = "".join(
            f"<li><strong>{_esc(r['model'])}</strong> vía <strong>{_esc(r['provider'])}</strong> — "
            f"<span class='neg'>+{r['change_pct']:.1f}%</span> "
            f"(ahora {_money(r['input'])} in / {_money(r['output'])} out)</li>"
            for r in increases[:8]
        )
        parts.append(f"<h3>Subidas</h3><ul>{items}</ul>")
    return "".join(parts)


def _section_sources(provider_status):
    rows = "".join(
        f"<tr><td>{_esc(name)}</td><td><code>{_esc(s.get('status','unknown'))}</code></td>"
        f"<td>{s.get('count', 0)}</td></tr>"
        for name, s in provider_status.items()
    )
    return f"<table><thead><tr><th>Fuente</th><th>Estado</th><th>Registros</th></tr></thead><tbody>{rows}</tbody></table>"


PAGE_TEMPLATE = """<!doctype html>
<html lang="es" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Price Radar — {day}</title>
<style>
:root {{
  --bg: #0b0f14; --panel: #121821; --border: #232c38; --text: #e6edf3;
  --muted: #8b98a5; --accent: #4fa3ff; --pos: #3fd88a; --neg: #ff6b6b;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--bg); color: var(--text);
  font: 15px/1.5 -apple-system, "Segoe UI", Roboto, sans-serif;
  padding: 24px 16px 64px;
}}
main {{ max-width: 1080px; margin: 0 auto; }}
h1 {{ font-size: 1.5rem; margin-bottom: 4px; }}
h2 {{ font-size: 1.15rem; margin: 40px 0 12px; border-bottom: 1px solid var(--border); padding-bottom: 8px; }}
h3 {{ font-size: 1rem; margin: 20px 0 8px; color: var(--accent); }}
.subtitle {{ color: var(--muted); margin-bottom: 8px; }}
.panel {{
  background: var(--panel); border: 1px solid var(--border); border-radius: 10px;
  padding: 16px 20px; margin-bottom: 8px;
}}
.table-scroll {{ overflow-x: auto; }}
table {{ width: 100%; border-collapse: collapse; font-size: 0.92rem; }}
th, td {{ text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--border); white-space: nowrap; }}
th {{ color: var(--muted); font-weight: 600; }}
tr:last-child td {{ border-bottom: none; }}
.muted {{ color: var(--muted); white-space: normal; }}
.pos {{ color: var(--pos); font-weight: 600; }}
.neg {{ color: var(--neg); font-weight: 600; }}
code {{ background: #1c2530; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; }}
ol, ul {{ padding-left: 20px; }}
li {{ margin-bottom: 6px; }}
footer {{ color: var(--muted); font-size: 0.85rem; margin-top: 48px; }}
.note {{ color: var(--muted); font-size: 0.85rem; margin-top: 8px; }}
.ai-summary {{ white-space: pre-wrap; }}
@media (prefers-color-scheme: light) {{
  :root:not([data-theme="dark"]) {{
    --bg: #f7f8fa; --panel: #ffffff; --border: #e2e6eb; --text: #1a2027; --muted: #64707c;
  }}
}}
</style>
</head>
<body>
<main>
  <h1>📡 AI Price Radar</h1>
  <p class="subtitle">{day} · {models_kept} rutas/modelos útiles · {sources_with_data} fuentes con datos · {scored_routes} rutas puntuadas</p>

  <h2>Fuentes</h2>
  <div class="panel table-scroll">{sources_table}</div>

  <h2>🆓 Mejor opción gratuita</h2>
  <div class="panel table-scroll"><table><thead><tr><th>Uso</th><th>Modelo</th><th>Calidad*</th><th>Proveedor/ruta</th><th>$/M in / out</th></tr></thead><tbody>{free_rows}</tbody></table></div>

  <h2>💰 Mejor relación calidad/precio DE PAGO</h2>
  <div class="panel table-scroll"><table><thead><tr><th>Uso</th><th>Modelo</th><th>Proveedor/ruta</th><th>Coste/tarea</th><th>$/M in</th><th>$/M out</th><th>Calidad*</th><th>Value</th></tr></thead><tbody>{paid_value_rows}</tbody></table></div>

  <h2>🧠 Opción premium por calidad</h2>
  <div class="panel table-scroll"><table><thead><tr><th>Uso</th><th>Modelo</th><th>Proveedor/ruta</th><th>Coste/tarea</th><th>$/M in</th><th>$/M out</th><th>Calidad*</th></tr></thead><tbody>{paid_quality_rows}</tbody></table></div>
  <p class="note">* Calidad (coding) = pass-rate del Aider Polyglot Leaderboard escalado a 0–10, emparejado automáticamente por nombre de modelo. Sin match fiable → sin puntuar, nunca estimado.</p>

  <h2>🔀 Mismo modelo, proveedor/ruta más barata</h2>
  <div class="panel table-scroll">{opportunities_html}</div>

  <h2>🏆 Top 5 DE PAGO por calidad/precio</h2>
  <div class="panel">{top5_html}</div>

  <h2>🔥 Cambios de precio</h2>
  <div class="panel">{changes_html}</div>

  {ai_section}

  <footer>Generado automáticamente. Los precios se recogen cada mañana; el histórico completo está en <code>data/</code> y <code>reports/</code> del repositorio.</footer>
</main>
</body>
</html>
"""


def build_html(snapshot, day, has_previous, ai_summary=None):
    recs = snapshot["recommendations"]
    scored_categories = {
        cat for cat in LABELS
        if any(
            r.get("quality") and r["quality"]["scores"].get(cat) is not None
            for r in snapshot["models"]
        )
    }

    ai_section = ""
    if ai_summary:
        ai_section = (
            "<h2>🤖 Estrategia recomendada para hoy</h2>"
            f"<div class='panel ai-summary'>{_esc(ai_summary)}</div>"
        )

    return PAGE_TEMPLATE.format(
        day=day,
        models_kept=snapshot["stats"]["models_kept"],
        sources_with_data=snapshot["stats"]["providers_with_data"],
        scored_routes=snapshot["stats"]["scored_routes"],
        sources_table=_section_sources(snapshot["provider_status"]),
        free_rows=_section_free(recs, scored_categories),
        paid_value_rows=_section_paid_value(recs, scored_categories),
        paid_quality_rows=_section_paid_quality(recs, scored_categories),
        opportunities_html=_section_opportunities(snapshot["cross_provider_opportunities"]),
        top5_html=_section_top5(recs, scored_categories),
        changes_html=_section_changes(
            has_previous,
            snapshot["changes"]["drops"],
            snapshot["changes"]["increases"],
        ),
        ai_section=ai_section,
    )
