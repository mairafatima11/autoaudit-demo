"""Tests for the reporting helpers."""
from app.legacy import _amount_for, _in_range, build_monthly_report


def test_in_range_excludes_missing_dates():
    assert _in_range({}, 1, 10) is False


def test_amount_applies_tax_and_fees():
    assert _amount_for({"amount": 10}, True, True) == 14.5


def test_build_monthly_report_groups_rows():
    rows = [{"date": 5, "amount": 10, "team": "a"}]
    out = build_monthly_report(rows, 1, 10, "GBP", False, False, "team", "amount", None)
    assert out["summary"]["count"] == 1
