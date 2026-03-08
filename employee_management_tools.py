from langchain.tools import tool
from employee_database import get_leave_balance, update_leave_balance
import sqlite3


@tool
def hire_employee(name: str, role: str, salary: str) -> str:
    """
    Add a new employee to the company database.
    """
    import agent
    from employee_database import add_employee
    if not agent.current_role or agent.current_role.lower() not in ["hr", "manager"]:
        return "Only HR or Managers can hire employees."

    add_employee(name, 20)

    return f"{name} has been hired as {role} with salary {salary}."


import sqlite3

DB_NAME = "employees.db"

import sqlite3
from langchain.tools import tool

DB_NAME = "employees.db"

@tool
def fire_employee(name: str) -> str:
    """Remove employee from company database"""

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE name=?",
        (name.title(),)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return "Employee not found."

    conn.close()

    return f"{name} has been removed from the company."


