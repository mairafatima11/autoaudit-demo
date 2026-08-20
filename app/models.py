from dataclasses import dataclass


@dataclass
class Invoice:
    number: str
    amount: float


def total_for(invoices):
    return sum(i.amount for i in invoices)


def apply_discount(invoice, pct):
    invoice.amount = invoice.amount * (1 - pct)
    return invoice
