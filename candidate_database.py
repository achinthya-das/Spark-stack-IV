import sqlite3

DB_NAME = "employees.db"

def add_candidate(name, resume, status="Applied"):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO candidates VALUES (?, ?, ?)",
        (name.title(), resume, status)
    )

    conn.commit()
    conn.close()


def get_all_candidates():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM candidates")

    data = cursor.fetchall()

    conn.close()

    return data