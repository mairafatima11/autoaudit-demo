# Run 2 — the corrected revision

Push this over the **same repository**, same file paths. That is what makes the
comparison meaningful: findings are matched by fingerprint, and the path is
part of the fingerprint.

## What changed

| File | Change |
|---|---|
| `app/routes.py` | `eval` → `float`; concatenated SQL → parameterised; `shell=True` → argument list |
| `config/settings.py` | committed key → `os.environ` |
| `app/legacy.py` | long function split; `yaml.load` → `yaml.safe_load`; `except Exception` narrowed |
| `app/handlers_a.py`, `app/handlers_b.py` | duplication extracted to `app/normalisation.py` |
| `app/models.py` | docstrings added |
| `README.md` | Usage and Testing sections added |
| `tests/` | 3 test files added, 12 cases total |

Unchanged on purpose: every control file. A finding appearing in one now is a
regression.

## Dashboard

| Tile | Run 1 | Run 2 |
|---|---|---|
| High | 5 | **0** |
| Medium | 2 | **0** |
| Info | 1 | 1 |
| Files scanned | 22 | 26 |
| Test coverage | ~18 | **~59** |

Health must rise sharply. Security should reach **100**.

## Findings — one remains, and it is correct

| Severity | Location | Rule | Why it stays |
|---|---|---|---|
| INFO | `config/dev.py:10` | dangerous-eval | Framework-intended config loading. Correctly graded Informational, not a bug. |

That single remaining line is a good thing to point at:

> "It didn't go to zero, and it shouldn't. This one is Flask-style config
> loading — the tool grades it Informational rather than pretending it's a
> vulnerability or hiding it entirely."

## Memory — the part that matters

| Panel | Expected |
|---|---|
| Health Score Trend | two points, second clearly higher |
| Severity Trend | high 5 → 0 |
| Fixed since last run | **9+** |
| No longer reported (out of scope) | **0** |
| Recurring | `config/dev.py:10` |
| Methodology warning | none — both runs same regime |

**The number to watch is "out of scope = 0".** Nothing left the analysis scope
between these revisions, so anything other than zero would mean scope changes
are being miscounted as fixes.

## Optional third run

Re-run this revision without changing anything. It must report **0 fixed, 0
new, everything recurring**, and an unchanged health score.

> "Same code, second run — it doesn't invent progress."
