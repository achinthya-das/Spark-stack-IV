import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    name TEXT PRIMARY KEY,
    leave_balance INTEGER
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates (
    name TEXT PRIMARY KEY,
    resume TEXT,
    status TEXT
)
""")

employees = [
    ("Varun", 10),
    ("Rahul", 8),
    ("Ananya", 12)
]

cursor.executemany(
    "INSERT OR IGNORE INTO employees VALUES (?, ?)",
    employees
)

conn.commit()
conn.close()


print("Database initialized.")
