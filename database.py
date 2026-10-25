import sqlite3

def get_connection():
    return sqlite3.connect("glitch.db")

def init_db():
    with get_connection() as db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tarea TEXT NOT NULL,
                completa INTEGER NOT NULL DEFAULT 0
            )
        """)
        db.commit()