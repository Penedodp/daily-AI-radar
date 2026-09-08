from scoring import compute_pricing_status, is_router_entity, is_free_available, is_free
from main import free_limits_for, build_free_today, build_explorer


def test_openrouter_free_router_is_classified_as_router_not_model():
    row = {"model_id": "openrouter/free", "input_usd_per_million": 0, "output_usd_per_million": 0}
    assert is_router_entity(row) is True
    assert compute_pricing_status(row) == "free_router"


def test_real_free_model_is_not_a_router():
    row = {"model_id": "meta-llama/llama-3.1-8b-instruct:free", "input_usd_per_million": 0, "output_usd_per_million": 0}
    assert is_router_entity(row) is False
    assert compute_pricing_status(row) == "free"


def test_free_router_is_free_available_but_not_is_free():
    row = {"pricing_status": "free_router"}
    assert is_free(row) is False  # never counted as a scoreable free MODEL
    assert is_free_available(row) is True  # but it IS something you can call for $0 today


def test_free_limits_for_router_uses_dedicated_config_entry():
    free_tiers = {
        "OpenRouter Free Router": {"provider": "OpenRouter Free Router", "status": "free_router"},
        "OpenRouter": {"provider": "OpenRouter", "status": "free_tier"},
    }
    router_row = {"entity_type": "router", "pricing_status": "free_router", "provider": "OpenRouter"}
    model_row = {"entity_type": "model", "pricing_status": "free", "provider": "OpenRouter"}
    assert free_limits_for(router_row, free_tiers)["status"] == "free_router"
    assert free_limits_for(model_row, free_tiers)["status"] == "free_tier"


def test_free_limits_for_paid_row_is_none():
    free_tiers = {"OpenRouter": {"provider": "OpenRouter", "status": "free_tier"}}
    paid_row = {"entity_type": "model", "pricing_status": "paid", "provider": "OpenRouter"}
    assert free_limits_for(paid_row, free_tiers) is None


def _model_row(model_id, provider, pricing_status, entity_type="model", quality_by_source=None, context_length=None):
    return {
        "canonical_model": model_id, "model_id": model_id, "provider": provider,
        "pricing_status": pricing_status, "entity_type": entity_type,
        "quality_by_source": quality_by_source or {}, "context_length": context_length,
        "input_usd_per_million": 0, "output_usd_per_million": 0, "weighted_cost": 0,
        "free_limits": None, "identity_confidence": "normalized_id",
    }


def test_free_today_includes_unscored_free_models():
    models = [
        _model_row("glm-5.2", "OpenRouter", "free", context_length=131072),
        _model_row("some-paid-model", "OpenRouter", "paid"),
    ]
    free_today = build_free_today(models)
    assert len(free_today) == 1
    assert free_today[0]["model"] == "glm-5.2"
    assert free_today[0]["quality_by_source"] == {}


def test_free_today_never_reduces_two_benchmark_sources_to_a_single_max():
    row = _model_row("glm-5.2", "OpenRouter", "free", context_length=131072, quality_by_source={
        "aider_polyglot": {"scores": {"coding": 3.0}, "source_label": "Aider Polyglot Leaderboard"},
        "lmarena_webdev": {"scores": {"coding": 9.0}, "source_label": "LMArena WebDev Arena"},
    })
    free_today = build_free_today([row])
    qbs = free_today[0]["quality_by_source"]
    assert set(qbs) == {"aider_polyglot", "lmarena_webdev"}
    assert qbs["aider_polyglot"]["score"] == 3.0
    assert qbs["lmarena_webdev"]["score"] == 9.0


def test_free_today_groups_multiple_free_routes_under_one_model_row():
    models = [
        _model_row("glm-5.2", "OpenRouter", "free", context_length=131072),
        _model_row("glm-5.2", "Novita", "free", context_length=65536),
    ]
    free_today = build_free_today(models)
    assert len(free_today) == 1
    assert free_today[0]["routes_count"] == 2
    assert {r["provider"] for r in free_today[0]["routes"]} == {"OpenRouter", "Novita"}


def test_free_today_includes_router_once_and_lists_it_last():
    models = [
        _model_row("glm-5.2", "OpenRouter", "free", context_length=131072),
        _model_row("openrouter/free", "OpenRouter", "free_router", entity_type="router"),
    ]
    free_today = build_free_today(models)
    assert len(free_today) == 2
    assert free_today[-1]["entity_type"] == "router"


def test_explorer_excludes_routers_entirely():
    models = [
        _model_row("glm-5.2", "OpenRouter", "free"),
        _model_row("openrouter/free", "OpenRouter", "free_router", entity_type="router"),
    ]
    explorer = build_explorer(models)
    assert all(m["model"] != "openrouter/free" for m in explorer)
    assert len(explorer) == 1
