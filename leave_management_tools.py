from langchain.tools import tool
from employee_database import get_leave_balance, update_leave_balance

leave_requests = []


@tool
def apply_leave(employee_name: str, days: int) -> str:
    """Employee applies for leave"""

    employee_name = employee_name.title()

    balance = get_leave_balance(employee_name)

    if balance is None:
        return f"{employee_name} not found in database."

    if balance < days:
        return f"Only {balance} leave days remaining."

    request = {
        "employee": employee_name,
        "days": days,
        "status": "Pending"
    }

    leave_requests.append(request)

    return f"Leave request submitted for {employee_name} for {days} days."


@tool
def approve_leave(employee_name: str) -> str:
    """Manager approves leave"""

    employee_name = employee_name.title()

    for request in leave_requests:

        if request["employee"] == employee_name and request["status"] == "Pending":

            balance = get_leave_balance(employee_name)

            new_balance = balance - request["days"]

            update_leave_balance(employee_name, new_balance)

            request["status"] = "Approved"

            return f"Leave approved for {employee_name}."

    return "No pending leave request."


@tool
def check_leave_balance(employee_name: str) -> str:
    """Check leave balance"""

    employee_name = employee_name.title()

    balance = get_leave_balance(employee_name)

    if balance is None:
        return "Employee not found."

    return f"{employee_name} has {balance} leave days remaining."


@tool
def allocate_leave(employee_name: str, days: int) -> str:
    """HR allocates additional leave"""

    employee_name = employee_name.title()

    balance = get_leave_balance(employee_name)

    if balance is None:
        return "Employee not found."

    new_balance = balance + days

    update_leave_balance(employee_name, new_balance)

    return f"{days} leave days allocated to {employee_name}."