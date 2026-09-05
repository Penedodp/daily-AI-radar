from quality_bench import _fingerprint, match_models


def _row(provider, model_id):
    return {"provider": provider, "model_id": model_id, "name": model_id, "metadata": {}}


def _entries(*names_scores):
    return [{"model": n, "score": s, "numeric": _fingerprint(n)[0], "text_key": _fingerprint(n)[1]} for n, s in names_scores]


def test_preview_never_inherits_stable_score():
    entries = _entries(("hy3", 8.0))
    rows = [_row("p", "org/hy3-preview")]
    assert match_models(entries, rows, "src") == {}


def test_thinking_suffix_is_not_equivalent_to_base():
    entries = _entries(("model", 7.0))
    rows = [_row("p", "org/model-thinking")]
    assert match_models(entries, rows, "src") == {}


def test_base_and_instruct_are_distinct():
    entries = _entries(("model-base", 6.0))
    rows = [_row("p", "org/model-instruct")]
    assert match_models(entries, rows, "src") == {}


def test_claude_3_vs_3_5_never_merge():
    entries = _entries(("claude-3.5-haiku", 9.0))
    rows = [_row("p", "anthropic/claude-3-haiku")]
    assert match_models(entries, rows, "src") == {}


def test_typographic_variants_do_match():
    entries = _entries(("Qwen3 32B", 7.5))
    rows = [_row("p", "qwen/qwen3-32b")]
    result = match_models(entries, rows, "src")
    assert result and list(result.values())[0]["scores"]["coding"] == 7.5


def test_different_checkpoint_dates_never_merge():
    entries = _entries(("DeepSeek V3 (0324)", 8.5))
    rows = [_row("p", "deepseek/deepseek-v3-0824")]
    assert match_models(entries, rows, "src") == {}


def test_glued_and_hyphenated_dates_are_treated_as_equivalent():
    entries = _entries(("GPT-4o (2024-08-06)", 9.1))
    rows = [_row("p", "openai/gpt-4o-20240806")]
    result = match_models(entries, rows, "src")
    assert result and list(result.values())[0]["scores"]["coding"] == 9.1
