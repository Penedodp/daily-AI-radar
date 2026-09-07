import pytest

from main import apply_price_change, _combined_tariff_change_pct


def test_task_profile_change_alone_is_not_a_price_movement():
    """Only weighted_cost moved (e.g. config.json's task_profiles changed) —
    the real tariff is untouched, so the tariff change is exactly 0%, never
    inferred from the weighted_cost delta (which did move, 0.05 -> 0.08)."""
    row = {"input_usd_per_million": 1.0, "output_usd_per_million": 2.0, "weighted_cost": 0.05}
    old = {"input_usd_per_million": 1.0, "output_usd_per_million": 2.0, "weighted_cost": 0.08}
    apply_price_change(row, old)
    assert row["change_pct"] == 0.0
    assert row["input_change_pct"] == 0.0
    assert row["output_change_pct"] == 0.0
    # but the estimated-cost move is still tracked, separately, and is NOT zero
    assert row["estimated_cost_change_pct"] == pytest.approx(-37.5)


def test_real_tariff_change_is_detected():
    row = {"input_usd_per_million": 0.8, "output_usd_per_million": 2.0, "weighted_cost": 0.04}
    old = {"input_usd_per_million": 1.0, "output_usd_per_million": 2.0, "weighted_cost": 0.05}
    apply_price_change(row, old)
    assert row["change_pct"] == pytest.approx(-20.0)
    assert row["input_change_pct"] == pytest.approx(-20.0)
    assert row["output_change_pct"] == 0.0


def test_no_previous_route_means_no_change_at_all():
    row = {"input_usd_per_million": 1.0, "output_usd_per_million": 2.0, "weighted_cost": 0.05}
    apply_price_change(row, None)
    assert row["change_pct"] is None
    assert row["estimated_cost_change_pct"] is None


def test_combined_change_picks_larger_magnitude_move():
    row = {"input_change_pct": -5.0, "output_change_pct": 30.0}
    assert _combined_tariff_change_pct(row) == 30.0
    row2 = {"input_change_pct": -50.0, "output_change_pct": 5.0}
    assert _combined_tariff_change_pct(row2) == -50.0


def test_combined_change_is_none_when_neither_moved():
    assert _combined_tariff_change_pct({"input_change_pct": None, "output_change_pct": None}) is None
