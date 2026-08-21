"""CONTROL: framework-intended config execution -> graded Informational."""
import os

_CONFIG_PATH = os.environ.get("DEMO_CONFIG", "instance/config.py")


def load_config(namespace):
    """Load a Python config file into `namespace`, the way Flask does."""
    with open(_CONFIG_PATH) as handle:
        exec(compile(handle.read(), _CONFIG_PATH, "exec"), namespace)
    return namespace
