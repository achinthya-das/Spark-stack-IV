from langchain.tools import tool
from employee_database import employees

# Simulated data
candidates = [
    {"name": "Alice", "status": "Interviewed"},
    {"name": "Bob", "status": "Hired"},
    {"name": "Charlie", "status": "Rejected"},
    {"name": "David", "status": "Interviewed"}
]

employees = ["Alice", "Bob", "Eve"]

leave_data = {
    "Alice": 3,
    "Bob": 5,
    "Eve": 2
}


@tool
def get_total_candidates() -> str:
    """
    Return total number of candidates in the recruitment pipeline.
    """

    return f"Total candidates in system: {len(candidates)}"


@tool
def get_total_employees() -> str:
    """
    Return total number of employees.
    """

    return f"Total employees in company: {len(employees)}"


@tool
def get_leave_summary() -> str:
    """
    Show how many leave days employees have taken.
    """

    summary = "\n".join([f"{emp}: {days} leave days taken"
                         for emp, days in leave_data.items()])

    return f"Leave Summary:\n{summary}"


@tool
def get_interview_stats() -> str:
    """
    Show interview statistics.
    """

    interviewed = sum(1 for c in candidates if c["status"] == "Interviewed")
    hired = sum(1 for c in candidates if c["status"] == "Hired")
    rejected = sum(1 for c in candidates if c["status"] == "Rejected")

    return f"""
Interview Statistics:
Interviewed: {interviewed}
Hired: {hired}
Rejected: {rejected}
"""