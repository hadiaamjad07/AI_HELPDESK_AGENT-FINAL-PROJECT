"""
routes/login.py
----------------
Login, Signup aur Logout ka logic.
"""

import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

login_bp = Blueprint("login", __name__)
DB_NAME = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@login_bp.route("/", methods=["GET"])
def home():
    if "user_id" in session:
        return redirect(url_for("ticket.dashboard"))
    return redirect(url_for("login.login"))


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["role"] = user["role"]
            return redirect(url_for("ticket.dashboard"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")


@login_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        conn = get_db_connection()
        existing = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()

        if existing:
            flash("Username already taken", "danger")
            conn.close()
            return redirect(url_for("login.signup"))

        hashed_pw = generate_password_hash(password)
        conn.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, 'user')",
            (username, hashed_pw),
        )
        conn.commit()
        conn.close()
        flash("Account created! Please login.", "success")
        return redirect(url_for("login.login"))

    return render_template("signup.html")


@login_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login.login"))
