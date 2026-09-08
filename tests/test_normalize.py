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


def test_qwen_3_8_27b_dash_and_dot_spellings_are_verified_equivalent():
    a = canonicalize("qwen/qwen3.8-27b", ALIASES)
    b = canonicalize("provider/qwen-3-8-27b", ALIASES)
    assert a == b == "qwen3.8-27b"


def test_qwen_3_8_max_dash_and_dot_spellings_are_verified_equivalent():
    a = canonicalize("qwen/qwen3.8-max", ALIASES)
    b = canonicalize("provider/qwen-3-8-max", ALIASES)
    assert a == b == "qwen3.8-max"


def test_qwen_3_8_27b_never_collapses_with_qwen_3_8_max():
    assert canonicalize("qwen/qwen3.8-27b", ALIASES) != canonicalize("qwen/qwen3.8-max", ALIASES)


def test_qwen_3_8_27b_never_collapses_with_a_thinking_variant():
    a = canonicalize("qwen/qwen3.8-27b", ALIASES)
    b = canonicalize("qwen/qwen3.8-27b-thinking", ALIASES)
    assert a != b


def test_qwen_3_8_family_never_collapses_with_unrelated_qwen3_8b():
    """qwen3-8b is Qwen 3 at 8B params — a completely different model from
    the Qwen3.8 *version* family (27b/max/flash variants)."""
    assert canonicalize("qwen/qwen3-8b", ALIASES) != canonicalize("qwen/qwen3.8-27b", ALIASES)
    assert canonicalize("qwen/qwen3-8b", ALIASES) != canonicalize("qwen/qwen3.8-max", ALIASES)


# PRE_BENCH_V2_FINAL_CLEANUP #1/#4/#39 — the Ling-3.0-Flash false-merge bug
# and the generic unknown-suffix policy that replaces it.

def test_ling_flash_never_collapses_with_sante_variant():
    a = canonicalize("novita/ling-3.0-flash", ALIASES)
    b = canonicalize("novita/ling-3.0-flash-sante", ALIASES)
    assert a != b
    assert a == "ling-3.0-flash"
    assert b == "ling-3.0-flash-sante"


def test_ling_flash_never_collapses_with_fin_variant():
    a = canonicalize("novita/ling-3.0-flash", ALIASES)
    b = canonicalize("novita/ling-3.0-flash-fin", ALIASES)
    assert a != b
    assert b == "ling-3.0-flash-fin"


def test_ling_flash_sante_never_collapses_with_fin():
    a = canonicalize("novita/ling-3.0-flash-sante", ALIASES)
    b = canonicalize("novita/ling-3.0-flash-fin", ALIASES)
    assert a != b


def test_ling_flash_typographic_variants_still_collapse():
    # Pure formatting differences (dashes/underscores/case) on the SAME
    # checkpoint must still converge — the guard blocks semantic suffixes,
    # not formatting.
    a = canonicalize("Ling_3.0_Flash", ALIASES)
    b = canonicalize("Ling-3.0-Flash", ALIASES)
    assert a == b == "ling-3.0-flash"


def test_generic_unknown_suffix_blocks_alias_even_without_a_blacklist_entry():
    """Any unrecognized semantic suffix — not just the ones we've already
    special-cased — must block a broad alias rule. Uses the real glm-5.2
    rule as a stand-in generic base+unknown-suffix case."""
    a = canonicalize("z-ai/glm-5.2", ALIASES)
    b = canonicalize("z-ai/glm-5.2-legal", ALIASES)
    c = canonicalize("z-ai/glm-5.2-medical", ALIASES)
    assert a != b
    assert a != c
    assert b != c


def test_explicit_verified_alias_can_still_permit_equivalence():
    # qwen3.8-27b / qwen-3-8-27b is an explicit, verified allowlisted rule
    # (different SEPARATORS, same digits) — this must keep matching even
    # under the stricter allowlist-based guard.
    a = canonicalize("qwen/qwen3.8-27b", ALIASES)
    b = canonicalize("provider/qwen-3-8-27b", ALIASES)
    assert a == b == "qwen3.8-27b"
