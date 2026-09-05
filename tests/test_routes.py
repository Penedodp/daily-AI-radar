from providers.openrouter_routes import route_label
from main import dedup_exact_routes


def test_standard_and_flex_are_distinguishable():
    a = route_label("OpenAI", "standard")
    b = route_label("OpenAI", "flex")
    assert a != b
    assert "OpenAI" in a and "OpenAI" in b


def test_xai_standard_zdr_priority_all_distinguishable():
    labels = {route_label("xAI", tag) for tag in ["standard", "zdr", "priority"]}
    assert len(labels) == 3


def test_tag_matching_provider_name_is_not_duplicated():
    label = route_label("OpenAI", "OpenAI")
    assert label.count("OpenAI") == 1


def test_missing_tag_falls_back_to_bare_provider_label():
    assert route_label("Together", None) == "OpenRouter → Together"


def test_missing_provider_name_falls_back_to_tag():
    assert route_label(None, "baseten") == "OpenRouter → baseten"


def _row(provider, model_id, route_tag=None, quantization=None):
    return {
        "provider": provider, "model_id": model_id,
        "metadata": {"route_tag": route_tag, "quantization": quantization},
    }


def test_dedup_keeps_distinct_quantizations_of_same_route():
    rows = [
        _row("OpenRouter → Baseten", "qwen/qwen3-coder", "baseten", "fp8"),
        _row("OpenRouter → Baseten", "qwen/qwen3-coder", "baseten", "bf16"),
    ]
    deduped, removed = dedup_exact_routes(rows)
    assert removed == 0
    assert len(deduped) == 2


def test_dedup_removes_true_exact_duplicate_route():
    rows = [
        _row("OpenRouter → Baseten", "qwen/qwen3-coder", "baseten", "fp8"),
        _row("OpenRouter → Baseten", "qwen/qwen3-coder", "baseten", "fp8"),
    ]
    deduped, removed = dedup_exact_routes(rows)
    assert removed == 1
    assert len(deduped) == 1
