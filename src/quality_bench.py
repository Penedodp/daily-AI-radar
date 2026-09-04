"""Automated coding-quality scoring, sourced from public benchmarks.

Two independent, no-API-key sources, combined with a clear precedence:

  1. Aider Polyglot Leaderboard (Aider-AI/aider on GitHub) — a fixed
     pass/fail correctness test across languages. Narrower coverage (a
     maintainer has to run and submit each new model) but objective.
     Preferred whenever it has a match.
  2. LMArena WebDev Arena (lmarena-ai/leaderboard-dataset on Hugging Face)
     — crowd-voted Elo rating for web-app generation. Broader and much
     faster to pick up brand-new releases (including non-Western labs like
     Zhipu/Alibaba/Moonshot) since it doesn't need anyone to run a fixed
     suite. Used as a fallback when Aider has no match.

Both are matched against provider model IDs the same strict way: version
numbers (3 vs 3.5, k2 vs k2.5, v3 vs v3.1...) must match exactly, and the
remaining text must be near-identical. A match that doesn't clear that bar
is discarded rather than guessed — an unscored model is preferable to a
wrongly-scored one (e.g. silently conflating claude-3-haiku with
claude-3.5-haiku).
"""
import difflib
import json
import re

import requests
import yaml

AIDER_URL = (
    "https://raw.githubusercontent.com/Aider-AI/aider/main/"
    "aider/website/_data/polyglot_leaderboard.yml"
)
ARENA_ROWS_URL = "https://datasets-server.huggingface.co/rows"
ARENA_DATASET = "lmarena-ai/leaderboard-dataset"
ARENA_CONFIG = "webdev"
ARENA_SPLIT = "latest"
ARENA_PAGE_SIZE = 100
ARENA_MAX_ROWS = 1000
# Elo calibration for WebDev Arena: ~950 is a weak/legacy model, ~1750 is the
# current frontier ceiling (observed on the live leaderboard). Reviewed/moved
# only if the whole field's ratings drift outside this band over time.
ARENA_ELO_FLOOR = 950.0
ARENA_ELO_CEILING = 1750.0

TEXT_MATCH_THRESHOLD = 0.90
AIDER_MIN_TEST_CASES = 100

SOURCE_LABELS = {
    "aider_polyglot": "Aider Polyglot Leaderboard",
    "lmarena_webdev": "LMArena WebDev Arena",
}

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


def _best_entry_per_model(scored_entries):
    """scored_entries: iterable of {"model": str, "score": 0-10 float}.
    Keeps, per (numeric, text) fingerprint, the entry with the highest score."""
    best = {}
    for e in scored_entries:
        name, score = e.get("model"), e.get("score")
        if not name or score is None:
            continue
        numeric, text_key = _fingerprint(name)
        if not text_key:
            continue
        key = (numeric, text_key)
        current = best.get(key)
        if current is None or score > current["score"]:
            best[key] = {"model": name, "score": float(score), "numeric": numeric, "text_key": text_key}
    return list(best.values())


def _fetch_with_cache(cache_path, fetch_fn):
    """fetch_fn() -> list of {"model","score"} dicts, or raises."""
    try:
        scored = fetch_fn()
        entries = _best_entry_per_model(scored)
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


def fetch_aider_leaderboard(cache_path, timeout=30):
    def _fetch():
        r = requests.get(AIDER_URL, timeout=timeout)
        r.raise_for_status()
        raw_entries = yaml.safe_load(r.text) or []
        out = []
        for e in raw_entries:
            rate, cases = e.get("pass_rate_2"), e.get("test_cases")
            if e.get("model") and rate is not None and cases and cases >= AIDER_MIN_TEST_CASES:
                out.append({"model": e["model"], "score": max(0.0, min(10.0, rate / 10.0))})
        return out
    return _fetch_with_cache(cache_path, _fetch)


def fetch_lmarena_webdev(cache_path, timeout=30):
    def _fetch():
        out = []
        offset = 0
        while offset < ARENA_MAX_ROWS:
            r = requests.get(
                ARENA_ROWS_URL,
                params={
                    "dataset": ARENA_DATASET, "config": ARENA_CONFIG, "split": ARENA_SPLIT,
                    "offset": offset, "length": ARENA_PAGE_SIZE,
                },
                timeout=timeout,
            )
            r.raise_for_status()
            payload = r.json()
            rows = payload.get("rows", [])
            if not rows:
                break
            for entry in rows:
                row = entry.get("row", {})
                if row.get("category") != "overall":
                    continue
                name, rating = row.get("model_name"), row.get("rating")
                if name and rating is not None:
                    score = (rating - ARENA_ELO_FLOOR) / (ARENA_ELO_CEILING - ARENA_ELO_FLOOR) * 10.0
                    out.append({"model": name, "score": max(0.0, min(10.0, score))})
            offset += ARENA_PAGE_SIZE
            if offset >= payload.get("num_rows_total", 0):
                break
        return out
    return _fetch_with_cache(cache_path, _fetch)


def _candidate_strings(row):
    model_id = row.get("model_id") or ""
    slug = model_id.split("/", 1)[-1]
    canonical_slug = (row.get("metadata") or {}).get("canonical_slug") or ""
    name = row.get("name") or ""
    return {model_id, slug, canonical_slug, name}


def match_models(bench_entries, rows, source):
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
        results[key] = {
            "label": entry["model"],
            "source": source,
            "source_label": SOURCE_LABELS.get(source, source),
            "match_ratio": round(ratio, 3),
            "scores": {"coding": round(entry["score"], 1)},
        }
    return results
