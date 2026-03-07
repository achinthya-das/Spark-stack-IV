import sqlite3

DB_NAME = "employees.db"


def get_leave_balance(employee_name):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT leave_balance FROM employees WHERE name=?",
        (employee_name,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None


def update_leave_balance(employee_name, new_balance):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE employees SET leave_balance=? WHERE name=?",
        (new_balance, employee_name)
    )

    conn.commit()
    conn.close()


def add_employee(name, leave_days):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees VALUES (?, ?)",
        (name.title(), leave_days)
    )

    conn.commit()
    conn.close()