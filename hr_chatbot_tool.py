
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


@tool
def hr_chatbot(question: str) -> str:
    """
    Answer employee HR related questions like leave policy,
    company rules, HR contact, work timings, etc.
    """

    prompt = ChatPromptTemplate.from_template("""
You are an HR assistant for a company.

Answer employee HR questions clearly using the company policies below.

Company Policies:

- Employees get 20 paid leave days per year
- Sick leave allowed: 10 days
- Work from home allowed twice per week
- HR Manager: Priya Sharma
- Office timing: 9 AM – 6 PM
- Employees must apply leave at least 2 days in advance

Employee Question:
{question}
""")

    chain = prompt | llm

    response = chain.invoke({
        "question": question
    })

    return response.content
