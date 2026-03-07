from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


@tool
def screen_resume(resume: str, job_description: str) -> str:
    """
    Screen a candidate resume against a job description.
    """

    prompt = ChatPromptTemplate.from_template("""
You are a recruitment AI.

Compare the candidate resume with the job description.

Resume:
{resume}

Job Description:
{job_description}

Determine:

- Skill match
- Experience match
- Overall suitability

Give a short evaluation.
""")

    chain = prompt | llm

    response = chain.invoke({
        "resume": resume,
        "job_description": job_description
    })

    return response.content


@tool
def match_candidate_to_job(skills: str, job_requirements: str) -> str:
    """
    Check how well candidate skills match job requirements.
    """

    prompt = ChatPromptTemplate.from_template("""
Compare candidate skills with job requirements.

Candidate Skills:
{skills}

Job Requirements:
{job_requirements}

Return a percentage match and explanation.
""")

    chain = prompt | llm

    response = chain.invoke({
        "skills": skills,
        "job_requirements": job_requirements
    })

    return response.content


@tool
def rank_candidates(candidate_list: str) -> str:
    """
    Rank multiple candidates based on their skills and experience.
    """

    prompt = ChatPromptTemplate.from_template("""
You are a recruitment assistant.

Rank the following candidates based on:

- Skills
- Experience
- Job relevance

Candidates:
{candidate_list}

Return a ranked list from best to worst.
""")

    chain = prompt | llm

    response = chain.invoke({
        "candidate_list": candidate_list
    })

    return response.content