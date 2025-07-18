from typing import List, Dict, Any
from pydantic import BaseModel

class CurriculumTask(BaseModel):
    course_idea: str
    target_audience: str

class CurriculumOutput(BaseModel):
    learning_objectives: List[str]
    lesson_blueprints: List[Dict[str, Any]]
    assessments: List[Dict[str, Any]]
    review_notes: str
    package_md: str
    package_json: Dict[str, Any]
