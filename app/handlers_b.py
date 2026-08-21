"""Request handlers, variant b."""
from app.normalisation import normalise_payload


def process_payload(payload, options):
    """Normalise an incoming payload."""
    return normalise_payload(payload, options)
