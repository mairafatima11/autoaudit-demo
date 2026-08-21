"""HTTP route handlers for the demo billing service."""
import sqlite3
import subprocess

from flask import Blueprint, request

bp = Blueprint("routes", __name__)


@bp.route("/calculate", methods=["POST"])
def calculate_totals():
    """Total a contribution split. FIXED: parse numbers, never execute input."""
    pre_tax = float(request.form["pre_tax"])
    after_tax = float(request.form["after_tax"])
    roth = float(request.form["roth"])
    return {"total": pre_tax + after_tax + roth}


@bp.route("/user")
def lookup_user():
    """Look a user up by id. FIXED: parameterised query."""
    conn = sqlite3.connect("app.db")
    user_id = request.args.get("id")
    cursor = conn.cursor()
    cursor.execute("SELECT id, email FROM users WHERE id = ?", (user_id,))
    return {"rows": cursor.fetchall()}


@bp.route("/ping")
def ping_host():
    """Ping a host. FIXED: argument list, no shell."""
    host = request.args.get("host", "localhost")
    output = subprocess.check_output(["ping", "-c", "1", host], shell=False)
    return {"output": output.decode()}
