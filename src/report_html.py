"""Builds the static dashboard published via GitHub Pages (docs/index.html).

Design: a dark, data-dense "market scanner" — the tables intentionally read
like OpenRouter/exchange-style pricing grids (the reference the product
owner asked to match), wrapped in a distinct visual identity:

  Color   bg #0a0d12 / panel #12161d / border #1e2530 / text #e8ecf1 /
          muted #8a94a3 · accent (radar amber) #f5a623 · pos #34d399 ·
          neg #f87171. Light theme mirrors these on a warm-neutral ground.
  Type    Bricolage Grotesque (display) + Manrope (UI/body) +
          JetBrains Mono (tabular numbers — prices line up like a ticker).
  Layout  compact radar-sweep hero (not full-viewport) with live stat
          tiles, then numbered sections (01-06) that mirror the actual
          decision funnel of the report (free -> value -> premium ->
          arbitrage -> shortlist -> price moves), revealed on scroll.

Pure stdlib string templating — no build step. Reuses the exact same
`snapshot`/`recs` structures as the Markdown report, so the two can't drift.
"""
import html as html_lib

LABELS = {
    "coding": "Coding",
    "agentic": "Agentic coding",
    "reasoning": "Razonamiento",
    "general": "General",
}

NO_BENCH_NOTE = "Sin benchmark automatizado disponible todavía para esta categoría."

_BADGE_PALETTE = [
    "#f5a623", "#34d399", "#60a5fa", "#f472b6", "#a78bfa",
    "#fb923c", "#2dd4bf", "#f87171", "#facc15", "#818cf8",
]


def _esc(v):
    return html_lib.escape(str(v))


def _money(v):
    return f"${v:.4f}" if v is not None else "—"


def _cost(v):
    return f"${v:.5f}" if v is not None else "—"


def _provider_badge(name):
    label = (name or "?").split("→")[-1].strip()
    words = [w for w in label.replace("/", " ").split() if w]
    initials = "".join(w[0] for w in words[:2]).upper() or "?"
    color = _BADGE_PALETTE[sum(ord(c) for c in label) % len(_BADGE_PALETTE)]
    return (
        f"<span class='provider'><span class='provider-dot' style='background:{color}'>"
        f"{_esc(initials)}</span>{_esc(name)}</span>"
    )


def _quality_cell(score, label=None, ratio=None, source_label=None, sortable=False):
    key = " data-key='quality'" if sortable else ""
    if score is None:
        return f"<td{key} data-value='-1' class='muted'>—</td>"
    pct = max(0.0, min(100.0, score * 10))
    tier = "tier-good" if score >= 6.5 else ("tier-mid" if score >= 3.5 else "tier-low")
    tooltip = f"{source_label or 'Match automático'}: {score:.1f}/10"
    if label:
        tooltip += f" · match ‘{label}’"
    if ratio is not None:
        tooltip += f" ({ratio * 100:.0f}% similitud de nombre)"
    return (
        f"<td{key} data-value='{score}'><span class='qcell' title='{_esc(tooltip)}'>"
        f"<span class='qbar'><span class='qbar-fill {tier}' style='width:{pct:.0f}%'></span></span>"
        f"<span class='qval'>{score:.1f}</span></span></td>"
    )


def _num_td(value, text, key=None):
    attr = f" data-key='{key}'" if key else ""
    v = "-999999" if value is None else str(value)
    return f"<td{attr} data-value='{v}' class='num'>{text}</td>"


def _section_free(recs, scored_categories):
    rows = []
    for cat, label in LABELS.items():
        if cat not in scored_categories:
            rows.append(f"<tr><td class='usage'>{label}</td><td colspan='4' class='muted'>{NO_BENCH_NOTE}</td></tr>")
            continue
        r = recs[cat]["best_free"]
        if not r:
            rows.append(f"<tr><td class='usage'>{label}</td><td colspan='4' class='muted'>Sin candidato gratis puntuado</td></tr>")
            continue
        rows.append(
            f"<tr><td class='usage'>{label}</td><td><strong>{_esc(r['model'])}</strong></td>"
            f"{_quality_cell(r.get('quality_score'), r.get('quality_label'), r.get('quality_match_ratio'), r.get('quality_source_label'))}"
            f"<td>{_provider_badge(r['provider'])}</td>"
            f"{_num_td(r['input'], _money(r['input']))}{_num_td(r['output'], _money(r['output']))}</tr>"
        )
    return "".join(rows)


def _section_paid_value(recs, scored_categories):
    rows = []
    for cat, label in LABELS.items():
        if cat not in scored_categories:
            rows.append(f"<tr><td class='usage'>{label}</td><td colspan='6' class='muted'>{NO_BENCH_NOTE}</td></tr>")
            continue
        r = recs[cat]["best_paid_value"]
        if not r:
            rows.append(f"<tr><td class='usage'>{label}</td><td colspan='6' class='muted'>Ningún modelo supera el mínimo de calidad</td></tr>")
            continue
        rows.append(
            f"<tr><td class='usage'>{label}</td><td><strong>{_esc(r['model'])}</strong></td>"
            f"<td>{_provider_badge(r['provider'])}</td>"
            f"{_num_td(r['task_cost'], _cost(r['task_cost']))}"
            f"{_num_td(r['input'], _money(r['input']))}{_num_td(r['output'], _money(r['output']))}"
            f"{_quality_cell(r.get('quality_score'), r.get('quality_label'), r.get('quality_match_ratio'), r.get('quality_source_label'))}"
            f"{_num_td(r.get('value_score'), r.get('value_score', '—'))}</tr>"
        )
    return "".join(rows)


def _section_paid_quality(recs, scored_categories):
    rows = []
    for cat, label in LABELS.items():
        if cat not in scored_categories:
            rows.append(f"<tr><td class='usage'>{label}</td><td colspan='5' class='muted'>{NO_BENCH_NOTE}</td></tr>")
            continue
        r = recs[cat]["best_paid_quality"]
        if not r:
            rows.append(f"<tr><td class='usage'>{label}</td><td colspan='5' class='muted'>—</td></tr>")
            continue
        rows.append(
            f"<tr><td class='usage'>{label}</td><td><strong>{_esc(r['model'])}</strong></td>"
            f"<td>{_provider_badge(r['provider'])}</td>"
            f"{_num_td(r['task_cost'], _cost(r['task_cost']))}"
            f"{_num_td(r['input'], _money(r['input']))}{_num_td(r['output'], _money(r['output']))}"
            f"{_quality_cell(r.get('quality_score'), r.get('quality_label'), r.get('quality_match_ratio'), r.get('quality_source_label'))}</tr>"
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
            f"<li><span class='rank'>{i}</span><div><strong>{_esc(r['model'])}</strong> vía "
            f"{_provider_badge(r['provider'])}<div class='meta'>"
            f"calidad {r.get('quality_score','—')}/10 · coste/tarea {_cost(r['task_cost'])} "
            f"({_money(r['input'])} in / {_money(r['output'])} out) · value {r.get('value_score','—')}"
            f"</div></div></li>"
            for i, r in enumerate(top, 1)
        )
        blocks.append(f"<ol class='top5'>{items}</ol>")
    return "".join(blocks)


def _section_opportunities(opportunities):
    if not opportunities:
        return "<p class='muted'>Aún no hay suficientes fuentes configuradas con el mismo modelo, o no hay diferencias ≥ al umbral.</p>"
    rows = []
    for o in opportunities[:15]:
        a, b = o["cheapest"], o["next"]
        saving_pill = f"<span class='pill pos'>-{o['saving_vs_next_pct']:.1f}%</span>"
        rows.append(
            f"<tr><td><strong>{_esc(o['model'])}</strong></td><td>{_provider_badge(a['provider'])}</td>"
            f"{_num_td(a['weighted_cost'], _cost(a['weighted_cost']), 'cost')}"
            f"{_num_td(a['input'], _money(a['input']), 'input')}{_num_td(a['output'], _money(a['output']), 'output')}"
            f"<td>{_esc(b['provider'])} ({_cost(b['weighted_cost'])})</td>"
            f"{_num_td(o['saving_vs_next_pct'], saving_pill, 'saving')}</tr>"
        )
    return (
        "<div class='table-scroll'><table class='grid' data-sortable>"
        "<thead><tr>"
        "<th>Modelo</th><th>Más barato</th>"
        "<th data-key='cost'>Coste perfil ↕</th>"
        "<th data-key='input'>$/M input ↕</th><th data-key='output'>$/M output ↕</th>"
        "<th>Siguiente</th><th data-key='saving'>Ahorro ↕</th>"
        "</tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table></div>"
    )


def _section_changes(has_previous, drops, increases):
    if not has_previous:
        return "<p class='muted'>Todavía no hay snapshot de un día anterior para comparar.</p>"
    parts = []
    if drops:
        items = "".join(
            f"<li><strong>{_esc(r['model'])}</strong> vía {_provider_badge(r['provider'])} "
            f"<span class='pill pos'>{r['change_pct']:.1f}%</span> "
            f"<span class='meta'>ahora {_money(r['input'])} in / {_money(r['output'])} out</span></li>"
            for r in drops[:12]
        )
        parts.append(f"<h3>Bajadas</h3><ul class='changes'>{items}</ul>")
    else:
        parts.append("<p class='muted'>No se detectaron bajadas ≥ al umbral en la misma ruta/proveedor.</p>")
    if increases:
        items = "".join(
            f"<li><strong>{_esc(r['model'])}</strong> vía {_provider_badge(r['provider'])} "
            f"<span class='pill neg'>+{r['change_pct']:.1f}%</span> "
            f"<span class='meta'>ahora {_money(r['input'])} in / {_money(r['output'])} out</span></li>"
            for r in increases[:8]
        )
        parts.append(f"<h3>Subidas</h3><ul class='changes'>{items}</ul>")
    return "".join(parts)


def _sparkline(trend, width=560, height=64):
    if not trend:
        return ""
    points = trend["points"]
    if len(points) < 2:
        return ""
    costs = [p["cost"] for p in points]
    lo, hi = min(costs), max(costs)
    span = (hi - lo) or (lo or 1)
    pad = 6
    n = len(points)
    xs = [pad + i / (n - 1) * (width - 2 * pad) for i in range(n)]
    ys = [pad + (1 - (c - lo) / span) * (height - 2 * pad) for c in costs]
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    area = f"{xs[0]:.1f},{height} " + line + f" {xs[-1]:.1f},{height}"
    first, last = points[0], points[-1]
    delta = ((last["cost"] - first["cost"]) / first["cost"] * 100) if first["cost"] else 0
    delta_cls = "pos" if delta <= 0 else "neg"
    delta_sign = "" if delta <= 0 else "+"
    model_esc = _esc(trend["model"])
    return (
        "<div class='spark'>"
        f"<div class='spark-head'>Evolución de <strong>{model_esc}</strong> "
        f"<span class='pill {delta_cls}'>{delta_sign}{delta:.1f}% en {n} días</span></div>"
        f"<svg viewBox='0 0 {width} {height}' preserveAspectRatio='none' class='spark-svg' role='img' "
        f"aria-label='Evolución de coste de {model_esc} en los últimos {n} días'>"
        f"<polygon points='{area}' class='spark-area'></polygon>"
        f"<polyline points='{line}' class='spark-line'></polyline>"
        f"<circle cx='{xs[-1]:.1f}' cy='{ys[-1]:.1f}' r='3.2' class='spark-dot'></circle>"
        "</svg>"
        f"<div class='spark-foot'><span>{first['date']}</span><span>{last['date']} · {_cost(last['cost'])}/tarea</span></div>"
        "</div>"
    )


def _status_chips(provider_status):
    dot = {"ok": "chip-ok", "cached_stale": "chip-warn"}
    chips = []
    for name, s in provider_status.items():
        status = s.get("status", "unknown")
        cls = dot.get(status, "chip-off")
        chips.append(
            f"<span class='chip'><span class='chip-dot {cls}'></span>"
            f"<span class='chip-name'>{_esc(name)}</span>"
            f"<span class='chip-count'>{s.get('count', 0)}</span></span>"
        )
    return "".join(chips)


STYLE = """
:root {
  --bg: #f6f4ef; --panel: #ffffff; --border: #e6e2d8; --text: #171a1f; --muted: #6b7280;
  --accent: #b8720a; --accent-soft: #fef3e0; --pos: #0f9d68; --neg: #dc4444;
  --shadow: 0 1px 2px rgba(20,20,10,0.04);
  --font-display: "Bricolage Grotesque", "Manrope", sans-serif;
  --font-body: "Manrope", -apple-system, "Segoe UI", sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, monospace;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0a0d12; --panel: #12161d; --border: #1e2530; --text: #e8ecf1; --muted: #8a94a3;
    --accent: #f5a623; --accent-soft: rgba(245,166,35,0.12); --pos: #34d399; --neg: #f87171;
    --shadow: 0 1px 2px rgba(0,0,0,0.3);
  }
}
:root[data-theme="dark"] {
  --bg: #0a0d12; --panel: #12161d; --border: #1e2530; --text: #e8ecf1; --muted: #8a94a3;
  --accent: #f5a623; --accent-soft: rgba(245,166,35,0.12); --pos: #34d399; --neg: #f87171;
  --shadow: 0 1px 2px rgba(0,0,0,0.3);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0; background: var(--bg); color: var(--text); font: 15px/1.55 var(--font-body);
}
a { color: inherit; }
main { max-width: 1120px; margin: 0 auto; padding: 0 20px 96px; }
h1, h2, h3 { font-family: var(--font-display); text-wrap: balance; margin: 0; }
p { text-wrap: pretty; }
::selection { background: var(--accent-soft); }

/* ---------- top bar ---------- */
.topbar {
  display: flex; align-items: center; justify-content: space-between;
  max-width: 1120px; margin: 0 auto; padding: 18px 20px;
  font-size: 0.82rem; color: var(--muted); letter-spacing: .02em;
}
.topbar .brand { display: flex; align-items: center; gap: 8px; color: var(--text); font-weight: 600; }
.topbar .brand-mark { width: 8px; height: 8px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }

/* ---------- section nav (sticky) ---------- */
.toc-wrap { position: sticky; top: 0; z-index: 10; background: var(--bg); border-bottom: 1px solid var(--border); }
.toc {
  max-width: 1120px; margin: 0 auto; padding: 0 20px; display: flex; gap: 4px; overflow-x: auto;
  scrollbar-width: none;
}
.toc::-webkit-scrollbar { display: none; }
.toc a {
  flex: none; display: flex; align-items: center; gap: 6px; padding: 12px 12px; text-decoration: none;
  font-size: 0.78rem; color: var(--muted); border-bottom: 2px solid transparent; white-space: nowrap;
}
.toc a span.n { font-family: var(--font-mono); color: var(--accent); }
.toc a:hover { color: var(--text); }
.toc a.active { color: var(--text); border-bottom-color: var(--accent); }

/* ---------- hero ---------- */
.hero {
  position: relative; max-width: 1120px; margin: 0 auto; padding: 8px 20px 40px;
  overflow: hidden;
}
.hero-inner { position: relative; z-index: 2; max-width: 640px; }
.eyebrow {
  font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: .12em; text-transform: uppercase;
  color: var(--accent); margin-bottom: 14px; display: inline-block;
}
.hero h1 { font-size: clamp(2rem, 4.5vw, 3rem); font-weight: 600; line-height: 1.08; letter-spacing: -0.01em; }
.hero p.lede { color: var(--muted); font-size: 1.02rem; margin: 16px 0 0; max-width: 52ch; }
.stat-row { display: flex; gap: 28px; margin-top: 32px; flex-wrap: wrap; }
.stat-tile .stat-num {
  font-family: var(--font-mono); font-size: 1.9rem; font-weight: 500; color: var(--text);
  font-variant-numeric: tabular-nums;
}
.stat-tile .stat-label { font-size: 0.78rem; color: var(--muted); margin-top: 2px; }

.radar-wrap {
  position: absolute; top: -60px; right: -60px; width: 340px; height: 340px; z-index: 1;
  pointer-events: none;
}
.radar-ring { position: absolute; inset: 0; border-radius: 50%; border: 1px solid var(--border); }
.radar-ring.r2 { inset: 42px; }
.radar-ring.r3 { inset: 84px; }
.radar-sweep {
  position: absolute; inset: 0; border-radius: 50%;
  background: conic-gradient(from 0deg, color-mix(in srgb, var(--accent) 65%, transparent), transparent 65%);
  animation: spin 7s linear infinite;
  opacity: 0.55;
}
/* rotate counter-clockwise so the bright edge leads the sweep and the fade trails behind it */
@keyframes spin { to { transform: rotate(-360deg); } }
@media (max-width: 760px) { .radar-wrap { display: none; } }

/* ---------- status chips ---------- */
.chips { display: flex; flex-wrap: wrap; gap: 10px; margin: 28px 0 4px; }
.chip {
  display: flex; align-items: center; gap: 8px; background: var(--panel); border: 1px solid var(--border);
  border-radius: 100px; padding: 6px 14px 6px 10px; font-size: 0.82rem; box-shadow: var(--shadow);
}
.chip-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--muted); }
.chip-dot.chip-ok { background: var(--pos); }
.chip-dot.chip-warn { background: var(--accent); }
.chip-dot.chip-off { background: var(--muted); opacity: .5; }
.chip-name { color: var(--muted); font-family: var(--font-mono); font-size: 0.78rem; }
.chip-count { font-family: var(--font-mono); font-weight: 600; }

/* ---------- sections ---------- */
section.block { margin: 64px 0; }
.block-head { display: flex; align-items: baseline; gap: 14px; margin-bottom: 18px; }
.block-head .idx {
  font-family: var(--font-mono); color: var(--accent); font-size: 0.85rem; letter-spacing: .04em;
}
.block-head h2 { font-size: 1.4rem; font-weight: 600; }
.block-note { color: var(--muted); font-size: 0.88rem; margin: -8px 0 18px; max-width: 62ch; }

/* ---------- tables ---------- */
.table-scroll {
  overflow-x: auto; -webkit-overflow-scrolling: touch;
  scrollbar-width: thin; scrollbar-color: var(--border) transparent;
}
.table-scroll::-webkit-scrollbar { height: 6px; }
.table-scroll::-webkit-scrollbar-track { background: transparent; }
.table-scroll::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
.table-scroll::-webkit-scrollbar-thumb:hover { background: var(--muted); }
table.grid { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
table.grid th {
  text-align: left; padding: 9px 11px; color: var(--muted); font-weight: 600; font-size: 0.7rem;
  text-transform: uppercase; letter-spacing: .06em; border-bottom: 1px solid var(--border);
  white-space: nowrap; user-select: none;
}
table.grid[data-sortable] th[data-key] { cursor: pointer; }
table.grid[data-sortable] th[data-key]:hover { color: var(--text); }
table.grid td { padding: 10px 11px; border-bottom: 1px solid var(--border); white-space: nowrap; }
table.grid td.num { font-family: var(--font-mono); font-variant-numeric: tabular-nums; }
table.grid tbody tr:last-child td { border-bottom: none; }
table.grid tbody tr:hover { background: var(--accent-soft); }
table.grid td.usage { color: var(--muted); font-size: 0.82rem; width: 1%; }
table.grid td.muted { color: var(--muted); white-space: normal; }

.provider { display: inline-flex; align-items: center; gap: 8px; }
.provider-dot {
  width: 20px; height: 20px; border-radius: 6px; display: inline-flex; align-items: center; justify-content: center;
  font-size: 0.62rem; font-weight: 700; color: #0a0d12; flex: none;
}

.qcell { display: inline-flex; align-items: center; gap: 7px; }
.qbar { width: 36px; height: 5px; border-radius: 3px; background: var(--border); overflow: hidden; flex: none; }
.qbar-fill { display: block; height: 100%; border-radius: 3px; }
.qbar-fill.tier-good { background: var(--pos); }
.qbar-fill.tier-mid { background: var(--accent); }
.qbar-fill.tier-low { background: var(--neg); }
.qval { font-family: var(--font-mono); font-variant-numeric: tabular-nums; color: var(--muted); }

.pill {
  font-family: var(--font-mono); font-size: 0.78rem; font-weight: 600; padding: 3px 9px; border-radius: 100px;
}
.pill.pos { color: var(--pos); background: color-mix(in srgb, var(--pos) 16%, transparent); }
.pill.neg { color: var(--neg); background: color-mix(in srgb, var(--neg) 16%, transparent); }

/* ---------- top5 ---------- */
h3 { font-size: 1rem; font-weight: 600; margin: 28px 0 12px; }
h3:first-child { margin-top: 0; }
ol.top5 { list-style: none; padding: 0; margin: 0; border: 1px solid var(--border); border-radius: 12px; overflow: hidden; }
ol.top5 li { display: flex; gap: 14px; padding: 14px 16px; border-bottom: 1px solid var(--border); align-items: flex-start; }
ol.top5 li:last-child { border-bottom: none; }
ol.top5 .rank {
  font-family: var(--font-mono); color: var(--muted); font-size: 0.85rem; width: 18px; flex: none; padding-top: 2px;
}
ol.top5 .meta { color: var(--muted); font-size: 0.82rem; margin-top: 3px; }

ul.changes { list-style: none; padding: 0; margin: 0 0 20px; }
ul.changes li { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; padding: 10px 0; border-bottom: 1px solid var(--border); }
ul.changes li:last-child { border-bottom: none; }
ul.changes .meta { color: var(--muted); font-size: 0.82rem; }

/* ---------- sparkline ---------- */
.spark {
  margin-top: 20px; border: 1px solid var(--border); border-radius: 12px; padding: 16px 18px;
}
.spark-head { font-size: 0.85rem; display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 8px; }
.spark-svg { width: 100%; height: 64px; display: block; overflow: visible; }
.spark-area { fill: color-mix(in srgb, var(--accent) 14%, transparent); stroke: none; }
.spark-line { fill: none; stroke: var(--accent); stroke-width: 1.6; stroke-linejoin: round; stroke-linecap: round; }
.spark-dot { fill: var(--accent); }
.spark-foot { display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.74rem; color: var(--muted); margin-top: 6px; }

.muted { color: var(--muted); }
.note { color: var(--muted); font-size: 0.85rem; }
.ai-summary { white-space: pre-wrap; line-height: 1.65; background: var(--panel); border: 1px solid var(--border); border-radius: 14px; padding: 24px 28px; box-shadow: var(--shadow); }

/* reveal-on-scroll: hidden state only applied once GSAP is confirmed running */
.gsap-ready .reveal { opacity: 0; }
"""

SCRIPT = """
(function () {
  // --- section nav: active-link tracking ---
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  var sections = tocLinks.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var idx = sections.indexOf(entry.target);
        if (idx === -1) { return; }
        if (entry.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.remove('active'); });
          tocLinks[idx].classList.add('active');
          tocLinks[idx].scrollIntoView({ block: 'nearest', inline: 'center' });
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    sections.forEach(function (s) { if (s) { observer.observe(s); } });
  }

  // --- sortable tables ---
  document.querySelectorAll('table[data-sortable]').forEach(function (table) {
    table.querySelectorAll('th[data-key]').forEach(function (th) {
      th.addEventListener('click', function () {
        var key = th.getAttribute('data-key');
        var dir = th.getAttribute('data-dir') === 'asc' ? 'desc' : 'asc';
        table.querySelectorAll('th[data-key]').forEach(function (x) { x.removeAttribute('data-dir'); });
        th.setAttribute('data-dir', dir);
        var tbody = table.querySelector('tbody');
        var rows = Array.prototype.slice.call(tbody.querySelectorAll('tr'));
        rows.sort(function (ra, rb) {
          var ta = ra.querySelector('[data-key="' + key + '"]');
          var tb = rb.querySelector('[data-key="' + key + '"]');
          var va = ta ? parseFloat(ta.getAttribute('data-value')) : -Infinity;
          var vb = tb ? parseFloat(tb.getAttribute('data-value')) : -Infinity;
          var cmp = va - vb;
          return dir === 'asc' ? cmp : -cmp;
        });
        rows.forEach(function (r) { tbody.appendChild(r); });
      });
    });
  });

  // --- scroll reveal + hero counters ---
  if (!window.gsap) { return; }
  var hasScrollTrigger = !!window.ScrollTrigger;
  if (hasScrollTrigger) { gsap.registerPlugin(ScrollTrigger); }
  document.documentElement.classList.add('gsap-ready');

  document.querySelectorAll('.reveal').forEach(function (section) {
    var rows = section.querySelectorAll('tbody tr, ol.top5 > li, ul.changes > li');
    var tl = gsap.timeline({
      scrollTrigger: hasScrollTrigger
        ? { trigger: section, start: 'top 85%', once: true }
        : undefined,
    });
    tl.fromTo(section, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out' });
    if (rows.length) {
      tl.fromTo(rows, { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.45, stagger: 0.035, ease: 'power2.out' }, '-=0.3');
    }
    if (!hasScrollTrigger) { tl.play(); }
  });

  document.querySelectorAll('.stat-num').forEach(function (el) {
    var target = parseFloat(el.getAttribute('data-value'));
    if (isNaN(target)) { return; }
    var obj = { v: 0 };
    gsap.to(obj, {
      v: target, duration: 1, ease: 'power1.out', delay: 0.15,
      onUpdate: function () { el.textContent = Math.round(obj.v); },
    });
  });
})();
"""

PAGE_HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Price Radar — {day}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{style}</style>
</head>
<body>
<div class="topbar">
  <span class="brand"><span class="brand-mark"></span>AI Price Radar</span>
  <span>Actualizado {day}</span>
</div>

<div class="toc-wrap"><nav class="toc" aria-label="Secciones">{toc}</nav></div>

<header class="hero">
  <div class="radar-wrap" aria-hidden="true">
    <div class="radar-ring"></div>
    <div class="radar-ring r2"></div>
    <div class="radar-ring r3"></div>
    <div class="radar-sweep"></div>
  </div>
  <div class="hero-inner">
    <span class="eyebrow">Escaneo diario de mercado</span>
    <h1>El mejor modelo de IA para programar, al precio de hoy.</h1>
    <p class="lede">Cada mañana comparamos catálogo y precios de varios proveedores contra un benchmark público de programación, y ordenamos las opciones por coste real de tarea — no por lista de precios sin más.</p>
    <div class="stat-row">
      <div class="stat-tile"><span class="stat-num" data-value="{models_kept}">{models_kept}</span><div class="stat-label">rutas / modelos</div></div>
      <div class="stat-tile"><span class="stat-num" data-value="{sources_with_data}">{sources_with_data}</span><div class="stat-label">fuentes con datos</div></div>
      <div class="stat-tile"><span class="stat-num" data-value="{scored_routes}">{scored_routes}</span><div class="stat-label">rutas puntuadas</div></div>
    </div>
    <div class="chips">{chips}</div>
  </div>
</header>

<main>
"""

SECTION_TEMPLATE = """
<section class="block reveal" id="s{idx}">
  <div class="block-head"><span class="idx">{idx}</span><h2>{title}</h2></div>
  {note}
  {body}
</section>
"""

PAGE_TAIL = """
</main>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>{script}</script>
</body>
</html>
"""


def _section_html(idx, title, body, note=""):
    note_html = f"<p class='block-note'>{note}</p>" if note else ""
    return SECTION_TEMPLATE.format(idx=idx, title=title, body=body, note=note_html)


def _toc_html(entries):
    return "".join(
        f"<a href='#s{idx}'><span class='n'>{idx}</span>{title}</a>"
        for idx, title in entries
    )


def build_html(snapshot, day, has_previous, ai_summary=None, price_trends=None):
    recs = snapshot["recommendations"]
    price_trends = price_trends or {}
    scored_categories = {
        cat for cat in LABELS
        if any(
            r.get("quality") and r["quality"]["scores"].get(cat) is not None
            for r in snapshot["models"]
        )
    }

    free_table = (
        "<div class='table-scroll'><table class='grid'><thead><tr>"
        "<th>Uso</th><th>Modelo</th><th>Calidad</th><th>Proveedor</th><th>$/M input</th><th>$/M output</th>"
        f"</tr></thead><tbody>{_section_free(recs, scored_categories)}</tbody></table></div>"
    )
    paid_value_table = (
        "<div class='table-scroll'><table class='grid'><thead><tr>"
        "<th>Uso</th><th>Modelo</th><th>Proveedor</th><th>Coste/tarea</th><th>$/M input</th><th>$/M output</th>"
        "<th>Calidad</th><th>Value</th></tr></thead>"
        f"<tbody>{_section_paid_value(recs, scored_categories)}</tbody></table></div>"
        + _sparkline(price_trends.get("coding"))
    )
    paid_quality_table = (
        "<div class='table-scroll'><table class='grid'><thead><tr>"
        "<th>Uso</th><th>Modelo</th><th>Proveedor</th><th>Coste/tarea</th><th>$/M input</th><th>$/M output</th>"
        "<th>Calidad</th></tr></thead>"
        f"<tbody>{_section_paid_quality(recs, scored_categories)}</tbody></table></div>"
    )

    blocks = [
        ("01", "Mejor opción gratuita", free_table, ""),
        (
            "02", "Mejor relación calidad/precio de pago", paid_value_table,
            "Solo entra un modelo cuando el benchmark de coding lo respalda — un modelo barato "
            "sin score todavía no aparece aquí, aunque merezca la pena; lo verás en las tablas de precio de arriba.",
        ),
        ("03", "Opción premium por calidad", paid_quality_table, ""),
        (
            "04", "Mismo modelo, ruta más barata", _section_opportunities(snapshot["cross_provider_opportunities"]),
            "Compara el mismo modelo entre proveedores — no es una bajada de precio, es elegir mejor ruta hoy.",
        ),
        ("05", "Top 5 de pago por calidad/precio", _section_top5(recs, scored_categories), ""),
        (
            "06", "Movimientos de precio",
            _section_changes(has_previous, snapshot["changes"]["drops"], snapshot["changes"]["increases"]), "",
        ),
    ]
    if ai_summary:
        blocks.append(("07", "Estrategia recomendada para hoy", f"<div class='ai-summary'>{_esc(ai_summary)}</div>", ""))

    toc = _toc_html([(idx, title) for idx, title, _body, _note in blocks])
    sections = "".join(_section_html(idx, title, body, note) for idx, title, body, note in blocks)

    head = PAGE_HEAD.format(
        day=day,
        style=STYLE,
        models_kept=snapshot["stats"]["models_kept"],
        sources_with_data=snapshot["stats"]["providers_with_data"],
        scored_routes=snapshot["stats"]["scored_routes"],
        chips=_status_chips(snapshot["provider_status"]),
        toc=toc,
    )
    tail = PAGE_TAIL.format(script=SCRIPT)
    return head + sections + tail
