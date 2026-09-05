"""Conservative model-identity canonicalization.

Philosophy (see DAILY_AI_RADAR_CLAUDE_PLAN.md, Fase 1): canonicalizing
formatting differences (dashes/underscores/case/provider prefix) is fine.
Collapsing genuinely different checkpoints under one canonical id is not.

`model_aliases.json` still ships broad "family" regexes (e.g. a single rule
for all `deepseek*r1*` ids) because that is what's needed to catch typo/case
variants across providers. To stop those broad rules from silently merging
different checkpoints (DeepSeek-R1 vs DeepSeek-R1-Distill-Qwen-32B), every
rule match is passed through `_has_unaccounted_variant`: if the raw model id
carries a size (`32b`, `1.5b`), a date/checkpoint (`0528`, `20240806`), or a
known variant word (`distill`, `instruct`, `preview`, ...) that isn't part of
the rule's own canonical string, the match is rejected and we fall back to
the safe, information-preserving slug normalization instead.
"""
import re

_TOKEN = re.compile(r"[a-z]+|\d+(?:\.\d+)?")
_VARIANT_TOKENS = {
    "distill", "base", "instruct", "chat", "thinking", "reasoning",
    "preview", "turbo", "flash", "mini", "nano", "highspeed", "vl",
    "vision", "lite", "exp", "experimental", "fast", "pro", "max",
    "ultra", "super", "b", "m", "k",  # trailing size-unit letters (32b, 8m...)
}


def _tokens(s):
    return set(_TOKEN.findall((s or "").lower()))


def _has_unaccounted_variant(raw_slug, canonical):
    """True if raw_slug carries a token (size, date/checkpoint number, or
    known variant word) that `canonical` doesn't already represent — i.e.
    collapsing to `canonical` would lose information that could distinguish
    a different checkpoint. Any leftover purely-numeric token is treated as
    suspicious (it could be a size like 32/70, a date like 0528/20240806, or
    a version segment) unless the canonical string already accounts for it."""
    leftover = _tokens(raw_slug) - _tokens(canonical)
    for tok in leftover:
        if tok.isdigit() or tok in _VARIANT_TOKENS:
            return True
    return False


def canonicalize_with_confidence(model_id, aliases):
    """(canonical_id, identity_confidence). `verified_alias` means an explicit
    rule in model_aliases.json matched and passed the variant guard —
    cross-provider "same model" comparisons should only trust this level (or
    an identical raw id, which also lands here since the fallback slug is
    lossless). `normalized_id` is the safe fallback: formatting-only
    normalization of a single id, never merged with anything else."""
    value = (model_id or "").strip()
    slug_for_guard = value.split("/", 1)[-1].lower()

    for rule in aliases.get("rules", []):
        if re.search(rule["pattern"], value, flags=re.IGNORECASE):
            canonical = rule["canonical"]
            if _has_unaccounted_variant(slug_for_guard, canonical):
                continue
            return canonical, "verified_alias"

    # Fallback: remove provider prefix and common free/latest route decorations.
    # This never merges distinct ids — it only normalizes formatting — so it's
    # always safe to use when no verified alias rule applies cleanly.
    slug = slug_for_guard
    slug = re.sub(r":free$", "", slug)
    slug = re.sub(r"^~", "", slug)
    slug = re.sub(r"[-_/ ]latest$", "", slug)
    return slug, "normalized_id"


def canonicalize(model_id, aliases):
    return canonicalize_with_confidence(model_id, aliases)[0]
