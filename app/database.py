import sqlite3
from datetime import datetime

def save_purchase(user, amount, grams):

    connection = sqlite3.connect("gold.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        amount INTEGER,
        grams REAL,
        timestamp TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO purchases (user, amount, grams, timestamp) VALUES (?,?,?,?)",
        (user, amount, grams, datetime.now().isoformat())
    )

    connection.commit()
    connection.close()