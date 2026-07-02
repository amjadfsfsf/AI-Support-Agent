import sqlite3

conn = sqlite3.connect("support.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    email TEXT,

    issue TEXT,

    status TEXT
)
""")

conn.commit()