"""CONTROL: methods *named* exec/eval are declarations, not calls."""


class Sandbox:
    def exec(self, params):
        """Declaring a method called exec must not be flagged."""
        return {"params": params, "ok": True}

    def eval(self, expression, params):
        """Same for eval."""
        return len(expression) + len(params)
