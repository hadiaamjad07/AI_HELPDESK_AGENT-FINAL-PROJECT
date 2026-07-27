"""
routes/chat.py
---------------
AI Chat page ka logic. User message bhejta hai, Ollama se jawab aata hai.
"""

from flask import Blueprint, render_template, request, jsonify, session
from ai.ollama import ask_ai

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["GET"])
def chat_page():
    if "user_id" not in session:
        return render_template("login.html")
    return render_template("chat.html")


@chat_bp.route("/api/chat", methods=["POST"])
def chat_api():
    """
    Ye endpoint website ke apne chat.html JS ke liye hai.
    Login session zaroori hai (browser cookie se).
    """
    if "user_id" not in session:
        return jsonify({"error": "Not logged in"}), 401

    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    ai_reply = ask_ai(user_message)
    return jsonify({"reply": ai_reply})


# ---- Simple shared-secret key for n8n (change this in a real project) ----
N8N_SECRET_KEY = "helpdesk-n8n-key-123"


@chat_bp.route("/api/webhook/chat", methods=["POST"])
def webhook_chat_api():
    """
    Ye endpoint sirf n8n (ya kisi bhi automation tool) ke liye hai.
    Isay login-session nahi chahiye — is liye ek simple secret key check
    karta hai taake koi bhi random request isay use na kar sake.

    n8n se call karte waqt header bhejna:
        X-API-KEY: helpdesk-n8n-key-123

    Body:
        { "message": "My internet is disconnected." }
    """
    key = request.headers.get("X-API-KEY")
    if key != N8N_SECRET_KEY:
        return jsonify({"error": "Invalid or missing API key"}), 403

    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    ai_reply = ask_ai(user_message)
    return jsonify({"reply": ai_reply})