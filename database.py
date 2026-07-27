"""
database.py
------------
Ye file SQLite database banati hai aur zaroori tables create karti hai.
Isko sirf ek dafa run karna hai (python database.py) taake database.db file
project folder mein ban jaye.
"""

import sqlite3
from werkzeug.security import generate_password_hash

DB_NAME = "database.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # ---------- USERS TABLE ----------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user'   -- 'user' or 'admin'
        )
    """)

    # ---------- TICKETS TABLE ----------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT,
            priority TEXT,
            summary TEXT,
            status TEXT NOT NULL DEFAULT 'Pending',   -- Pending / In Progress / Closed
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    conn.commit()

    # ---------- Create a default admin account (only if it doesn't exist) ----------
    cursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))
    if cursor.fetchone() is None:
        hashed_pw = generate_password_hash("admin123")
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ("admin", hashed_pw, "admin"),
        )
        conn.commit()
        print("✅ Default admin created -> username: admin | password: admin123")

    conn.close()
    print("✅ Database and tables ready (database.db)")


if __name__ == "__main__":
    init_db()
