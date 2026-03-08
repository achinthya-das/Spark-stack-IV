
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pypdf import PdfReader

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def read_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

@tool
def parse_resume(file_path: str) -> str:
    """
    Parse a resume PDF and extract structured information.
    """

    resume_text = read_pdf(file_path)

    prompt = ChatPromptTemplate.from_template("""
Extract the following details from the resume:

- Name
- Email
- Skills
- Education
- Years of Experience

Resume:
{resume_text}
""")

    chain = prompt | llm

    response = chain.invoke({
        "resume_text": resume_text
    })

    return response.content
