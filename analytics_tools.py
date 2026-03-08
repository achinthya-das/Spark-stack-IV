from langchain.tools import tool

# Simulated data
candidates = [
    {"name": "Alice", "status": "Interviewed"},
    {"name": "Bob", "status": "Hired"},
    {"name": "Charlie", "status": "Rejected"},
    {"name": "David", "status": "Interviewed"}
]


@tool
def get_total_candidates() -> str:
    """Return total number of candidates in database."""
    
    import sqlite3

    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM candidates")
    total = cursor.fetchone()[0]

    conn.close()

    return f"Total candidates in system: {total}"


@tool
def get_total_employees() -> str:
    """Return total employees and their names from the database."""

    import sqlite3

    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM employees")
    employees = cursor.fetchall()

    conn.close()

    names = [emp[0] for emp in employees]

    return f"Total employees in company: {len(names)}\nEmployees: {', '.join(names)}"


@tool
def get_leave_summary() -> str:
    """Show leave balance summary of all employees."""

    import sqlite3

    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, leave_balance FROM employees")
    data = cursor.fetchall()

    conn.close()

    summary = "\n".join(
        [f"{name}: {balance} leave days remaining" for name, balance in data]
    )

    return f"Leave Summary:\n{summary}"


@tool
def get_interview_stats() -> str:
    """Return interview statistics."""

    return "Interview statistics feature currently uses simulated data."