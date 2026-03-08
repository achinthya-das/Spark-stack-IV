import sqlite3

DB_NAME = "employees.db"


def get_leave_balance(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT leave_balance FROM employees WHERE name=?",
        (name.title(),)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]

    return None


def update_leave_balance(name, new_balance):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE employees SET leave_balance=? WHERE name=?",
        (new_balance, name.title())
    )

    conn.commit()
    conn.close()


def add_employee(name, leave_balance=20):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO employees (name, leave_balance) VALUES (?, ?)",
        (name.title(), leave_balance)
    )

    conn.commit()
    conn.close()