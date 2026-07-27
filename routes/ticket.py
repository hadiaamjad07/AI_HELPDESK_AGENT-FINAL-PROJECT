"""
routes/ticket.py
-----------------
Ticket create karna, dekhna, aur dashboard stats dikhana.
"""

import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ai.ollama import analyze_ticket

ticket_bp = Blueprint("ticket", __name__)
DB_NAME = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def login_required():
    return "user_id" in session


@ticket_bp.route("/dashboard")
def dashboard():
    if not login_required():
        return redirect(url_for("login.login"))

    conn = get_db_connection()

    # Agar admin hai to sab tickets dikhao, warna sirf apne
    if session.get("role") == "admin":
        tickets = conn.execute(
            "SELECT * FROM tickets ORDER BY created_at DESC"
        ).fetchall()
    else:
        tickets = conn.execute(
            "SELECT * FROM tickets WHERE user_id = ? ORDER BY created_at DESC",
            (session["user_id"],),
        ).fetchall()

    total = len(tickets)
    pending = len([t for t in tickets if t["status"] == "Pending"])
    closed = len([t for t in tickets if t["status"] == "Closed"])
    high_priority = len([t for t in tickets if t["priority"] == "High"])

    conn.close()

    stats = {
        "total": total,
        "pending": pending,
        "closed": closed,
        "high_priority": high_priority,
    }

    return render_template("dashboard.html", tickets=tickets, stats=stats)


@ticket_bp.route("/ticket/create", methods=["GET", "POST"])
def create_ticket():
    if not login_required():
        return redirect(url_for("login.login"))

    if request.method == "POST":
        title = request.form["title"].strip()
        description = request.form["description"].strip()

        # AI se category/priority/summary nikalwao
        ai_result = analyze_ticket(title, description)

        conn = get_db_connection()
        conn.execute(
            """INSERT INTO tickets
               (user_id, title, description, category, priority, summary, status)
               VALUES (?, ?, ?, ?, ?, ?, 'Pending')""",
            (
                session["user_id"],
                title,
                description,
                ai_result["category"],
                ai_result["priority"],
                ai_result["summary"],
            ),
        )
        conn.commit()
        conn.close()

        flash("Ticket created successfully!", "success")
        return redirect(url_for("ticket.dashboard"))

    return render_template("create_ticket.html")


@ticket_bp.route("/ticket/<int:ticket_id>/close")
def close_ticket(ticket_id):
    if not login_required():
        return redirect(url_for("login.login"))

    conn = get_db_connection()
    conn.execute("UPDATE tickets SET status = 'Closed' WHERE id = ?", (ticket_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("ticket.dashboard"))
