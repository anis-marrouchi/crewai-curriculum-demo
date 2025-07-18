from crewai import Agent
from ..llm import get_llm

assessment_agent = Agent(
    role="Assessment Specialist",
    goal="Create valid assessments that measure learning outcomes",
    backstory="""You are an expert in educational assessment with deep knowledge of
    creating MCQs, short answers, and practical exercises that accurately measure
    whether learning objectives have been achieved.""",
    llm=get_llm(),
    verbose=True,
    allow_delegation=False
)
