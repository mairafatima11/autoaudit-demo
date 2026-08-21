"""Shared payload normalisation, extracted from the two handler modules."""
import json
import logging

logger = logging.getLogger(__name__)


def normalise_payload(payload, options):
    """Decode and normalise a JSON payload according to `options`."""
    logger.info("processing payload")
    decoded = json.loads(payload)
    normalised = {}
    for key, value in decoded.items():
        if value is None:
            continue
        if isinstance(value, str):
            normalised[key] = value.strip().lower()
        elif isinstance(value, (int, float)):
            normalised[key] = round(float(value), 4)
        else:
            normalised[key] = value
    if options.get("drop_empty"):
        normalised = {k: v for k, v in normalised.items() if v != ""}
    if options.get("sort"):
        normalised = dict(sorted(normalised.items()))
    logger.info("processed %d keys", len(normalised))
    return normalised
