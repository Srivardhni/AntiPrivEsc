import sqlite3

conn = sqlite3.connect("alerts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    process_name TEXT,
    pid INTEGER
)
""")

def log_alert(proc):
    cursor.execute(
        "INSERT INTO alerts (process_name, pid) VALUES (?, ?)",
        (proc['name'], proc['pid'])
    )
    conn.commit()