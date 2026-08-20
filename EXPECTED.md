# Run 1 — the buggy revision

Push these files to a **brand new** GitHub repository (for example
`autoaudit-demo`). A new URL means a new repo id, so Memory starts clean and
nothing from your earlier runs interferes.

Every number below was measured with AutoAudit's own analysers.

> **These are the floor, not the total.** They were measured with the built-in
> rules only. With Semgrep running you will see *more* findings, not fewer.

## Repository page

| Field | Expected |
|---|---|
| Primary language | python |
| Package manager | **npm** |
| Frameworks | Express, React |
| Files scanned | 22 |
| Files indexed | 15 |

`npm` is detected from `package.json` alone — there is deliberately no
`requirements.txt` (Python deps live in `requirements-dev.txt`, which is not a
detection indicator).

## Dashboard

| Tile | Expected |
|---|---|
| High | 5 |
| Medium | 2 |
| Info | 1 |
| Test coverage | ~18 |

## The 8 security findings

| Severity | Location | Rule |
|---|---|---|
| HIGH | `app/routes.py:13` | dangerous-eval |
| HIGH | `app/routes.py:14` | dangerous-eval |
| HIGH | `app/routes.py:15` | dangerous-eval |
| HIGH | `app/routes.py:25` | sql-string-concat |
| HIGH | `config/settings.py:5` | hardcoded-secret |
| MEDIUM | `app/legacy.py:53` | insecure-yaml-load |
| MEDIUM | `frontend/src/PaymentForm.tsx:12` | dangerous-eval |
| INFO | `config/dev.py:10` | dangerous-eval — **correct, this is a control** |

All four security rules fire. Plus, from Quality and Documentation:

- `long-function` in `app/legacy.py`
- `broad-except` in `app/legacy.py`
- `duplicate-code` between `app/handlers_a.py` and `app/handlers_b.py`
- missing docstrings in `app/models.py`
- missing README sections: **Usage**, **Testing**

## Three things to point at during the demo

**1. The same rule, three severities.** `dangerous-eval` appears as HIGH on
`routes.py` (user input reaches it), MEDIUM on the TSX file (source unclear),
and INFO on `config/dev.py` (framework-intended config loading). Severity is
not fixed per rule — it depends on context.

**2. Nine control files that stay silent.** If any of these produces a
finding, a false positive has regressed:

| File | Why it must stay silent |
|---|---|
| `app/db.py` | `session.exec(...)` is a method call, not dynamic code |
| `app/interpreter.py` | `def exec` / `def eval` are declarations |
| `app/docs_example.py` | prose and comments that mention `eval()` |
| `static/js/jquery-3.6.0.min.js` | minified, by filename |
| `static/js/materialize.js` | bundled library, by name |
| `static/js/app.js` | minified **by shape** — ordinary name, contains SQL concatenation |
| `app/assets/vendor/bootstrap.js` | vendored, by directory |
| `tests/test_routes.py` | contains `eval("1 + 1")`, excluded as a test |
| `package-lock.json` | lockfile |

**3. One grouped fix.** On the Fixes page, `routes.py` lines 13, 14 and 15
should produce **one** patch, not three: *"Resolves 3 findings — lines 13, 14,
15."* Three separate patches would conflict with each other.

## Also worth showing

- **PDF export** — `PaymentForm.tsx` evidence contains `<FormField>`, which is
  raw XML to the renderer. The export must succeed, not crash.
- **Explorer** — open `app/db.py` and `app/interpreter.py` and show they are
  clean.
