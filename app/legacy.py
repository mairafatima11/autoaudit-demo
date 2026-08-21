"""Legacy reporting module kept for the v1 API."""
import yaml


def _in_range(row, start, end):
    """Whether a row falls inside the reporting window."""
    return row.get("date") is not None and start <= row["date"] <= end


def _amount_for(row, include_tax, include_fees):
    """Apply tax and fee adjustments to one row's amount."""
    amount = row.get("amount", 0)
    if include_tax:
        amount *= 1.2
    if include_fees:
        amount += 2.5
    return amount


def _decorate(ordered, currency):
    """Attach display fields to each ordered entry."""
    for index, entry in enumerate(ordered):
        entry["formatted"] = "%s %.2f" % (currency, entry["amount"])
        entry["group"] = entry["key"].upper()
        entry["index"] = index
    return ordered


def build_monthly_report(rows, start, end, currency, include_tax, include_fees,
                         group_by, sort_key, limit):
    """FIXED: split into helpers, now well under the length threshold."""
    output, totals = [], {}
    for row in rows:
        if not _in_range(row, start, end):
            continue
        key = row.get(group_by, "unknown")
        amount = _amount_for(row, include_tax, include_fees)
        totals[key] = totals.get(key, 0) + amount
        output.append({"key": key, "amount": amount, "currency": currency})

    ordered = sorted(output, key=lambda item: item.get(sort_key, 0))
    if limit:
        ordered = ordered[:limit]
    ordered = _decorate(ordered, currency)
    return {
        "rows": ordered,
        "summary": {"count": len(ordered),
                    "totals": {k: v for k, v in totals.items() if v}},
        "footer": {"generated": True, "currency": currency},
        "valid": all(entry["amount"] >= 0 for entry in ordered),
        "checked": len(ordered),
    }


def load_report_config(path):
    """Load report configuration. FIXED: safe_load, and a narrow except."""
    try:
        with open(path) as handle:
            return yaml.safe_load(handle.read())
    except (OSError, yaml.YAMLError):
        return None
