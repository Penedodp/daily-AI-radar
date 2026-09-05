from scoring import compute_pricing_status, has_known_price, is_free


def test_dedicated_zero_price_is_not_free():
    row = {"input_usd_per_million": 0, "output_usd_per_million": 0, "pricing_status": "dedicated"}
    assert is_free(row) is False


def test_unknown_zero_price_is_not_free():
    row = {"input_usd_per_million": 0, "output_usd_per_million": 0, "pricing_status": "unknown"}
    assert is_free(row) is False


def test_explicit_free_status_is_free():
    row = {"input_usd_per_million": 0, "output_usd_per_million": 0, "pricing_status": "free"}
    assert is_free(row) is True


def test_zero_price_without_free_suffix_is_unknown_not_free():
    row = {"input_usd_per_million": 0, "output_usd_per_million": 0, "model_id": "some/model"}
    assert compute_pricing_status(row) == "unknown"


def test_zero_price_with_openrouter_free_suffix_is_free():
    row = {"input_usd_per_million": 0, "output_usd_per_million": 0, "model_id": "meta-llama/llama-3.1-8b-instruct:free"}
    assert compute_pricing_status(row) == "free"


def test_nonzero_price_is_paid_even_with_free_looking_id():
    row = {"input_usd_per_million": 0.5, "output_usd_per_million": 1.0, "model_id": "some/model:free"}
    assert compute_pricing_status(row) == "paid"


def test_has_known_price_excludes_unknown():
    assert has_known_price({"pricing_status": "unknown"}) is False
    assert has_known_price({"pricing_status": "paid"}) is True
    assert has_known_price({"pricing_status": "free"}) is True
    assert has_known_price({"pricing_status": "dedicated"}) is False
