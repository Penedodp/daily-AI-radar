import re

import report_html
from report_html import (
    build_html, _explorer_row, _price_text, _format_context_tokens, _provider_badge,
    _section_free, _section_paid_value, _section_paid_quality,
)


def test_explorer_table_is_declared_before_first_use_in_script():
    """Regression for audit #2 §8: `explorerTable` was read (in the custom
    token-profile block) before its `var explorerTable = ...` declaration.
    `var` hoisting made it silently `undefined`, so the calculator never ran.
    This statically asserts the declaration now comes first in the script."""
    script = report_html.SCRIPT
    declare_idx = script.index("var explorerTable = document.getElementById")
    earlier_uses = [m.start() for m in re.finditer(r"\bexplorerTable\b", script) if m.start() < declare_idx]
    assert earlier_uses == [], (
        "explorerTable is referenced before its declaration in SCRIPT — "
        "the custom cost calculator will silently no-op"
    )


def test_unknown_price_never_renders_as_zero_dollars():
    assert _price_text(0, "unknown") == "—"
    assert _price_text(0, "paid") == "$0.0000"  # a genuinely-priced $0 edge case still renders
    assert _price_text(0, "free") == "$0.0000"


def test_explorer_row_shows_dash_not_fake_price_for_unknown_status():
    model = {
        "model": "some/unknown-model", "best_provider": "Together AI", "routes_count": 1,
        "routes": [], "weighted_cost": 0.0, "input": 0.0, "output": 0.0,
        "context_length": None, "free": False, "pricing_status": "unknown",
        "quality_by_source": {}, "search_text": "together ai",
    }
    html = _explorer_row(model)
    assert "$0.0000" not in html
    assert "data-value='-999999'" in html


def _empty_row_span(html):
    """Sum of column widths in the single fallback <tr>: 1 (the plain <td>)
    plus whatever the colspan says."""
    colspan = re.search(r"colspan='(\d+)'", html)
    return 1 + (int(colspan.group(1)) if colspan else 0)


def test_free_table_empty_row_colspan_matches_header_column_count():
    # PRE_BENCH_V2_FINAL_CLEANUP #37: "Uso, Modelo, Calidad, Proveedor, $/M input, $/M output" = 6 columns.
    assert _empty_row_span(_section_free({})) == 6


def test_paid_value_table_empty_row_colspan_matches_header_column_count():
    # "Uso, Modelo, Proveedor, Coste, $/M input, $/M output, Calidad, Radar Value" = 8 columns.
    assert _empty_row_span(_section_paid_value({})) == 8


def test_paid_quality_table_empty_row_colspan_matches_header_column_count():
    # "Uso, Modelo, Proveedor, Coste, $/M input, $/M output, Calidad" = 7 columns.
    assert _empty_row_span(_section_paid_quality({})) == 7


def test_branding_is_daily_ai_radar_everywhere():
    snapshot = _minimal_snapshot()
    html = build_html(snapshot, "2026-09-05", has_previous=False, config={})
    assert "Daily AI Radar" in html
    assert "AI Price Radar" not in html


def _minimal_snapshot():
    return {
        "generated_at": "2026-09-05T09:00:00+01:00",
        "previous_snapshot_date": None,
        "provider_status": {},
        "stats": {
            "unique_models": 0, "models_kept": 0, "providers_with_data": 0,
            "openrouter_routes_analyzed": 0, "scored_routes": 0,
        },
        "recommendations": {cat: {"sources": {}} for cat in report_html.LABELS},
        "cross_provider_opportunities": [],
        "changes": {"drops": [], "increases": []},
        "models": [],
        "explorer": [],
        "validation_warnings": [],
    }


def test_build_html_with_no_data_does_not_crash_and_shows_placeholder():
    html = build_html(_minimal_snapshot(), "2026-09-05", has_previous=False, config={})
    assert "Próximamente" in html


def test_context_tokens_format_as_round_units_not_kilobyte_overflow():
    assert _format_context_tokens(32768) == "32K"
    assert _format_context_tokens(65536) == "64K"
    assert _format_context_tokens(131072) == "128K"
    assert _format_context_tokens(262144) == "256K"
    assert _format_context_tokens(1048576) == "1M"
    assert _format_context_tokens(2097152) == "2M"
    assert "1049K" not in _format_context_tokens(1048576)


def test_provider_initials_ignore_parenthetical_slug_suffix():
    html = _provider_badge("Darkbloom (darkbloom/fp4)")
    assert ">D<" in html
    assert ">D(<" not in html


def test_provider_initials_use_both_words_for_two_word_names():
    html = _provider_badge("Example Cloud")
    assert ">EC<" in html
