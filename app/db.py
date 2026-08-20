"""Database access. CONTROL: `.exec()` is a method call, not dynamic code."""
from sqlmodel import Session, select


def list_invoices(session: Session, params):
    """Run a query. Uses `session.exec()`, which must not be flagged."""
    statement = select("invoices")
    return session.exec(statement, params).all()
