from providers.openrouter_routes import route_label
from main import dedup_exact_routes, route_identity


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


def _route_row(model_id, provider_name, route_tag=None, quantization=None):
    return {
        "source": "openrouter-route", "provider": route_label(provider_name, route_tag),
        "model_id": model_id,
        "metadata": {"route_tag": route_tag, "provider_name": provider_name, "quantization": quantization},
    }


def test_dedup_keeps_distinct_quantizations_of_same_route():
    rows = [
        _route_row("qwen/qwen3-coder", "Baseten", "baseten", "fp8"),
        _route_row("qwen/qwen3-coder", "Baseten", "baseten", "bf16"),
    ]
    deduped, removed = dedup_exact_routes(rows)
    assert removed == 0
    assert len(deduped) == 2


def test_dedup_removes_true_exact_duplicate_route():
    rows = [
        _route_row("qwen/qwen3-coder", "Baseten", "baseten", "fp8"),
        _route_row("qwen/qwen3-coder", "Baseten", "baseten", "fp8"),
    ]
    deduped, removed = dedup_exact_routes(rows)
    assert removed == 1
    assert len(deduped) == 1


def test_route_identity_ignores_synthesized_display_label():
    """Two rows with different display labels (one includes the tag in
    parentheses, one wouldn't if tag==provider_name) but the same underlying
    provider_name+tag+quantization must still be the same identity."""
    a = {"source": "openrouter-route", "provider": "OpenRouter → OpenAI (flex)",
         "model_id": "openai/gpt-5.5", "metadata": {"provider_name": "OpenAI", "route_tag": "flex", "quantization": None}}
    b = dict(a, provider="OpenRouter -> OpenAI [flex]")  # same underlying route, cosmetically different label
    assert route_identity(a) == route_identity(b)


def test_route_identity_distinguishes_standard_vs_flex():
    a = {"source": "openrouter-route", "provider": "x", "model_id": "openai/gpt-5.5",
         "metadata": {"provider_name": "OpenAI", "route_tag": "standard", "quantization": None}}
    b = {"source": "openrouter-route", "provider": "x", "model_id": "openai/gpt-5.5",
         "metadata": {"provider_name": "OpenAI", "route_tag": "flex", "quantization": None}}
    assert route_identity(a) != route_identity(b)


def test_route_identity_distinguishes_xai_zdr_priority():
    tags = ["standard", "zdr", "priority"]
    identities = {
        route_identity({"source": "openrouter-route", "provider": "x", "model_id": "x-ai/grok-4.5",
                         "metadata": {"provider_name": "xAI", "route_tag": t, "quantization": None}})
        for t in tags
    }
    assert len(identities) == 3


def test_route_identity_distinguishes_quantization():
    a = {"source": "openrouter-route", "provider": "x", "model_id": "m", "metadata": {"provider_name": "Darkbloom", "route_tag": "darkbloom", "quantization": "fp4"}}
    b = {"source": "openrouter-route", "provider": "x", "model_id": "m", "metadata": {"provider_name": "Darkbloom", "route_tag": "darkbloom", "quantization": "fp8"}}
    assert route_identity(a) != route_identity(b)
