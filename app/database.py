import sqlite3

def save_purchase(user, amount):

    connection = sqlite3.connect("kubergold.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchases
    (
        user TEXT,
        amount INTEGER
    )
    """)

    cursor.execute(
        "INSERT INTO purchases VALUES (?,?)",
        (user, amount)
    )

    connection.commit()
    connection.close()