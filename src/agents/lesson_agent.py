from crewai import Agent
from ..llm import get_llm

lesson_agent = Agent(
    role="Curriculum Designer",
    goal="Design engaging, effective lesson plans that achieve learning objectives",
    backstory="""You are a master curriculum designer who creates comprehensive lesson
    blueprints. You excel at designing hooks, explanations, practice activities, and
    reflection exercises that keep learners engaged.""",
    llm=get_llm(),
    verbose=True,
    allow_delegation=False
)
