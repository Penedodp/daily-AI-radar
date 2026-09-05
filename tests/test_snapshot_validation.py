"""End-to-end regression fixture covering the cases from both audit plans:
model identity, pricing status, Aider/WebDev kept as separate rankings,
route labeling, and snapshot validation (errors vs warnings)."""
from normalize import canonicalize
from scoring import compute_pricing_status, costs_by_task, weighted_daily_cost, value_score, is_free
from main import (
    recommendations, cross_provider_opportunities, validate_snapshot,
    build_explorer, compact, route_key, dedup_exact_routes,
)
from report_html import build_html

ALIASES = {"rules": [{"pattern": "(?i)deepseek.*r1", "canonical": "deepseek-r1"}]}
TASK_PROFILES = {
    "coding": {"input_tokens": 30000, "output_tokens": 6000, "weight": 1.0},
}
CONFIG = {"paid_min_quality": {"coding": 0}, "cross_provider_min_saving_pct": 5, "value_cost_anchor_usd": 0.05}


def _raw(provider, source, model_id, inp, out, metadata=None):
    return {
        "provider": provider, "source": source, "model_id": model_id, "name": model_id,
        "input_usd_per_million": inp, "output_usd_per_million": out,
        "context_length": 32000, "metadata": metadata or {},
    }


def _build_models(raw_rows, bench_matches_by_route):
    """bench_matches_by_route: {route_key: {source: bq_dict}}"""
    models = []
    for row in raw_rows:
        row["canonical_model"] = canonicalize(row["model_id"], ALIASES)
        row["pricing_status"] = compute_pricing_status(row)
        matches = bench_matches_by_route.get(route_key(row), {})
        row["quality_by_source"] = {}
        for source, bq in matches.items():
            row["quality_by_source"][source] = {
                "label": bq["label"], "source_label": bq["source_label"],
                "scores": dict(bq["scores"]), "match_ratio": 1.0, "match_type": "exact",
            }
        row["costs_by_task"] = costs_by_task(row, TASK_PROFILES)
        row["weighted_cost"] = weighted_daily_cost(row, TASK_PROFILES)
        row["value_scores"] = {}
        for source, q in row["quality_by_source"].items():
            row["value_scores"][source] = {}
            sc = q["scores"].get("coding")
            if sc is not None:
                row["value_scores"][source]["coding"] = value_score(
                    sc, row["costs_by_task"]["coding"], CONFIG["value_cost_anchor_usd"],
                )
        row["change_pct"] = None
        models.append(row)
    return models


def _fixture_models():
    raw = [
        # two DeepSeek R1 variants that a broad alias rule alone would wrongly merge
        _raw("DeepSeek", "openrouter", "deepseek/deepseek-r1", 0.5, 2.0),
        _raw("DeepSeek", "openrouter", "deepseek/deepseek-r1-distill-llama-70b", 0.1, 0.4),
        # a genuinely free model (explicit :free signal)
        _raw("OpenRouter", "openrouter", "meta-llama/llama-3.1-8b-instruct:free", 0, 0),
        # a 0/0 model with no free signal (e.g. Together "dedicated"-style catalog entry)
        _raw("Together AI", "together", "some-org/dedicated-model", 0, 0),
        # scored ONLY by Aider
        _raw("OpenRouter", "openrouter", "anthropic/claude-3.5-sonnet", 3.0, 15.0),
        # scored ONLY by LMArena
        _raw("OpenRouter", "openrouter", "z-ai/glm-5.2-flash", 0.075, 0.25),
        # scored by BOTH — must still rank in two independent lists, never merged
        _raw("OpenRouter", "openrouter", "qwen/qwen3-max", 1.0, 3.0),
        # two OpenAI routes distinguished only by tag
        _raw("OpenRouter → OpenAI", "openrouter-route", "openai/gpt-5.5", 1.0, 4.0),
        _raw("OpenRouter → OpenAI (flex)", "openrouter-route", "openai/gpt-5.5", 0.6, 2.4),
        # two xAI routes distinguished only by tag
        _raw("OpenRouter → xAI", "openrouter-route", "x-ai/grok-4.5", 2.0, 8.0),
        _raw("OpenRouter → xAI (zdr)", "openrouter-route", "x-ai/grok-4.5", 2.5, 10.0),
        # unscored model
        _raw("OpenRouter", "openrouter", "some/unscored-model", 0.2, 0.8),
        # a route with latency/throughput metadata
        _raw("OpenRouter → Baseten", "openrouter-route", "qwen/qwen3-coder", 0.3, 1.2,
             metadata={"latency_p50": 420, "throughput_p50": 55}),
    ]
    bench = {
        "OpenRouter::anthropic/claude-3.5-sonnet": {
            "aider_polyglot": {"label": "claude-3.5-sonnet", "source_label": "Aider Polyglot Leaderboard",
                                "scores": {"coding": 7.4}},
        },
        "OpenRouter::z-ai/glm-5.2-flash": {
            "lmarena_webdev": {"label": "glm-5.2-flash", "source_label": "LMArena WebDev Arena",
                                "scores": {"coding": 8.2}},
        },
        "OpenRouter::qwen/qwen3-max": {
            "aider_polyglot": {"label": "qwen3-max", "source_label": "Aider Polyglot Leaderboard",
                                "scores": {"coding": 6.0}},
            "lmarena_webdev": {"label": "qwen3-max", "source_label": "LMArena WebDev Arena",
                                "scores": {"coding": 9.0}},
        },
    }
    return _build_models(raw, bench)


def test_deepseek_r1_variants_are_not_compared_as_same_model():
    models = _fixture_models()
    r1 = next(r for r in models if r["model_id"] == "deepseek/deepseek-r1")
    distill = next(r for r in models if r["model_id"] == "deepseek/deepseek-r1-distill-llama-70b")
    assert r1["canonical_model"] != distill["canonical_model"]
    opportunities = cross_provider_opportunities(models, CONFIG)
    for o in opportunities:
        assert not ({r1["canonical_model"], distill["canonical_model"]} <= {o["cheapest"]["model"], o["next"]["model"]})


def test_dedicated_style_zero_price_never_shows_as_free():
    models = _fixture_models()
    dedicated = next(r for r in models if r["model_id"] == "some-org/dedicated-model")
    assert dedicated["pricing_status"] == "unknown"
    assert is_free(dedicated) is False


def test_aider_and_webdev_never_rank_against_each_other():
    """The core fix of audit #2: a model scored only by Aider (7.4) and one
    scored only by WebDev (8.2) must land in two SEPARATE rankings — never
    one list where 8.2 > 7.4 implies WebDev is simply 'better'."""
    models = _fixture_models()
    recs = recommendations(models, CONFIG)
    sources = recs["coding"]["sources"]
    assert set(sources.keys()) == {"aider_polyglot", "lmarena_webdev"}

    aider_value_models = {r["model"] for r in sources["aider_polyglot"]["top_paid_value"]}
    webdev_value_models = {r["model"] for r in sources["lmarena_webdev"]["top_paid_value"]}
    claude = canonicalize("anthropic/claude-3.5-sonnet", ALIASES)
    glm = canonicalize("z-ai/glm-5.2-flash", ALIASES)
    assert claude in aider_value_models
    assert glm in webdev_value_models
    # claude (Aider-only) must not appear in the WebDev ranking at all, and vice versa
    assert claude not in webdev_value_models
    assert glm not in aider_value_models


def test_model_scored_by_both_sources_appears_independently_in_both():
    models = _fixture_models()
    recs = recommendations(models, CONFIG)
    qwen = canonicalize("qwen/qwen3-max", ALIASES)
    aider_models = {r["model"] for r in recs["coding"]["sources"]["aider_polyglot"]["top_paid_value"]}
    webdev_models = {r["model"] for r in recs["coding"]["sources"]["lmarena_webdev"]["top_paid_value"]}
    assert qwen in aider_models
    assert qwen in webdev_models
    # and its score/value differ per source, proving they weren't averaged into one
    aider_pick = next(r for r in recs["coding"]["sources"]["aider_polyglot"]["top_paid_value"] if r["model"] == qwen)
    webdev_pick = next(r for r in recs["coding"]["sources"]["lmarena_webdev"]["top_paid_value"] if r["model"] == qwen)
    assert aider_pick["quality_score"] == 6.0
    assert webdev_pick["quality_score"] == 9.0


def test_openai_and_xai_routes_stay_distinguishable_by_provider_label():
    models = _fixture_models()
    providers = {r["provider"] for r in models if "gpt-5.5" in r["model_id"]}
    assert providers == {"OpenRouter → OpenAI", "OpenRouter → OpenAI (flex)"}
    xai_providers = {r["provider"] for r in models if "grok-4.5" in r["model_id"]}
    assert xai_providers == {"OpenRouter → xAI", "OpenRouter → xAI (zdr)"}


def test_validate_snapshot_has_no_errors_on_clean_fixture():
    models = _fixture_models()
    errors, warnings = validate_snapshot(models)
    assert errors == []
    # unscored + dedicated/unknown rows are expected, routine conditions -> warnings, not errors
    assert any("unknown" in w for w in warnings)
    assert any("sin ningún benchmark" in w for w in warnings)


def test_validate_snapshot_flags_invalid_price_as_error():
    models = _fixture_models()
    broken = dict(models[0])
    broken["input_usd_per_million"] = -5.0
    errors, _warnings = validate_snapshot(models + [broken])
    assert any("precio inválido" in e for e in errors)


def test_validate_snapshot_flags_size_mismatch_under_same_canonical_as_error():
    a = _raw("Prov", "openrouter", "org/model-32b", 1.0, 2.0)
    b = _raw("Prov", "openrouter", "org/model-70b", 1.0, 2.0)
    models = _build_models([a, b], {})
    # Force both under the same (wrong) canonical, simulating an alias bug.
    for r in models:
        r["canonical_model"] = "model"
    errors, _warnings = validate_snapshot(models)
    assert any("tamaños de modelo distintos" in e for e in errors)


def test_dedup_exact_routes_removes_literal_duplicates():
    rows = [
        _raw("OpenRouter", "openrouter", "a/b", 1.0, 2.0),
        _raw("OpenRouter", "openrouter", "a/b", 1.0, 2.0),  # exact duplicate
        _raw("OpenRouter", "openrouter", "a/c", 1.0, 2.0),
    ]
    deduped, removed = dedup_exact_routes(rows)
    assert removed == 1
    assert len(deduped) == 2


def test_explorer_groups_by_canonical_model_not_by_route():
    models = _fixture_models()
    explorer = build_explorer(models)
    gpt_entry = next(m for m in explorer if m["model"] == canonicalize("openai/gpt-5.5", ALIASES))
    assert gpt_entry["routes_count"] == 2


def test_dashboard_builds_without_error_and_never_ranks_sources_together():
    models = _fixture_models()
    recs = recommendations(models, CONFIG)
    opportunities = cross_provider_opportunities(models, CONFIG)
    explorer = build_explorer(models)
    snapshot = {
        "generated_at": "2026-09-05T09:00:00+01:00",
        "previous_snapshot_date": None,
        "provider_status": {"openrouter": {"status": "ok", "count": len(models)}},
        "stats": {
            "raw_rows": len(models), "duplicate_routes_removed": 0,
            "models_kept": len(models), "models_filtered": 0,
            "unique_models": len({r["canonical_model"] for r in models}),
            "providers_with_data": 1, "benchmarks_active": 2, "openrouter_routes_analyzed": 3,
            "scored_routes": sum(1 for r in models if r.get("quality_by_source")),
            "unknown_price_routes": sum(1 for r in models if r.get("pricing_status") == "unknown"),
        },
        "recommendations": recs,
        "cross_provider_opportunities": opportunities,
        "changes": {"drops": [], "increases": []},
        "models": models,
        "explorer": explorer,
        "validation_warnings": [],
    }
    html = build_html(snapshot, "2026-09-05", has_previous=False, config=CONFIG)
    assert "Aider" in html
    assert "WebDev Arena" in html
    assert "OpenRouter → OpenAI (flex)" in html
    assert "8.2" in html and "7.4" in html
