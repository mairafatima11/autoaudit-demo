"""Tests for the invoice model."""
from app.models import Invoice, apply_discount, total_for


def test_total_for_sums_amounts():
    assert total_for([Invoice("1", 10.0), Invoice("2", 5.0)]) == 15.0


def test_apply_discount_reduces_amount():
    assert apply_discount(Invoice("1", 100.0), 0.1).amount == 90.0


def test_total_for_empty():
    assert total_for([]) == 0
