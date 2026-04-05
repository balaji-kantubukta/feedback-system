
# SQLite helper functions for Student Feedback System
import sqlite3

def init_db(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS feedback (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    feedback TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

def insert_feedback(db_path, name, feedback):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('INSERT INTO feedback (name, feedback) VALUES (?, ?)', (name, feedback))
    conn.commit()
    conn.close()

def get_all_feedback(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT name, feedback FROM feedback ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows