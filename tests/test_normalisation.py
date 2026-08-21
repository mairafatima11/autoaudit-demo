"""Tests for the shared payload normaliser."""
from app.normalisation import normalise_payload


def test_strings_are_trimmed_and_lowercased():
    assert normalise_payload('{"a": " X "}', {}) == {"a": "x"}


def test_none_values_are_dropped():
    assert normalise_payload('{"a": null}', {}) == {}


def test_sort_option_orders_keys():
    assert list(normalise_payload('{"b": 1, "a": 2}', {"sort": True})) == ["a", "b"]
