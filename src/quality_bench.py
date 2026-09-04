"""Automated coding-quality scoring, sourced from a public benchmark.

Source: Aider Polyglot Leaderboard (Aider-AI/aider on GitHub), a community-run,
actively-maintained coding benchmark (pass-rate on multi-language exercises).
No API key required, updated within days of new model releases.

This module fetches the leaderboard, converts each model's best pass_rate_2
into a 0-10 "coding" quality score, and matches benchmark model names against
provider model IDs. Matching is deliberately strict: version numbers (3 vs
3.5, k2 vs k2.5, v3 vs v3.1...) must match exactly, and the remaining text
must be near-identical. A match that doesn't clear that bar is discarded
rather than guessed — an unscored model is preferable to a wrongly-scored one
(e.g. silently conflating claude-3-haiku with claude-3.5-haiku).
"""
import difflib
import json
import re

import requests
import yaml

LEADERBOARD_URL = (
    "https://raw.githubusercontent.com/Aider-AI/aider/main/"
    "aider/website/_data/polyglot_leaderboard.yml"
)
TEXT_MATCH_THRESHOLD = 0.90
MIN_TEST_CASES = 100

_STRIP_WORDS = re.compile(r"\b(preview|latest|exp|experimental|instruct|chat|it|base|thinking)\b")
_DATE_ISO = re.compile(r"\d{4}-\d{2}-\d{2}")
_DATE_GLUED = re.compile(r"(?<![a-z0-9])\d{8}(?![a-z0-9])")
_TOKEN = re.compile(r"[a-z]+|\d+")


def _fingerprint(raw):
    """(numeric_tokens, text_key) — version numbers kept separate from text
    so "claude-3-haiku" and "claude-3.5-haiku" can never fuzzy-match."""
    s = (raw or "").lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = _DATE_ISO.sub(" ", s)
    s = _DATE_GLUED.sub(" ", s)
    s = _STRIP_WORDS.sub(" ", s)
    tokens = _TOKEN.findall(s)
    numeric = tuple(t for t in tokens if t.isdigit())
    text_key = "".join(t for t in tokens if not t.isdigit())
    return numeric, text_key


def _best_entry_per_model(raw_entries):
    best = {}
    for e in raw_entries or []:
        name = e.get("model")
        rate = e.get("pass_rate_2")
        cases = e.get("test_cases")
        if not name or rate is None or not cases or cases < MIN_TEST_CASES:
            continue
        numeric, text_key = _fingerprint(name)
        if not text_key:
            continue
        key = (numeric, text_key)
        current = best.get(key)
        if current is None or float(rate) > current["pass_rate_2"]:
            best[key] = {
                "model": name,
                "pass_rate_2": float(rate),
                "numeric": numeric,
                "text_key": text_key,
            }
    return list(best.values())


def fetch_leaderboard(cache_path, timeout=30):
    """Returns (entries, status). Falls back to the last cached copy on failure."""
    try:
        r = requests.get(LEADERBOARD_URL, timeout=timeout)
        r.raise_for_status()
        raw_entries = yaml.safe_load(r.text) or []
        entries = _best_entry_per_model(raw_entries)
        if not entries:
            raise ValueError("empty leaderboard after parsing")
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
        return entries, "ok"
    except Exception:
        if cache_path.exists():
            try:
                cached = json.loads(cache_path.read_text(encoding="utf-8"))
                for e in cached:
                    e["numeric"] = tuple(e.get("numeric") or ())
                return cached, "cached_stale"
            except Exception:
                pass
        return [], "error"


def _candidate_strings(row):
    model_id = row.get("model_id") or ""
    slug = model_id.split("/", 1)[-1]
    canonical_slug = (row.get("metadata") or {}).get("canonical_slug") or ""
    name = row.get("name") or ""
    return {model_id, slug, canonical_slug, name}


def match_models(bench_entries, rows):
    """Returns {route_key: quality_dict} for rows whose model matches a
    benchmark entry: exact version numbers + near-identical remaining text."""
    row_best = {}
    for row in rows:
        fingerprints = {
            _fingerprint(s) for s in _candidate_strings(row) if s and _fingerprint(s)[1]
        }
        if not fingerprints:
            continue

        best_ratio, best_entry = 0.0, None
        for entry in bench_entries:
            for numeric, text_key in fingerprints:
                if numeric != tuple(entry["numeric"]):
                    continue
                ratio = 1.0 if text_key == entry["text_key"] else difflib.SequenceMatcher(
                    None, text_key, entry["text_key"]
                ).ratio()
                if ratio > best_ratio:
                    best_ratio, best_entry = ratio, entry

        if best_entry and best_ratio >= TEXT_MATCH_THRESHOLD:
            key = f"{row.get('provider','')}::{row.get('model_id','')}"
            row_best[key] = (best_ratio, best_entry)

    results = {}
    for key, (ratio, entry) in row_best.items():
        score = round(min(10.0, max(0.0, entry["pass_rate_2"] / 10.0)), 1)
        results[key] = {
            "label": entry["model"],
            "source": "aider_polyglot",
            "match_ratio": round(ratio, 3),
            "scores": {"coding": score},
        }
    return results
