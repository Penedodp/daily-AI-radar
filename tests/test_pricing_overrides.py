from scoring import compute_pricing_status, override_key


def _overrides(*entries):
    return {override_key(e["provider"], e["model_id"]): e for e in entries}


def test_novita_fin_override_yields_free():
    overrides = _overrides({
        "provider": "Novita AI", "model_id": "ling-3.0-flash-fin",
        "pricing_status": "free", "verified_at": "2026-09-07", "source_url": "https://novita.ai/pricing",
    })
    row = {"provider": "Novita AI", "model_id": "ling-3.0-flash-fin",
           "input_usd_per_million": 0, "output_usd_per_million": 0}
    assert compute_pricing_status(row, overrides) == "free"


def test_novita_sante_override_yields_promotional_free():
    overrides = _overrides({
        "provider": "Novita AI", "model_id": "ling-3.0-flash-sante",
        "pricing_status": "promotional_free", "verified_at": "2026-09-07", "source_url": "https://novita.ai/pricing",
    })
    row = {"provider": "Novita AI", "model_id": "ling-3.0-flash-sante",
           "input_usd_per_million": 0, "output_usd_per_million": 0}
    assert compute_pricing_status(row, overrides) == "promotional_free"


def test_novita_unknown_model_without_override_stays_unknown():
    overrides = _overrides({
        "provider": "Novita AI", "model_id": "ling-3.0-flash-fin",
        "pricing_status": "free", "verified_at": "2026-09-07", "source_url": "https://novita.ai/pricing",
    })
    row = {"provider": "Novita AI", "model_id": "some-other-novita-model",
           "input_usd_per_million": 0, "output_usd_per_million": 0}
    assert compute_pricing_status(row, overrides) == "unknown"


def test_paid_signal_always_wins_over_an_override():
    overrides = _overrides({
        "provider": "Novita AI", "model_id": "ling-3.0-flash-fin",
        "pricing_status": "free", "verified_at": "2026-09-07", "source_url": "https://novita.ai/pricing",
    })
    row = {"provider": "Novita AI", "model_id": "ling-3.0-flash-fin",
           "input_usd_per_million": 0.5, "output_usd_per_million": 1.5}
    assert compute_pricing_status(row, overrides) == "paid"
