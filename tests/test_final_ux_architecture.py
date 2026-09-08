"""FINAL_PRE_BENCH_V2_UX_ARCHITECTURE regression tests: router exclusion from
model-level counts/comparisons, persisted registries, stats naming, and the
Radar/Explorer/Methodology page split."""
from main import (
    build_explorer, build_free_today, build_model_benchmark_registry,
)
from report_html import (
    build_html, build_explorer_page, build_methodology_page, build_benchmarks_placeholder_page,
)


def _row(model_id, provider, pricing_status, entity_type="model", quality_by_source=None,
         context_length=None, canonical_model=None):
    return {
        "canonical_model": canonical_model or model_id, "model_id": model_id, "provider": provider,
        "pricing_status": pricing_status, "entity_type": entity_type,
        "quality_by_source": quality_by_source or {}, "context_length": context_length,
        "input_usd_per_million": 0, "output_usd_per_million": 0, "weighted_cost": 0,
        "free_limits": None, "identity_confidence": "normalized_id",
    }


def test_openrouter_free_router_excluded_from_explorer():
    models = [
        _row("glm-5.2", "OpenRouter", "free"),
        _row("openrouter/free", "OpenRouter", "free_router", entity_type="router"),
    ]
    explorer = build_explorer(models)
    assert all(m["model"] != "openrouter/free" for m in explorer)


def test_openrouter_free_router_excluded_from_free_today_grouping_but_still_listed():
    """The router IS still shown (it's a real, usable $0 service) but never
    grouped/counted as if it were one more free MODEL."""
    models = [
        _row("glm-5.2", "OpenRouter", "free"),
        _row("openrouter/free", "OpenRouter", "free_router", entity_type="router"),
    ]
    free_today = build_free_today(models)
    model_rows = [m for m in free_today if m["entity_type"] == "model"]
    router_rows = [m for m in free_today if m["entity_type"] == "router"]
    assert len(model_rows) == 1
    assert len(router_rows) == 1


def test_compact_output_always_carries_route_identity():
    """FINAL_PRE_BENCH_V2_UX_ARCHITECTURE #15: the CURRENT (today's) point in
    Best Market History must carry route_identity just like every historical
    point — compact() is what feeds that current point, so it must always
    include it."""
    from main import compact
    row = {
        "canonical_model": "glm-5.2", "model_id": "z-ai/glm-5.2", "provider": "OpenRouter",
        "source": "openrouter", "pricing_status": "paid", "identity_confidence": "verified_alias",
        "input_usd_per_million": 0.5, "output_usd_per_million": 1.5, "weighted_cost": 0.02,
        "context_length": 131072, "metadata": {},
    }
    result = compact(row)
    assert result["route_identity"]
    assert result["route_identity"].startswith("route_identity_v1::")


def test_router_never_enters_the_model_benchmark_registry():
    router = _row("openrouter/free", "OpenRouter", "free_router", entity_type="router")
    router["_route_quality_by_source"] = {"aider_polyglot": {"scores": {"coding": 9.9}, "match_ratio": 1.0}}
    registry = build_model_benchmark_registry([router])
    assert "openrouter/free" not in registry


def _minimal_snapshot():
    return {
        "generated_at": "2026-09-08T09:00:00+01:00",
        "previous_snapshot_date": None,
        "provider_status": {},
        "stats": {
            "unique_models": 0, "models_kept": 0, "providers_with_data": 0,
            "openrouter_routes_analyzed": 0, "models_with_benchmark": 0,
        },
        "recommendations": {"coding": {"sources": {}}, "agentic": {"sources": {}},
                             "reasoning": {"sources": {}}, "general": {"sources": {}}},
        "cross_provider_opportunities": [],
        "changes": {"drops": [], "increases": []},
        "models": [],
        "explorer": [],
        "free_today": [],
        "validation_warnings": [],
    }


def test_radar_page_no_longer_embeds_the_full_catalog_table():
    html = build_html(_minimal_snapshot(), "2026-09-08", has_previous=False, config={})
    assert "id='explorer-table'" not in html
    assert "explorer.html" in html  # the CTA link out to the full catalog


def test_radar_page_has_nav_with_radar_active():
    html = build_html(_minimal_snapshot(), "2026-09-08", has_previous=False, config={})
    assert "href='index.html' class=\"active\"" in html
    assert "aria-current=\"page\">Radar</a>" in html


def test_explorer_page_has_the_full_catalog_table_and_nav():
    html = build_explorer_page(_minimal_snapshot(), "2026-09-08", config={})
    assert "explorer-table" in html or "Sin datos de catálogo" in html
    assert "explorer.html" in html
    assert "page-size-btn" in html


def test_methodology_page_has_data_health_and_nav():
    html = build_methodology_page(_minimal_snapshot(), "2026-09-08", config={})
    assert "Data Health" in html
    assert "methodology.html" in html


def test_benchmarks_placeholder_page_says_proximamente():
    html = build_benchmarks_placeholder_page("2026-09-08", generated_at="2026-09-08T09:00:00+01:00")
    assert "Benchmark Engine v2" in html
    assert "benchmarks.html" in html
