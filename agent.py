from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv
current_user=None

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")



from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Import all tools
from resume_parser_tool import parse_resume
from recruitment_tools import screen_resume, match_candidate_to_job, rank_candidates
from hr_chatbot_tool import hr_chatbot
from leave_management_tools import apply_leave, approve_leave, check_leave_balance
from document_generation_tools import generate_offer_letter, generate_experience_letter, generate_relieving_letter
from calendar_tools import find_available_slots, schedule_interview, send_calendar_invite
from analytics_tools import get_total_candidates, get_total_employees, get_leave_summary, get_interview_stats
from employee_management_tools import hire_employee, fire_employee


# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# List of all tools
tools = [
    parse_resume,
    screen_resume,
    match_candidate_to_job,
    rank_candidates,
    hr_chatbot,
    apply_leave,
    approve_leave,
    check_leave_balance,
    generate_offer_letter,
    generate_experience_letter,
    generate_relieving_letter,
    find_available_slots,
    schedule_interview,
    send_calendar_invite,
    get_total_candidates,
    get_total_employees,
    get_leave_summary,
    get_interview_stats,
    hire_employee,
    fire_employee
]
SYSTEM_PROMPT = """
You are an AI HR assistant.

You help with:
- resume screening
- HR questions
- leave management
- interview scheduling
- employee management
- analytics

Use tools whenever needed.
"""


# Create the agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    memory=memory
    verbose=True,
    agent_kwargs={"system_message": SYSTEM_PROMPT}
)


# Run the agent
while True:

    user_input = input("\nAsk HR Agent: ")
    # detect name introduction
    if user_input.lower().startswith("i am"):
        current_user = user_input.split("i am")[-1].strip()
        print(f"\nAgent: Hello {current_user}. How can I help you today?")
        continue

    if user_input.lower() == "exit":
        break

    if current_user and "leave" in user_input.lower():
        user_input = f"{current_user} wants to apply leave. {user_input}"

    response = agent.run(user_input)

    print("\nAgent:", response)