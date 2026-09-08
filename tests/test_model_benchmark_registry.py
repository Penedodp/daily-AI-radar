from main import build_model_benchmark_registry


def _row(canonical, entity_type="model", route_quality=None):
    return {
        "canonical_model": canonical, "entity_type": entity_type,
        "_route_quality_by_source": route_quality or {},
    }


def test_two_routes_of_same_model_share_one_registry_entry_even_if_only_one_matched():
    """A model's cheaper route might have a raw slug that didn't fuzzy-match
    the benchmark leaderboard while a pricier route of the SAME canonical
    model did — both must end up seeing the same benchmark, not just
    whichever route happened to match."""
    matched_route = _row("qwen3.8-27b", route_quality={
        "aider_polyglot": {"scores": {"coding": 7.0}, "match_ratio": 0.98},
    })
    unmatched_route = _row("qwen3.8-27b", route_quality={})
    registry = build_model_benchmark_registry([matched_route, unmatched_route])
    assert registry["qwen3.8-27b"]["aider_polyglot"]["scores"]["coding"] == 7.0


def test_higher_confidence_match_wins_for_the_same_source():
    low = _row("glm-5.2", route_quality={
        "aider_polyglot": {"scores": {"coding": 5.0}, "match_ratio": 0.94},
    })
    high = _row("glm-5.2", route_quality={
        "aider_polyglot": {"scores": {"coding": 8.0}, "match_ratio": 0.999},
    })
    registry = build_model_benchmark_registry([low, high])
    assert registry["glm-5.2"]["aider_polyglot"]["scores"]["coding"] == 8.0


def test_router_rows_never_contribute_to_the_registry():
    router = _row("openrouter/free", entity_type="router", route_quality={
        "aider_polyglot": {"scores": {"coding": 9.9}, "match_ratio": 1.0},
    })
    registry = build_model_benchmark_registry([router])
    assert "openrouter/free" not in registry


def test_route_quality_field_is_removed_after_registry_build():
    row = _row("glm-5.2", route_quality={"aider_polyglot": {"scores": {"coding": 5.0}, "match_ratio": 1.0}})
    build_model_benchmark_registry([row])
    assert "_route_quality_by_source" not in row
