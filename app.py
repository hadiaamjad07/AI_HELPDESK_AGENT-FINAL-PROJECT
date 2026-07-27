"""
app.py
------
Ye main file hai jo Flask app ko start karti hai.
Run karne ke liye terminal mein likho:  python app.py
"""

from flask import Flask
from routes.login import login_bp
from routes.ticket import ticket_bp
from routes.chat import chat_bp
import os

app = Flask(__name__)
app.secret_key = "change-this-secret-key-later"  # session ke liye zaroori

# ---- Blueprints register karo ----
app.register_blueprint(login_bp)
app.register_blueprint(ticket_bp)
app.register_blueprint(chat_bp)


if __name__ == "__main__":
    # Agar database.db abhi tak nahi bana to warn karo
    if not os.path.exists("database.db"):
        print("⚠️  database.db nahi mila. Pehle 'python database.py' run karo.")
    app.run(debug=True, port=5000)
