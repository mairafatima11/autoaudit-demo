"""CONTROL: findings inside tests are excluded by default."""
from app.routes import calculate_totals


def test_eval_helper():
    assert eval("1 + 1") == 2


def test_calculate_totals_exists():
    assert callable(calculate_totals)
