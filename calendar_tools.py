from langchain.tools import tool

# Simulated available interview slots
available_slots = [
    "Monday 10:00 AM",
    "Monday 2:00 PM",
    "Tuesday 11:00 AM",
    "Wednesday 3:00 PM"
]

scheduled_interviews = []


@tool
def find_available_slots() -> str:
    """
    Show available interview time slots.
    """

    if not available_slots:
        return "No interview slots available."

    return "Available interview slots:\n" + "\n".join(available_slots)


@tool
def schedule_interview(candidate_name: str, slot: str) -> str:
    """
    Schedule an interview for a candidate.
    """

    if slot not in available_slots:
        return "Selected slot is not available."

    interview = {
        "candidate": candidate_name,
        "slot": slot
    }

    scheduled_interviews.append(interview)
    available_slots.remove(slot)

    return f"Interview scheduled for {candidate_name} at {slot}."


@tool
def send_calendar_invite(candidate_name: str, slot: str) -> str:
    """
    Simulate sending a calendar invite.
    """

    return f"Calendar invite sent to {candidate_name} for interview at {slot}."