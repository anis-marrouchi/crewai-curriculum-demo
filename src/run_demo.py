import json
import sys
import os
from dotenv import load_dotenv

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
load_dotenv(os.path.join(project_root, '.env'))

from src.crew import CurriculumCrew

def main():
    crew = CurriculumCrew()
    result = crew.generate_curriculum(
        course_idea="Introduction to Data Ethics",
        target_audience="Non-technical managers in fintech startups"
    )
    
    print(result.package_md)
    with open("syllabus.json", "w") as f:
        json.dump(result.package_json, f, indent=2)

if __name__ == "__main__":
    main()
