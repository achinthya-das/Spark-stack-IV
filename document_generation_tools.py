from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


@tool
def generate_offer_letter(name: str, position: str, salary: str) -> str:
    """
    Generate an offer letter for a selected candidate.
    """

    prompt = ChatPromptTemplate.from_template("""
Generate a professional offer letter.

Candidate Name: {name}
Position: {position}
Salary: {salary}

Include:

- Congratulations
- Job role
- Salary details
- Joining instructions
- Professional closing
""")

    chain = prompt | llm

    response = chain.invoke({
        "name": name,
        "position": position,
        "salary": salary
    })

    return response.content


@tool
def generate_experience_letter(name: str, role: str, years: str) -> str:
    """
    Generate an employee experience letter.
    """

    prompt = ChatPromptTemplate.from_template("""
Generate a professional experience letter.

Employee Name: {name}
Role: {role}
Years Worked: {years}

Mention:

- Employee contribution
- Role responsibilities
- Appreciation
""")

    chain = prompt | llm

    response = chain.invoke({
        "name": name,
        "role": role,
        "years": years
    })

    return response.content


@tool
def generate_relieving_letter(name: str, role: str) -> str:
    """
    Generate a relieving letter when an employee leaves the company.
    """

    prompt = ChatPromptTemplate.from_template("""
Generate a professional relieving letter.

Employee Name: {name}
Role: {role}

Mention:

- Employee served the company
- All duties handed over
- Wish them success
""")

    chain = prompt | llm

    response = chain.invoke({
        "name": name,
        "role": role
    })

    return response.content