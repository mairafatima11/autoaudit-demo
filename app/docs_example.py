"""CONTROL: prose that mentions eval() is documentation, not code.

Instead of building strings you could use `eval()` to parse them, but
don't - it executes whatever it is given. The same applies to `exec()`.
"""


def parse_number(raw):
    """Parse a numeric string safely."""
    # Do not use eval() here; int() is enough.
    return int(raw)
