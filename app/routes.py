"""HTTP route handlers for the demo billing service."""
import sqlite3
import subprocess

from flask import Blueprint, request

bp = Blueprint("routes", __name__)


@bp.route("/calculate", methods=["POST"])
def calculate_totals():
    # ISSUE: user input reaches eval() -> dangerous-eval, HIGH
    pre_tax = eval(request.form["pre_tax"])
    after_tax = eval(request.form["after_tax"])
    roth = eval(request.form["roth"])
    return {"total": pre_tax + after_tax + roth}


@bp.route("/user")
def lookup_user():
    conn = sqlite3.connect("app.db")
    user_id = request.args.get("id")
    # ISSUE: string-built SQL -> sql-string-concat, HIGH
    cursor = conn.cursor()
    cursor.execute("SELECT id, email FROM users WHERE id = " + user_id)
    return {"rows": cursor.fetchall()}


@bp.route("/ping")
def ping_host():
    host = request.args.get("host", "localhost")
    # ISSUE: shell command built from user input -> command injection
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return {"output": output.decode()}
