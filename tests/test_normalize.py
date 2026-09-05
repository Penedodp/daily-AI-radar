import json
from pathlib import Path

from normalize import canonicalize, canonicalize_with_confidence

ALIASES = json.loads((Path(__file__).resolve().parents[1] / "model_aliases.json").read_text(encoding="utf-8"))


def test_deepseek_r1_distill_sizes_never_collapse():
    a = canonicalize("deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", ALIASES)
    b = canonicalize("deepseek-ai/DeepSeek-R1-Distill-Qwen-32B", ALIASES)
    assert a != b


def test_deepseek_r1_distill_base_model_never_collapses():
    a = canonicalize("deepseek-ai/DeepSeek-R1-Distill-Qwen-32B", ALIASES)
    b = canonicalize("deepseek-ai/DeepSeek-R1-Distill-Llama-70B", ALIASES)
    assert a != b


def test_deepseek_r1_checkpoint_date_never_collapses_with_base():
    a = canonicalize("deepseek/deepseek-r1-0528", ALIASES)
    b = canonicalize("deepseek/deepseek-r1-0528-qwen3-8b", ALIASES)
    assert a != b


def test_deepseek_r1_0528_qwen3_8b_never_collapses_with_distill_1_5b():
    a = canonicalize("deepseek/deepseek-r1-0528-qwen3-8b", ALIASES)
    b = canonicalize("deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", ALIASES)
    assert a != b


def test_qwen3_coder_size_variants_never_collapse():
    a = canonicalize("qwen/qwen3-coder-480b-a35b-instruct", ALIASES)
    b = canonicalize("qwen/qwen3-coder-30b-a3b-instruct", ALIASES)
    assert a != b


def test_bare_qwen3_coder_alias_still_applies_when_unambiguous():
    # No extra size/variant token beyond what the canonical already carries.
    assert canonicalize("qwen/Qwen3-Coder", ALIASES) == "qwen3-coder"


def test_glm_flash_variant_does_not_collapse_into_bare_glm():
    a = canonicalize("z-ai/glm-5.2", ALIASES)
    b = canonicalize("z-ai/glm-5.2-flash", ALIASES)
    assert a != b
    assert a == "glm-5.2"


def test_typographic_variants_of_same_checkpoint_collapse():
    # Same rule (glm-5.2), same distinguishing info either way -> legit merge.
    a = canonicalize("z-ai/GLM_5.2", ALIASES)
    b = canonicalize("z-ai/glm-5.2", ALIASES)
    assert a == b == "glm-5.2"


def test_free_suffix_and_provider_prefix_are_formatting_only():
    a = canonicalize("meta-llama/llama-3.1-8b-instruct:free", ALIASES)
    b = canonicalize("meta-llama/llama-3.1-8b-instruct", ALIASES)
    assert a == b


def test_confidence_is_verified_alias_only_when_a_rule_matched_cleanly():
    _, conf = canonicalize_with_confidence("z-ai/glm-5.2", ALIASES)
    assert conf == "verified_alias"


def test_confidence_is_normalized_id_on_fallback():
    _, conf = canonicalize_with_confidence("meta-llama/llama-3.1-8b-instruct", ALIASES)
    assert conf == "normalized_id"


def test_confidence_is_normalized_id_when_guard_rejects_the_rule():
    _, conf = canonicalize_with_confidence("z-ai/glm-5.2-flash", ALIASES)
    assert conf == "normalized_id"
