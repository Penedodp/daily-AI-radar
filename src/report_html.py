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
import json
from datetime import datetime

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


_KNOWN_PRICE_STATUSES = {"paid", "free", "promotional_free"}


def _price_text(value, pricing_status, fmt=_money):
    """Never render a formatted price for a status we don't actually trust —
    an `unknown` 0/0 must read as '—', not '$0.0000' (audit #2 §9)."""
    if pricing_status not in _KNOWN_PRICE_STATUSES:
        return "—"
    return fmt(value)


def _provider_badge(name):
    label = (name or "?").split("→")[-1].strip()
    words = [w for w in label.replace("/", " ").split() if w]
    initials = "".join(w[0] for w in words[:2]).upper() or "?"
    color = _BADGE_PALETTE[sum(ord(c) for c in label) % len(_BADGE_PALETTE)]
    return (
        f"<span class='provider'><span class='provider-dot' style='background:{color}'>"
        f"{_esc(initials)}</span>{_esc(name)}</span>"
    )


_SOURCE_SHORT = {
    "Aider Polyglot Leaderboard": "Aider",
    "LMArena WebDev Arena": "WebDev Arena",
}


def _quality_span(score, label=None, ratio=None, source_label=None,
                   raw_score=None, raw_unit=None, match_type=None):
    """The inner <span> only — callers that need to pack several source
    scores into one table cell (Model Explorer) use this directly instead of
    `_quality_cell`, which wraps a single one in its own <td>."""
    if score is None:
        return "—"
    pct = max(0.0, min(100.0, score * 10))
    tier = "tier-good" if score >= 6.5 else ("tier-mid" if score >= 3.5 else "tier-low")
    tooltip = f"{source_label or 'Match automático'}"
    if raw_score is not None:
        tooltip += f" — {raw_score:g}{(' ' + raw_unit) if raw_unit else ''}"
    tooltip += f" · normalizado {score:.1f}/10"
    if label:
        tooltip += f" · match ‘{label}’"
    if ratio is not None:
        tooltip += f" ({ratio * 100:.0f}% similitud de nombre{', fuzzy' if match_type == 'fuzzy' else ''})"
    tooltip += ". Puntuaciones de benchmarks distintos no son directamente comparables entre sí."
    short_source = _SOURCE_SHORT.get(source_label, source_label or "auto")
    return (
        f"<span class='qcell' title='{_esc(tooltip)}'>"
        f"<span class='qbar'><span class='qbar-fill {tier}' style='width:{pct:.0f}%'></span></span>"
        f"<span class='qval'>{score:.1f}</span>"
        f"<span class='qsrc'>{_esc(short_source)}</span></span>"
    )


def _quality_cell(score, label=None, ratio=None, source_label=None, sortable=False,
                   raw_score=None, raw_unit=None, match_type=None):
    key = " data-key='quality'" if sortable else ""
    value = "-1" if score is None else str(score)
    span = _quality_span(score, label, ratio, source_label, raw_score, raw_unit, match_type)
    cls = " class='muted'" if score is None else ""
    return f"<td{key} data-value='{value}'{cls}>{span}</td>"


def _num_td(value, text, key=None):
    attr = f" data-key='{key}'" if key else ""
    v = "-999999" if value is None else str(value)
    return f"<td{attr} data-value='{v}' class='num'>{text}</td>"


def _quality_cell_from(r):
    return _quality_cell(
        r.get("quality_score"), r.get("quality_label"), r.get("quality_match_ratio"),
        r.get("quality_source_label"), raw_score=r.get("quality_raw"),
        raw_unit=r.get("quality_raw_unit"), match_type=r.get("quality_match_type"),
    )


def _empty_categories_note(recs):
    empty = [LABELS[c] for c in LABELS if not recs.get(c, {}).get("sources")]
    if not empty:
        return ""
    return f"<p class='muted note'>Próximamente: {' · '.join(empty)} (sin benchmark automatizado todavía).</p>"


def _iter_cat_sources(recs):
    """Yields (category_label, source_key, source_data) for every (category,
    source) pair that actually has data — never a merged/combined ranking."""
    for cat, label in LABELS.items():
        for source, sdata in recs.get(cat, {}).get("sources", {}).items():
            yield label, source, sdata


def _section_free(recs):
    rows = []
    for label, source, sdata in _iter_cat_sources(recs):
        r = sdata["best_free"]
        if not r:
            continue
        rows.append(
            f"<tr><td class='usage'>{label}</td><td><strong>{_esc(r['model'])}</strong></td>"
            f"{_quality_cell_from(r)}"
            f"<td>{_provider_badge(r['provider'])}</td>"
            f"{_num_td(r['input'], _price_text(r['input'], r['pricing_status']))}"
            f"{_num_td(r['output'], _price_text(r['output'], r['pricing_status']))}</tr>"
        )
    if not rows:
        rows.append("<tr><td class='usage'>—</td><td colspan='4' class='muted'>Ningún modelo gratuito puntuado todavía</td></tr>")
    return "".join(rows)


def _section_paid_value(recs):
    rows = []
    for label, source, sdata in _iter_cat_sources(recs):
        r = sdata["best_paid_value"]
        if not r:
            continue
        rows.append(
            f"<tr><td class='usage'>{label}</td><td><strong>{_esc(r['model'])}</strong></td>"
            f"<td>{_provider_badge(r['provider'])}</td>"
            f"{_num_td(r['task_cost'], _cost(r['task_cost']))}"
            f"{_num_td(r['input'], _price_text(r['input'], r['pricing_status']))}"
            f"{_num_td(r['output'], _price_text(r['output'], r['pricing_status']))}"
            f"{_quality_cell_from(r)}"
            f"{_num_td(r.get('value_score'), r.get('value_score', '—'))}</tr>"
        )
    if not rows:
        rows.append("<tr><td class='usage'>—</td><td colspan='6' class='muted'>Ningún modelo de pago supera el mínimo de calidad</td></tr>")
    return "".join(rows)


def _section_paid_quality(recs):
    rows = []
    for label, source, sdata in _iter_cat_sources(recs):
        r = sdata["best_paid_quality"]
        if not r:
            continue
        rows.append(
            f"<tr><td class='usage'>{label}</td><td><strong>{_esc(r['model'])}</strong></td>"
            f"<td>{_provider_badge(r['provider'])}</td>"
            f"{_num_td(r['task_cost'], _cost(r['task_cost']))}"
            f"{_num_td(r['input'], _price_text(r['input'], r['pricing_status']))}"
            f"{_num_td(r['output'], _price_text(r['output'], r['pricing_status']))}"
            f"{_quality_cell_from(r)}</tr>"
        )
    if not rows:
        rows.append("<tr><td class='usage'>—</td><td colspan='5' class='muted'>Sin candidatos de pago puntuados</td></tr>")
    return "".join(rows)


def _section_top5(recs):
    blocks = []
    any_block = False
    for label, source, sdata in _iter_cat_sources(recs):
        top = sdata["top_paid_value"]
        if not top:
            continue
        any_block = True
        blocks.append(f"<h3>{label} · {_esc(sdata['source_label'])}</h3>")
        items = "".join(
            f"<li><span class='rank'>{i}</span><div><strong>{_esc(r['model'])}</strong> vía "
            f"{_provider_badge(r['provider'])}<div class='meta'>"
            f"calidad {r.get('quality_score','—')}/10 · coste estimado {_cost(r['task_cost'])} "
            f"({_price_text(r['input'], r['pricing_status'])} in / {_price_text(r['output'], r['pricing_status'])} out) "
            f"· Radar Value {r.get('value_score','—')}"
            f"</div></div></li>"
            for i, r in enumerate(top, 1)
        )
        blocks.append(f"<ol class='top5'>{items}</ol>")
    if not any_block:
        blocks.append("<p class='muted'>Sin candidatos de pago que superen el mínimo de calidad configurado.</p>")
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


def _changes_period_label(snapshot, day):
    previous_day = snapshot.get("previous_snapshot_date")
    if not previous_day:
        return "sin histórico"
    try:
        d_prev = datetime.fromisoformat(previous_day).date()
        d_today = datetime.fromisoformat(day).date()
    except ValueError:
        return f"vs {previous_day}"
    return "vs ayer" if (d_today - d_prev).days == 1 else f"vs último snapshot · {previous_day}"


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


def _explorer_row(m):
    # A model can be scored by several sources at once — show each independently,
    # never averaged/merged (audit #2 §2).
    qbs = m.get("quality_by_source") or {}
    if qbs:
        best_score = max((q["score"] for q in qbs.values() if q["score"] is not None), default=-1)
        spans = "".join(
            _quality_span(q["score"], None, None, q.get("source_label"),
                          raw_score=q.get("raw_score"), raw_unit=q.get("raw_unit"),
                          match_type=q.get("match_type"))
            for q in qbs.values()
        )
        quality_html = f"<td data-key='equality' data-value='{best_score}' class='quality-multi'>{spans}</td>"
    else:
        quality_html = "<td data-key='equality' data-value='-1' class='muted'>—</td>"
    if m["free"]:
        status_badge, status_cls = "Gratis", "pos"
    elif m.get("pricing_status") == "paid":
        status_badge, status_cls = "Pago", "neutral"
    else:
        status_badge, status_cls = "Desconocido", "neg"
    search_bits = f"{m['model']} {m.get('search_text', m['best_provider'])}".lower()
    search_text = _esc(search_bits)
    routes_json = _esc(json.dumps(m["routes"], ensure_ascii=False))
    n_routes = m["routes_count"]
    route_word = "ruta" if n_routes == 1 else "rutas"
    model_esc = _esc(m["model"])
    known = m["pricing_status"] in _KNOWN_PRICE_STATUSES
    price_in = _price_text(m["input"], m["pricing_status"])
    price_out = _price_text(m["output"], m["pricing_status"])
    cost_text = _cost(m["weighted_cost"]) if known else "—"
    # Sentinel (None -> "-999999" in _num_td) so an unknown price never sorts
    # as if it were the cheapest option in the table.
    in_value, out_value, cost_value = (m["input"], m["output"], m["weighted_cost"]) if known else (None, None, None)
    return (
        f"<tr class='exp-row' data-search='{search_text}' data-pricing-status='{_esc(m['pricing_status'])}'>"
        f"<td><input type='checkbox' class='cmp-check' data-model='{model_esc}' aria-label='Seleccionar {model_esc} para comparar'></td>"
        f"<td class='usage'>"
        f"<button type='button' class='exp-toggle' aria-expanded='false' data-routes='{routes_json}'>"
        f"{model_esc}<span class='exp-count'>{n_routes} {route_word}</span></button></td>"
        f"<td>{_provider_badge(m['best_provider'])}</td>"
        f"{_num_td(cost_value, cost_text, 'ecost')}"
        f"{_num_td(in_value, price_in, 'einput')}"
        f"{_num_td(out_value, price_out, 'eoutput')}"
        f"<td data-key='ecustom' data-value='-999999' class='num'>—</td>"
        f"{quality_html}"
        f"<td><span class='pill {status_cls}'>{status_badge}</span></td>"
        f"</tr>"
    )


def _section_explorer(explorer, task_profiles=None):
    if not explorer:
        return "<p class='muted'>Sin datos de catálogo todavía.</p>"
    rows = "".join(_explorer_row(m) for m in explorer)
    coding = (task_profiles or {}).get("coding", {})
    default_in = coding.get("input_tokens", 30000)
    default_out = coding.get("output_tokens", 6000)
    return (
        "<div class='explorer-controls'>"
        "<input type='search' id='model-search' class='search-input' "
        "placeholder='Buscar modelo, proveedor…' aria-label='Buscar modelo o proveedor'>"
        "<button type='button' id='cmp-btn' class='cmp-btn' disabled>Comparar seleccionados (0)</button>"
        "</div>"
        "<div class='profile-inputs' id='profile-inputs'>"
        "<span class='profile-label'>Perfil personalizado:</span>"
        f"<label>Input tokens <input type='number' id='tok-input' min='0' step='1000' value='{default_in}'></label>"
        f"<label>Output tokens <input type='number' id='tok-output' min='0' step='500' value='{default_out}'></label>"
        "<span class='muted note'>recalcula la columna «Coste personalizado» al vuelo, sin recargar</span>"
        "</div>"
        "<div id='cmp-panel' class='cmp-panel' hidden></div>"
        "<div class='table-scroll'><table class='grid' data-sortable id='explorer-table'>"
        "<thead><tr>"
        "<th></th><th>Modelo</th><th>Proveedor más barato</th>"
        "<th data-key='ecost'>Coste estimado</th><th data-key='einput'>$/M input</th>"
        "<th data-key='eoutput'>$/M output</th><th data-key='ecustom'>Coste personalizado</th>"
        "<th data-key='equality'>Calidad</th><th>Estado</th>"
        "</tr></thead>"
        f"<tbody>{rows}</tbody></table></div>"
        f"<p class='muted note' id='explorer-count'>{len(explorer)} modelos únicos. "
        "Haz clic en un modelo para ver todas sus rutas. Selecciona hasta 4 para compararlos.</p>"
    )


def _section_methodology(config):
    config = config or {}
    anchor = config.get("value_cost_anchor_usd", 0.05)
    profiles = config.get("task_profiles", {})
    profile_rows = []
    for k, p in profiles.items():
        in_tok, out_tok, weight = p.get("input_tokens", 0), p.get("output_tokens", 0), p.get("weight", 0)
        in_text, out_text = f"{in_tok:,}", f"{out_tok:,}"
        profile_rows.append(
            f"<tr><td class='usage'>{LABELS.get(k, k)}</td>"
            f"{_num_td(in_tok, in_text)}{_num_td(out_tok, out_text)}{_num_td(weight, weight)}</tr>"
        )
    rows = "".join(profile_rows)
    return f"""
<div class="methodology">
  <h3>Precios</h3>
  <p>Se descargan directamente de la API pública de cada proveedor configurado, una vez al día. Un
  precio en $0/$0 no se asume gratis: solo cuenta como gratis cuando el proveedor lo declara
  explícitamente (hoy, el sufijo <code>:free</code> de OpenRouter); en cualquier otro caso queda como
  <em>desconocido</em> y no entra en ningún ranking por coste.</p>
  <h3>Identidad de modelo</h3>
  <p>Dos rutas se tratan como el mismo modelo solo cuando su id normalizado coincide exactamente o
  existe una regla de alias que no pierde información de tamaño, fecha o variante del checkpoint
  original. Nunca por similitud de nombre sin más — evita, por ejemplo, fusionar
  <code>DeepSeek-R1</code> con <code>DeepSeek-R1-Distill-Qwen-32B</code>.</p>
  <h3>Benchmarks</h3>
  <p><strong>Aider Polyglot Leaderboard</strong> mide corrección de código con un test fijo
  (pass/fail). <strong>LMArena WebDev Arena</strong> mide preferencia humana generando aplicaciones
  web (rating Elo). Son escalas distintas: nunca se combinan en un único ranking, y la fuente exacta
  se muestra siempre junto al dato, no solo al pasar el ratón por encima.</p>
  <h3>Coste estimado</h3>
  <p>Perfil de tokens fijo por tipo de tarea (editable en <code>config.json</code>):</p>
  <div class="table-scroll"><table class='grid'><thead><tr>
  <th>Uso</th><th>Input tokens</th><th>Output tokens</th><th>Peso</th>
  </tr></thead><tbody>{rows}</tbody></table></div>
  <h3>Radar Value</h3>
  <p>Índice propio de este proyecto — <strong>no es un benchmark</strong>:
  <code>calidad × 10 / sqrt(1 + coste_tarea / {anchor})</code>. Combina calidad medida y coste
  estimado para ordenar por "valor"; el ancla de {anchor} USD/tarea es el punto en el que el coste
  empieza a penalizar.</p>
  <h3>Limitaciones</h3>
  <ul>
    <li>Los precios pueden cambiar durante el día — el snapshot es de un momento dado.</li>
    <li>Un modelo sin benchmark no significa baja calidad: significa que no hay dato fiable todavía.</li>
    <li>Benchmarks distintos no son directamente comparables entre sí.</li>
    <li>Latencia/throughput (cuando existen) pueden variar por región o carga.</li>
    <li>El coste estimado usa un perfil de tokens fijo; tu carga de trabajo real puede diferir.</li>
  </ul>
</div>
"""


def _sparkline(trend, width=560, height=64, title=None):
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
    source_suffix = f" · {_esc(title)}" if title else ""
    return (
        "<div class='spark'>"
        f"<div class='spark-head'>Evolución de <strong>{model_esc}</strong>{source_suffix} "
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

.qcell { display: inline-flex; align-items: center; gap: 7px; flex-wrap: wrap; }
.qbar { width: 36px; height: 5px; border-radius: 3px; background: var(--border); overflow: hidden; flex: none; }
.qbar-fill { display: block; height: 100%; border-radius: 3px; }
.qbar-fill.tier-good { background: var(--pos); }
.qbar-fill.tier-mid { background: var(--accent); }
.qbar-fill.tier-low { background: var(--neg); }
.qval { font-family: var(--font-mono); font-variant-numeric: tabular-nums; color: var(--muted); }
.qsrc {
  font-size: 0.66rem; letter-spacing: .01em; color: var(--muted); background: var(--panel-2, var(--panel));
  border: 1px solid var(--border); border-radius: 999px; padding: 1px 6px; white-space: nowrap;
}
td.quality-multi { display: table-cell; }
td.quality-multi .qcell { display: flex; margin-bottom: 4px; }
td.quality-multi .qcell:last-child { margin-bottom: 0; }

/* ---------- freshness ---------- */
.freshness { display: inline-flex; align-items: center; gap: 6px; }
.freshness .dot { width: 7px; height: 7px; border-radius: 50%; background: var(--muted); flex: none; }
.freshness .dot.fresh { background: var(--pos); }
.freshness .dot.stale { background: var(--accent); }
.freshness .dot.old { background: var(--neg); }

.pill {
  font-family: var(--font-mono); font-size: 0.78rem; font-weight: 600; padding: 3px 9px; border-radius: 100px;
}
.pill.pos { color: var(--pos); background: color-mix(in srgb, var(--pos) 16%, transparent); }
.pill.neg { color: var(--neg); background: color-mix(in srgb, var(--neg) 16%, transparent); }
.pill.neutral { color: var(--muted); background: var(--panel); border: 1px solid var(--border); }

/* ---------- accessibility: focus & keyboard ---------- */
a:focus-visible, button:focus-visible, input:focus-visible,
th[tabindex]:focus-visible, .exp-toggle:focus-visible {
  outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 4px;
}
table.grid[data-sortable] th[data-key][aria-sort="ascending"]::after { content: " ▲"; color: var(--accent); }
table.grid[data-sortable] th[data-key][aria-sort="descending"]::after { content: " ▼"; color: var(--accent); }

/* ---------- explorer / search / compare ---------- */
.explorer-controls { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin-bottom: 16px; }
.search-input {
  flex: 1 1 260px; background: var(--panel); border: 1px solid var(--border); border-radius: 10px;
  padding: 10px 14px; color: var(--text); font-size: 0.9rem; font-family: var(--font-body);
}
.search-input::placeholder { color: var(--muted); }
.cmp-btn {
  font-family: var(--font-body); font-weight: 600; font-size: 0.84rem; padding: 10px 16px; border-radius: 10px;
  border: 1px solid var(--accent); background: color-mix(in srgb, var(--accent) 14%, transparent); color: var(--text);
  cursor: pointer; white-space: nowrap;
}
.cmp-btn:disabled { opacity: 0.4; cursor: not-allowed; border-color: var(--border); background: transparent; }
.exp-toggle {
  background: none; border: none; color: inherit; font: inherit; cursor: pointer; text-align: left;
  display: flex; flex-direction: column; gap: 2px; padding: 0;
}
.exp-toggle:hover { color: var(--accent); }
.exp-count { font-size: 0.7rem; color: var(--muted); font-weight: 400; }
tr.exp-detail td { background: color-mix(in srgb, var(--panel) 60%, transparent); white-space: normal; padding: 12px 16px; }
.exp-routes { display: flex; flex-direction: column; gap: 6px; font-size: 0.82rem; }
.exp-routes .exp-route-row { display: flex; gap: 14px; flex-wrap: wrap; align-items: center; }
tr.hidden-row { display: none; }
.cmp-panel { margin-bottom: 20px; border: 1px solid var(--border); border-radius: 12px; padding: 18px; background: var(--panel); }
.cmp-panel h4 { margin: 0 0 12px; font-size: 0.95rem; }
.profile-inputs {
  display: flex; align-items: center; gap: 16px; flex-wrap: wrap; margin-bottom: 16px; padding: 12px 16px;
  border: 1px dashed var(--border); border-radius: 10px; font-size: 0.82rem;
}
.profile-label { color: var(--muted); font-weight: 600; }
.profile-inputs label { display: flex; align-items: center; gap: 6px; color: var(--muted); }
.profile-inputs input[type="number"] {
  width: 90px; background: var(--bg); border: 1px solid var(--border); border-radius: 6px; padding: 5px 8px;
  color: var(--text); font-family: var(--font-mono); font-size: 0.82rem;
}

/* ---------- methodology ---------- */
.methodology h3 { font-size: 0.92rem; margin: 22px 0 8px; }
.methodology h3:first-child { margin-top: 0; }
.methodology p { color: var(--muted); font-size: 0.88rem; max-width: 72ch; }
.methodology code {
  font-family: var(--font-mono); font-size: 0.82em; background: var(--panel); border: 1px solid var(--border);
  border-radius: 4px; padding: 1px 5px;
}
.methodology ul { color: var(--muted); font-size: 0.88rem; padding-left: 20px; max-width: 72ch; }

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

  // --- sortable tables (mouse + keyboard, aria-sort kept in sync) ---
  document.querySelectorAll('table[data-sortable]').forEach(function (table) {
    var headers = table.querySelectorAll('th[data-key]');
    headers.forEach(function (th) {
      th.setAttribute('tabindex', '0');
      th.setAttribute('role', 'button');
      th.setAttribute('aria-sort', 'none');
      function doSort() {
        var key = th.getAttribute('data-key');
        var dir = th.getAttribute('data-dir') === 'asc' ? 'desc' : 'asc';
        headers.forEach(function (x) { x.removeAttribute('data-dir'); x.setAttribute('aria-sort', 'none'); });
        th.setAttribute('data-dir', dir);
        th.setAttribute('aria-sort', dir === 'asc' ? 'ascending' : 'descending');
        var tbody = table.querySelector('tbody');
        // Collapse any expanded model-explorer detail rows before reordering —
        // a detail row has no sort key and would otherwise land in the wrong place.
        tbody.querySelectorAll('tr.exp-detail').forEach(function (d) { d.remove(); });
        tbody.querySelectorAll('.exp-toggle[aria-expanded="true"]').forEach(function (t) { t.setAttribute('aria-expanded', 'false'); });
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
      }
      th.addEventListener('click', doSort);
      th.addEventListener('keydown', function (ev) {
        if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); doSort(); }
      });
    });
  });

  // --- model explorer: shared element refs (declared once, before any block that uses them) ---
  var explorerTable = document.getElementById('explorer-table');
  var explorerCount = document.getElementById('explorer-count');
  var searchInput = document.getElementById('model-search');

  // --- model explorer: custom token profile recalculates "coste personalizado" live ---
  var tokInput = document.getElementById('tok-input');
  var tokOutput = document.getElementById('tok-output');
  if (tokInput && tokOutput && explorerTable) {
    function recalcCustomCost() {
      var inTok = Math.max(0, parseFloat(tokInput.value) || 0);
      var outTok = Math.max(0, parseFloat(tokOutput.value) || 0);
      var knownStatus = { free: 1, paid: 1, promotional_free: 1 };
      explorerTable.querySelectorAll('tbody tr.exp-row').forEach(function (row) {
        var customCell = row.querySelector('[data-key="ecustom"]');
        if (!customCell) { return; }
        var status = row.getAttribute('data-pricing-status');
        if (!knownStatus[status]) {
          // Never compute a fake cost for a price we don't actually trust.
          customCell.setAttribute('data-value', '-999999');
          customCell.textContent = '—';
          return;
        }
        var inCell = row.querySelector('[data-key="einput"]');
        var outCell = row.querySelector('[data-key="eoutput"]');
        if (!inCell || !outCell) { return; }
        var pIn = parseFloat(inCell.getAttribute('data-value'));
        var pOut = parseFloat(outCell.getAttribute('data-value'));
        var cost = (inTok / 1000000) * pIn + (outTok / 1000000) * pOut;
        customCell.setAttribute('data-value', cost);
        customCell.textContent = '$' + cost.toFixed(5);
      });
    }
    tokInput.addEventListener('input', recalcCustomCost);
    tokOutput.addEventListener('input', recalcCustomCost);
    recalcCustomCost();
  }

  // --- model explorer: search filter ---
  if (searchInput && explorerTable) {
    searchInput.addEventListener('input', function () {
      var needle = searchInput.value.trim().toLowerCase();
      var visible = 0;
      explorerTable.querySelectorAll('tbody tr.exp-row').forEach(function (row) {
        var hay = row.getAttribute('data-search') || '';
        var match = !needle || hay.indexOf(needle) !== -1;
        row.classList.toggle('hidden-row', !match);
        if (match) { visible++; }
        var detail = row.nextElementSibling;
        if (detail && detail.classList.contains('exp-detail')) {
          detail.classList.toggle('hidden-row', !match);
        }
      });
      if (explorerCount) {
        explorerCount.textContent = needle
          ? visible + ' de ' + explorerTable.querySelectorAll('tbody tr.exp-row').length + ' modelos coinciden con "' + searchInput.value.trim() + '".'
          : explorerTable.querySelectorAll('tbody tr.exp-row').length + ' modelos únicos. Haz clic en un modelo para ver todas sus rutas. Selecciona hasta 4 para compararlos.';
      }
    });
  }

  // --- model explorer: expand routes ---
  if (explorerTable) {
    explorerTable.querySelectorAll('.exp-toggle').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var row = btn.closest('tr');
        var open = btn.getAttribute('aria-expanded') === 'true';
        var existing = row.nextElementSibling;
        if (existing && existing.classList.contains('exp-detail')) { existing.remove(); }
        if (open) { btn.setAttribute('aria-expanded', 'false'); return; }
        explorerTable.querySelectorAll('.exp-toggle[aria-expanded="true"]').forEach(function (t) {
          t.setAttribute('aria-expanded', 'false');
          var d = t.closest('tr').nextElementSibling;
          if (d && d.classList.contains('exp-detail')) { d.remove(); }
        });
        btn.setAttribute('aria-expanded', 'true');
        var routes;
        try { routes = JSON.parse(btn.getAttribute('data-routes')); } catch (e) { routes = []; }
        var cols = row.children.length;
        var known = { free: 1, paid: 1, promotional_free: 1 };
        var html = "<div class='exp-routes'>" + routes.map(function (r) {
          var status = r.pricing_status === 'free' ? 'Gratis' : (r.pricing_status === 'paid' ? 'Pago' : 'Desconocido');
          var isKnown = !!known[r.pricing_status];
          var priceText = isKnown ? ("$" + r.input.toFixed(4) + " in / $" + r.output.toFixed(4) + " out") : "— precio no disponible";
          var costText = isKnown ? ("coste estimado $" + r.weighted_cost.toFixed(5)) : "";
          var extras = [];
          if (r.context_length) { extras.push(Math.round(r.context_length / 1000) + "K contexto"); }
          if (r.quantization) { extras.push(escapeHtml(r.quantization)); }
          if (r.latency_p50 != null) { extras.push("latencia p50 " + r.latency_p50 + " ms"); }
          if (r.throughput_p50 != null) { extras.push(r.throughput_p50 + " tok/s"); }
          if (r.uptime_last_1d != null) { extras.push((r.uptime_last_1d * 100).toFixed(2) + "% uptime"); }
          var extrasHtml = extras.length ? "<span class='meta'>" + extras.join(' · ') + "</span>" : "";
          return "<div class='exp-route-row'><strong>" + escapeHtml(r.provider) + "</strong>" +
            "<span class='meta'>" + escapeHtml(r.raw_model) + "</span>" +
            "<span class='meta'>" + priceText + "</span>" +
            (costText ? "<span class='meta'>" + costText + "</span>" : "") +
            extrasHtml +
            "<span class='pill neutral'>" + status + "</span></div>";
        }).join('') + "</div>";
        var tr = document.createElement('tr');
        tr.className = 'exp-detail';
        tr.innerHTML = "<td colspan='" + cols + "'>" + html + "</td>";
        row.parentNode.insertBefore(tr, row.nextSibling);
      });
    });
  }
  function escapeHtml(s) {
    var div = document.createElement('div');
    div.textContent = String(s == null ? '' : s);
    return div.innerHTML;
  }

  // --- model explorer: compare up to 4 selected models ---
  var cmpBtn = document.getElementById('cmp-btn');
  var cmpPanel = document.getElementById('cmp-panel');
  if (explorerTable && cmpBtn && cmpPanel) {
    function selectedChecks() {
      return Array.prototype.slice.call(explorerTable.querySelectorAll('.cmp-check:checked'));
    }
    function refreshCmpBtn() {
      var n = selectedChecks().length;
      cmpBtn.textContent = 'Comparar seleccionados (' + n + ')';
      cmpBtn.disabled = n < 2;
    }
    explorerTable.querySelectorAll('.cmp-check').forEach(function (chk) {
      chk.addEventListener('change', function () {
        if (selectedChecks().length > 4) { chk.checked = false; }
        refreshCmpBtn();
      });
    });
    cmpBtn.addEventListener('click', function () {
      var rows = selectedChecks().map(function (chk) { return chk.closest('tr'); });
      var cells = ['ecost', 'einput', 'eoutput', 'ecustom'];
      var head = '<tr><th>Modelo</th><th>Coste estimado</th><th>$/M input</th><th>$/M output</th><th>Coste personalizado</th><th>Calidad</th><th>Estado</th></tr>';
      var body = rows.map(function (r) {
        var name = r.querySelector('.exp-toggle').firstChild.textContent;
        var tds = cells.map(function (k) {
          var td = r.querySelector('[data-key="' + k + '"]');
          return '<td class="num">' + (td ? td.textContent : '—') + '</td>';
        }).join('');
        var quality = r.querySelector('.qcell');
        var status = r.querySelector('.pill');
        return '<tr><td class="usage">' + escapeHtml(name) + '</td>' + tds +
          '<td>' + (quality ? quality.outerHTML : '—') + '</td>' +
          '<td>' + (status ? status.outerHTML : '—') + '</td></tr>';
      }).join('');
      cmpPanel.innerHTML = '<h4>Comparativa</h4><div class="table-scroll"><table class="grid"><thead>' + head + '</thead><tbody>' + body + '</tbody></table></div>';
      cmpPanel.hidden = false;
    });
  }

  // --- freshness indicator: computed client-side against wall-clock time,
  // since a static page's "now" isn't known at generation time ---
  var freshEl = document.getElementById('freshness');
  if (freshEl) {
    var generatedAt = new Date(freshEl.getAttribute('data-generated-at'));
    if (!isNaN(generatedAt.getTime())) {
      var hours = (Date.now() - generatedAt.getTime()) / 3600000;
      var dot = freshEl.querySelector('.dot');
      var cls = hours < 6 ? 'fresh' : (hours < 24 ? 'stale' : 'old');
      dot.classList.add(cls);
      dot.title = hours < 1
        ? 'hace menos de 1 h'
        : 'hace ' + Math.round(hours) + ' h';
    }
  }

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
<title>Daily AI Radar — {day}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{style}</style>
</head>
<body>
<div class="topbar">
  <span class="brand"><span class="brand-mark"></span>Daily AI Radar</span>
  <span class="freshness" id="freshness" data-generated-at="{generated_at}">
    <span class="dot"></span><span class="freshness-text">Actualizado {generated_label}</span>
  </span>
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
    <p class="lede">Cada mañana comparamos catálogo y precios de varios proveedores contra benchmarks públicos de programación, y ordenamos las opciones por coste estimado de tarea — no por lista de precios sin más.</p>
    <div class="stat-row">
      <div class="stat-tile"><span class="stat-num" data-value="{unique_models}">{unique_models}</span><div class="stat-label">modelos únicos</div></div>
      <div class="stat-tile"><span class="stat-num" data-value="{models_kept}">{models_kept}</span><div class="stat-label">rutas / precios</div></div>
      <div class="stat-tile"><span class="stat-num" data-value="{sources_with_data}">{sources_with_data}</span><div class="stat-label">proveedores de precios</div></div>
      <div class="stat-tile"><span class="stat-num" data-value="{openrouter_routes}">{openrouter_routes}</span><div class="stat-label">rutas OpenRouter analizadas</div></div>
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


def build_html(snapshot, day, has_previous, ai_summary=None, price_trends=None, config=None):
    recs = snapshot["recommendations"]
    price_trends = price_trends or {}
    empty_note = _empty_categories_note(recs)

    # Coding is the only category with any benchmark today; render whichever
    # source(s) have a trend without assuming which one exists.
    coding_trends = (price_trends or {}).get("coding", {})
    sparkline_html = "".join(_sparkline(t, title=t.get("source_label")) for t in coding_trends.values() if t)

    free_table = (
        "<div class='table-scroll'><table class='grid'><thead><tr>"
        "<th>Uso</th><th>Modelo</th><th>Calidad</th><th>Proveedor</th><th>$/M input</th><th>$/M output</th>"
        f"</tr></thead><tbody>{_section_free(recs)}</tbody></table></div>{empty_note}"
    )
    paid_value_table = (
        "<div class='table-scroll'><table class='grid'><thead><tr>"
        "<th>Uso</th><th>Modelo</th><th>Proveedor</th><th>Coste estimado</th><th>$/M input</th><th>$/M output</th>"
        "<th>Calidad</th><th>Radar Value</th></tr></thead>"
        f"<tbody>{_section_paid_value(recs)}</tbody></table></div>{empty_note}"
        + sparkline_html
    )
    paid_quality_table = (
        "<div class='table-scroll'><table class='grid'><thead><tr>"
        "<th>Uso</th><th>Modelo</th><th>Proveedor</th><th>Coste estimado</th><th>$/M input</th><th>$/M output</th>"
        "<th>Calidad</th></tr></thead>"
        f"<tbody>{_section_paid_quality(recs)}</tbody></table></div>{empty_note}"
    )

    raw_blocks = [
        ("Mejor opción gratuita", free_table,
         "«Gratis» solo cuenta cuando el proveedor lo declara explícitamente — un precio 0/0 sin esa "
         "señal se trata como desconocido, no como gratis, y no entra en esta lista."),
        (
            "Mejor relación calidad/precio entre modelos puntuados", paid_value_table,
            "Solo entra un modelo cuando el benchmark de coding lo respalda — un modelo barato "
            "sin score todavía no aparece aquí, aunque merezca la pena; lo verás en las tablas de precio de arriba. "
            "Radar Value es un índice propio (calidad medida × coste estimado), no un benchmark.",
        ),
        (
            "Mayor puntuación entre modelos de pago con benchmark disponible", paid_quality_table,
            "No implica que sea la mejor opción absoluta del mercado — solo la de mayor calidad medida "
            "entre los modelos que tienen benchmark.",
        ),
        (
            "Mismo modelo, ruta más barata", _section_opportunities(snapshot["cross_provider_opportunities"]),
            "Compara el mismo modelo entre proveedores — no es una bajada de precio, es elegir mejor ruta hoy. "
            "Solo se compara cuando la identidad del modelo está confirmada (mismo id normalizado o alias verificado) "
            "y el precio de ambos lados es conocido (no `unknown`/dedicado).",
        ),
        ("Top 5 de pago por calidad/precio", _section_top5(recs), ""),
        (
            f"Movimientos de precio ({_changes_period_label(snapshot, day)})",
            _section_changes(has_previous, snapshot["changes"]["drops"], snapshot["changes"]["increases"]),
            "Solo se compara la misma ruta/proveedor frente al snapshot anterior — nunca dos proveedores distintos, "
            "y un cambio en el perfil de tokens nunca se cuenta como cambio de tarifa.",
        ),
        (
            "Explorador de modelos",
            _section_explorer(snapshot.get("explorer") or [], (config or {}).get("task_profiles")),
            "Catálogo completo, uno por modelo (no por ruta) — busca, expande para ver todas sus rutas y "
            "compara hasta 4 a la vez.",
        ),
        ("Metodología", _section_methodology(config), ""),
    ]
    if ai_summary:
        raw_blocks.append(("Estrategia recomendada para hoy", f"<div class='ai-summary'>{_esc(ai_summary)}</div>", ""))

    blocks = [(f"{i + 1:02d}", title, body, note) for i, (title, body, note) in enumerate(raw_blocks)]
    toc = _toc_html([(idx, title) for idx, title, _body, _note in blocks])
    sections = "".join(_section_html(idx, title, body, note) for idx, title, body, note in blocks)

    generated_at = snapshot.get("generated_at", "")
    try:
        generated_label = datetime.fromisoformat(generated_at).strftime("%d/%m/%Y %H:%M %Z")
    except (ValueError, TypeError):
        generated_label = day

    head = PAGE_HEAD.format(
        day=day,
        generated_at=_esc(generated_at),
        generated_label=_esc(generated_label),
        style=STYLE,
        unique_models=snapshot["stats"].get("unique_models", 0),
        models_kept=snapshot["stats"]["models_kept"],
        sources_with_data=snapshot["stats"]["providers_with_data"],
        openrouter_routes=snapshot["stats"].get("openrouter_routes_analyzed", 0),
        scored_routes=snapshot["stats"]["scored_routes"],
        chips=_status_chips(snapshot["provider_status"]),
        toc=toc,
    )
    tail = PAGE_TAIL.format(script=SCRIPT)
    return head + sections + tail
