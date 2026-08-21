# AutoAudit Demo Service

A small billing service used to demonstrate AutoAudit AI end to end.
This is the **corrected** revision: the planted issues are resolved while
every control case is left exactly as it was.

## Installation

```bash
pip install -r requirements-dev.txt
npm install
```

## Usage

```bash
flask --app app run
```

Post a calculation to `/calculate` with `pre_tax`, `after_tax` and `roth`
form fields, or look a customer up with `GET /user?id=<id>`.

## Testing

```bash
pytest
```

The suite covers the routes, the reporting helpers, the payload normaliser
and the invoice model.

## License

MIT
