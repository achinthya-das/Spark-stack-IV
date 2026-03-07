from langchain.tools import tool
from employee_database import employees, leave_balance


@tool
def hire_employee(name: str, role: str, salary: str) -> str:
    """
    Add a new employee to the company database.
    """

    from employee_database import add_employee

    add_employee(name, 20)

    return f"{name} has been hired as {role} with salary {salary}."


@tool
def fire_employee(name: str) -> str:
    """
    Remove an employee from the company database.
    """

    if name not in employees:
        return "Employee not found."

    del employees[name]
    del leave_balance[name]

    return f"{name} has been removed from the company."