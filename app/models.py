"""Invoice domain model and helpers."""
from dataclasses import dataclass


@dataclass
class Invoice:
    """A single customer invoice."""

    number: str
    amount: float


def total_for(invoices):
    """Return the summed amount across `invoices`."""
    return sum(i.amount for i in invoices)


def apply_discount(invoice, pct):
    """Reduce `invoice` by a fractional percentage and return it."""
    invoice.amount = invoice.amount * (1 - pct)
    return invoice
