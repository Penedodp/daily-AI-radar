import json
from pathlib import Path

from scoring import compute_pricing_status, override_key
from main import _pricing_override_match_stats

ALIASES_PATH = Path(__file__).resolve().parents[1] / "config" / "provider_pricing_overrides.json"


def _overrides(*entries):
    return {override_key(e["provider"], e["model_id"]): e for e in entries}


def test_novita_fin_override_yields_free():
    overrides = _overrides({
        "provider": "Novita AI", "model_id": "inclusionai/ling-3.0-flash-fin",
        "pricing_status": "free", "verified_at": "2026-09-08", "source_url": "https://novita.ai/pricing",
    })
    row = {"provider": "Novita AI", "model_id": "inclusionai/ling-3.0-flash-fin",
           "input_usd_per_million": 0, "output_usd_per_million": 0}
    assert compute_pricing_status(row, overrides) == "free"


def test_novita_sante_override_yields_promotional_free():
    overrides = _overrides({
        "provider": "Novita AI", "model_id": "inclusionai/ling-3.0-flash-sante",
        "pricing_status": "promotional_free", "verified_at": "2026-09-08", "source_url": "https://novita.ai/pricing",
    })
    row = {"provider": "Novita AI", "model_id": "inclusionai/ling-3.0-flash-sante",
           "input_usd_per_million": 0, "output_usd_per_million": 0}
    assert compute_pricing_status(row, overrides) == "promotional_free"


def test_novita_unknown_model_without_override_stays_unknown():
    overrides = _overrides({
        "provider": "Novita AI", "model_id": "inclusionai/ling-3.0-flash-fin",
        "pricing_status": "free", "verified_at": "2026-09-08", "source_url": "https://novita.ai/pricing",
    })
    row = {"provider": "Novita AI", "model_id": "some-other-novita-model",
           "input_usd_per_million": 0, "output_usd_per_million": 0}
    assert compute_pricing_status(row, overrides) == "unknown"


def test_paid_signal_always_wins_over_an_override():
    overrides = _overrides({
        "provider": "Novita AI", "model_id": "inclusionai/ling-3.0-flash-fin",
        "pricing_status": "free", "verified_at": "2026-09-08", "source_url": "https://novita.ai/pricing",
    })
    row = {"provider": "Novita AI", "model_id": "inclusionai/ling-3.0-flash-fin",
           "input_usd_per_million": 0.5, "output_usd_per_million": 1.5}
    assert compute_pricing_status(row, overrides) == "paid"


def test_shipped_override_config_uses_the_real_namespaced_novita_ids():
    """FINAL_PRE_BENCH_V2_UX_ARCHITECTURE #3: the collector returns namespaced
    ids (e.g. 'inclusionai/ling-3.0-flash-fin'), not the bare slug — an
    override with the bare slug silently never matches anything."""
    cfg = json.loads(ALIASES_PATH.read_text(encoding="utf-8"))
    ids = {e["model_id"] for e in cfg["entries"]}
    assert "inclusionai/ling-3.0-flash-fin" in ids
    assert "inclusionai/ling-3.0-flash-sante" in ids
    assert "ling-3.0-flash-fin" not in ids
    assert "ling-3.0-flash-sante" not in ids


def _row(provider, model_id, override=None):
    return {"provider": provider, "model_id": model_id, "pricing_override": override}


def test_override_match_stats_detect_configured_but_unused():
    overrides = _overrides({
        "provider": "Novita AI", "model_id": "inclusionai/ling-3.0-flash-fin",
        "pricing_status": "free", "verified_at": "2026-09-08", "source_url": "https://novita.ai/pricing",
    }, {
        "provider": "Novita AI", "model_id": "inclusionai/ling-3.0-flash-sante",
        "pricing_status": "promotional_free", "verified_at": "2026-09-08", "source_url": "https://novita.ai/pricing",
    })
    # only ONE of the two configured overrides actually matched a live row
    models = [_row("Novita AI", "inclusionai/ling-3.0-flash-fin",
                    override=overrides[override_key("Novita AI", "inclusionai/ling-3.0-flash-fin")])]
    stats = _pricing_override_match_stats(models, overrides)
    assert stats["pricing_overrides_configured"] == 2
    assert stats["pricing_overrides_used"] == 1
    assert stats["pricing_overrides_unused"] == 1


def test_override_match_stats_all_used():
    overrides = _overrides({
        "provider": "Novita AI", "model_id": "inclusionai/ling-3.0-flash-fin",
        "pricing_status": "free", "verified_at": "2026-09-08", "source_url": "https://novita.ai/pricing",
    })
    models = [_row("Novita AI", "inclusionai/ling-3.0-flash-fin",
                    override=overrides[override_key("Novita AI", "inclusionai/ling-3.0-flash-fin")])]
    stats = _pricing_override_match_stats(models, overrides)
    assert stats["pricing_overrides_configured"] == 1
    assert stats["pricing_overrides_used"] == 1
    assert stats["pricing_overrides_unused"] == 0
