"""Application settings."""
import os

DEBUG = False
# FIXED: read from the environment, never committed
API_KEY = os.environ["DEMO_API_KEY"]
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://localhost/demo")
