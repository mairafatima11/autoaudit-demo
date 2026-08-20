"""Legacy reporting module kept for the v1 API."""
import yaml


def build_monthly_report(rows, start, end, currency, include_tax, include_fees,
                         group_by, sort_key, limit):
    """ISSUE: far over the long-function threshold -> long-function."""
    output = []
    totals = {}
    for row in rows:
        if row.get("date") is None:
            continue
        if row["date"] < start:
            continue
        if row["date"] > end:
            continue
        key = row.get(group_by, "unknown")
        totals.setdefault(key, 0)
        amount = row.get("amount", 0)
        if include_tax:
            amount = amount * 1.2
        if include_fees:
            amount = amount + 2.5
        totals[key] = totals[key] + amount
        output.append({"key": key, "amount": amount, "currency": currency})
    for key in list(totals):
        if totals[key] == 0:
            del totals[key]
    ordered = sorted(output, key=lambda item: item.get(sort_key, 0))
    if limit:
        ordered = ordered[:limit]
    summary = {"count": len(ordered), "totals": totals}
    footer = {"generated": True, "currency": currency}
    result = {"rows": ordered, "summary": summary, "footer": footer}
    for entry in ordered:
        entry["formatted"] = "%s %.2f" % (currency, entry["amount"])
    for entry in ordered:
        entry["group"] = entry["key"].upper()
    for entry in ordered:
        entry["index"] = ordered.index(entry)
    checks = []
    for entry in ordered:
        checks.append(entry["amount"] >= 0)
    result["valid"] = all(checks)
    result["checked"] = len(checks)
    return result


def load_report_config(path):
    try:
        with open(path) as handle:
            # ISSUE: unsafe YAML loading -> insecure-yaml-load
            return yaml.load(handle.read())
    except Exception:
        # ISSUE: swallows every error -> broad-except
        return None
