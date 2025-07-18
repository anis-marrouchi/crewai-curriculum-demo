from crewai import Task
from typing import List, Dict, Any

def create_objectives_task(agent, course_idea: str, target_audience: str) -> Task:
    return Task(
        description=f"""Create 3-5 SMART learning objectives for a course on "{course_idea}" 
        targeting "{target_audience}". Each objective should use Bloom's taxonomy verbs and be measurable.""",
        expected_output="A JSON array of 3-5 SMART learning objectives as strings",
        agent=agent
    )

def create_lessons_task(agent, objectives: List[str]) -> Task:
    return Task(
        description=f"""Create one detailed lesson blueprint for each of these objectives: {objectives}
        Each blueprint should include: title, hook, explanation, practice activity, reflection, and estimated time.""",
        expected_output="A JSON array of lesson blueprints with the specified structure",
        agent=agent
    )

def create_assessments_task(agent, lessons: List[Dict[str, Any]]) -> Task:
    return Task(
        description=f"""Create assessments for these lessons: {lessons}
        For each lesson, provide 2 MCQs and 1 short answer question that align with the learning objectives.""",
        expected_output="A JSON array of assessments with MCQs and short answers",
        agent=agent
    )

def create_review_task(agent, curriculum_data: Dict[str, Any]) -> Task:
    return Task(
        description=f"""Review this curriculum for alignment and quality: {curriculum_data}
        Check if objectives, lessons, and assessments are well-aligned. Provide PASS/FAIL and notes.""",
        expected_output="A review summary with PASS/FAIL status and improvement notes",
        agent=agent
    )
