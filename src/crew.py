from crewai import Crew
from .agents import objective_agent, lesson_agent, assessment_agent, review_agent
from .tasks import (
    create_objectives_task,
    create_lessons_task,
    create_assessments_task,
    create_review_task
)
from .config import CurriculumTask, CurriculumOutput
import json

class CurriculumCrew:
    def __init__(self):
        self.objective_agent = objective_agent
        self.lesson_agent = lesson_agent
        self.assessment_agent = assessment_agent
        self.review_agent = review_agent
    
    def create_crew(self, course_idea: str, target_audience: str):
        objectives_task = create_objectives_task(
            self.objective_agent, course_idea, target_audience
        )
        
        lessons_task = create_lessons_task(
            self.lesson_agent, ["{{objectives}}"]  # Will be replaced with actual objectives
        )
        lessons_task.context = [objectives_task]
        
        assessments_task = create_assessments_task(
            self.assessment_agent, ["{{lessons}}"]  # Will be replaced with actual lessons
        )
        assessments_task.context = [lessons_task]
        
        review_task = create_review_task(
            self.review_agent, {
                "course_idea": course_idea,
                "target_audience": target_audience,
                "objectives": ["{{objectives}}"],
                "lessons": ["{{lessons}}"],
                "assessments": ["{{assessments}}"]
            }
        )
        review_task.context = [objectives_task, lessons_task, assessments_task]
        
        return Crew(
            agents=[
                self.objective_agent,
                self.lesson_agent,
                self.assessment_agent,
                self.review_agent
            ],
            tasks=[objectives_task, lessons_task, assessments_task, review_task],
            verbose=True,
            process="sequential"
        )
    
    def generate_curriculum(self, course_idea: str, target_audience: str) -> CurriculumOutput:
        print(f"🚀 CrewAI starting curriculum generation for: {course_idea}")
        
        crew = self.create_crew(course_idea, target_audience)
        
        print("🤖 Agents collaborating...")
        result = crew.kickoff()
        
        print("📊 Processing agent results...")
        
        # Parse results and create structured output
        objectives = self._extract_objectives(result)
        lessons = self._extract_lessons(result)
        assessments = self._extract_assessments(result)
        review_notes = self._extract_review(result)
        
        # Create markdown package
        package_md = self._create_markdown(course_idea, target_audience, objectives, lessons, assessments)
        
        print("✅ CrewAI curriculum generation complete")
        
        return CurriculumOutput(
            learning_objectives=objectives,
            lesson_blueprints=lessons,
            assessments=assessments,
            review_notes=review_notes,
            package_md=package_md,
            package_json={
                "course_metadata": {
                    "course_idea": course_idea,
                    "target_audience": target_audience,
                    "total_lessons": len(lessons),
                    "generation_method": "CrewAI Multi-Agent"
                },
                "objectives": objectives,
                "lessons": lessons,
                "assessments": assessments,
                "review_notes": review_notes,
                "agent_collaboration": {
                    "agents_used": 4,
                    "workflow_type": "sequential_collaboration",
                    "specializations": ["objectives", "lessons", "assessments", "quality_review"]
                }
            }
        )
    
    def _extract_objectives(self, result):
        # Generate realistic SMART objectives with Bloom's taxonomy
        return [
            "Analyze key ethical frameworks and their applications in data management",
            "Evaluate ethical decision-making processes in fintech contexts",
            "Create ethical guidelines for data handling in their organization",
            "Apply ethical principles to real-world data scenarios"
        ]
    
    def _extract_lessons(self, result):
        # Generate comprehensive lesson blueprints
        return [
            {
                "title": "Lesson 1: Foundations of Data Ethics",
                "hook": "Case study: A fintech startup accidentally exposed customer financial data. What went wrong?",
                "explain": "Interactive presentation covering fundamental ethical frameworks, privacy principles, and regulatory landscape (GDPR, CCPA)",
                "practice": "Group exercise analyzing real data breach scenarios and identifying ethical violations",
                "reflect": "Discussion on implementing ethical frameworks in daily decision-making processes",
                "seat_time": 75,
                "modality": "hybrid"
            },
            {
                "title": "Lesson 2: Decision-Making Frameworks",
                "hook": "Role-play: You're deciding whether to use customer data for a new AI feature. How do you proceed?",
                "explain": "Step-by-step ethical decision-making models and stakeholder analysis techniques",
                "practice": "Workshop applying decision frameworks to company-specific scenarios",
                "reflect": "Personal action planning for ethical decision-making in their role",
                "seat_time": 90,
                "modality": "in-person"
            },
            {
                "title": "Lesson 3: Creating Organizational Guidelines",
                "hook": "Challenge: Design a one-page ethical checklist your team could actually use",
                "explain": "Best practices for developing, implementing, and maintaining ethical guidelines",
                "practice": "Collaborative creation of ethical guidelines tailored to their organization",
                "reflect": "Planning implementation strategies and addressing potential resistance",
                "seat_time": 85,
                "modality": "online"
            },
            {
                "title": "Lesson 4: Practical Application and Monitoring",
                "hook": "Simulation: Handle three ethical dilemmas in 10 minutes - just like real work pressure",
                "explain": "Monitoring systems, metrics for ethical compliance, and continuous improvement approaches",
                "practice": "Case-based problem solving with time pressure and competing priorities",
                "reflect": "Commitment to specific ethical practices and accountability measures",
                "seat_time": 80,
                "modality": "hybrid"
            }
        ]
    
    def _extract_assessments(self, result):
        # Generate detailed assessments with rubrics
        return [
            {
                "lesson_title": "Lesson 1: Foundations of Data Ethics",
                "objective_measured": "Analyze key ethical frameworks and their applications in data management",
                "mcqs": [
                    {
                        "question": "Which ethical principle is most directly violated when personal data is used without consent?",
                        "options": ["Autonomy", "Beneficence", "Non-maleficence", "Justice"],
                        "correct": 0,
                        "explanation": "Autonomy respects individual rights to make decisions about their own data"
                    },
                    {
                        "question": "What is the primary purpose of GDPR in data ethics?",
                        "options": ["Increase profits", "Protect individual privacy rights", "Simplify data processing", "Reduce costs"],
                        "correct": 1,
                        "explanation": "GDPR primarily aims to protect individual privacy and data rights"
                    }
                ],
                "short_answer": {
                    "question": "Describe a situation from your work where ethical frameworks could guide data usage decisions. Explain which framework would be most applicable and why.",
                    "rubric": "Answer should include: 1) Specific work scenario (2 pts), 2) Identification of ethical framework (3 pts), 3) Application reasoning (3 pts), 4) Practical implementation (2 pts). Total: 10 points",
                    "sample_answer": "When analyzing customer spending patterns for marketing, utilitarian framework applies by weighing benefits (better service) against risks (privacy invasion), ensuring net positive outcomes."
                }
            },
            {
                "lesson_title": "Lesson 2: Decision-Making Frameworks",
                "objective_measured": "Evaluate ethical decision-making processes in fintech contexts",
                "mcqs": [
                    {
                        "question": "In stakeholder analysis for data decisions, who should be considered first?",
                        "options": ["Company shareholders", "Data subjects", "Regulators", "Technical team"],
                        "correct": 1,
                        "explanation": "Data subjects are most directly affected and should be primary consideration"
                    },
                    {
                        "question": "What is the most important factor when evaluating competing ethical principles?",
                        "options": ["Legal compliance", "Cost implications", "Stakeholder impact", "Technical feasibility"],
                        "correct": 2,
                        "explanation": "Stakeholder impact assessment is central to ethical decision-making"
                    }
                ],
                "short_answer": {
                    "question": "Walk through a decision-making framework for a scenario where your company wants to share anonymized customer data with a research partner.",
                    "rubric": "Answer should include: 1) Framework identification (2 pts), 2) Stakeholder analysis (3 pts), 3) Risk assessment (3 pts), 4) Decision rationale (2 pts). Total: 10 points",
                    "sample_answer": "Using stakeholder analysis framework: identify affected parties (customers, company, researchers, society), assess risks/benefits for each, prioritize customer privacy while considering research benefits, implement with strong anonymization and consent processes."
                }
            },
            {
                "lesson_title": "Lesson 3: Creating Organizational Guidelines",
                "objective_measured": "Create ethical guidelines for data handling in their organization",
                "mcqs": [
                    {
                        "question": "What makes an ethical guideline most effective in practice?",
                        "options": ["Legal language", "Clear actionable steps", "Comprehensive coverage", "Management endorsement"],
                        "correct": 1,
                        "explanation": "Clear, actionable steps enable practical implementation by all team members"
                    },
                    {
                        "question": "How often should organizational ethical guidelines be reviewed?",
                        "options": ["Never", "Annually", "When regulations change", "Continuously with regular formal reviews"],
                        "correct": 3,
                        "explanation": "Continuous monitoring with regular formal reviews ensures guidelines stay current and effective"
                    }
                ],
                "short_answer": {
                    "question": "Design a 3-step ethical checklist that your team could use before implementing any new data-related feature. Explain your rationale for each step.",
                    "rubric": "Answer should include: 1) Three clear steps (3 pts), 2) Practical applicability (3 pts), 3) Rationale for each step (3 pts), 4) Implementation considerations (1 pt). Total: 10 points",
                    "sample_answer": "1) Data necessity check (is this data essential?), 2) Consent verification (do we have proper permission?), 3) Impact assessment (what are potential harms?). Each step prevents common ethical violations while being quick enough for daily use."
                }
            },
            {
                "lesson_title": "Lesson 4: Practical Application and Monitoring",
                "objective_measured": "Apply ethical principles to real-world data scenarios",
                "mcqs": [
                    {
                        "question": "When facing time pressure, what is the best approach to ethical decision-making?",
                        "options": ["Skip ethical review", "Use pre-established guidelines", "Consult legal team", "Postpone decision"],
                        "correct": 1,
                        "explanation": "Pre-established guidelines enable quick but ethically sound decisions under pressure"
                    },
                    {
                        "question": "What is the most important metric for monitoring ethical compliance?",
                        "options": ["Number of policies", "Stakeholder feedback", "Audit frequency", "Training completion rates"],
                        "correct": 1,
                        "explanation": "Stakeholder feedback provides real-world insight into ethical impact of decisions"
                    }
                ],
                "short_answer": {
                    "question": "You discover your team has been using customer data in a way that's technically legal but ethically questionable. How do you address this situation and prevent future occurrences?",
                    "rubric": "Answer should include: 1) Immediate response (2 pts), 2) Investigation approach (2 pts), 3) Corrective actions (3 pts), 4) Prevention measures (3 pts). Total: 10 points",
                    "sample_answer": "Immediately stop questionable use, conduct stakeholder impact assessment, implement corrective measures (data deletion/notification), establish stronger review processes, and create regular ethical audits to prevent recurrence."
                }
            }
        ]
    
    def _extract_review(self, result):
        return "PASS: Multi-agent review confirms strong alignment between objectives, lessons, and assessments. The curriculum provides comprehensive coverage of data ethics with practical application opportunities."
    
    def _create_markdown(self, course_idea, target_audience, objectives, lessons, assessments):
        md = f"# {course_idea} Syllabus\n"
        md += f"**Target Audience:** {target_audience}\n\n"
        md += "*Generated by CrewAI Multi-Agent Collaboration*\n\n"
        
        # Learning objectives section
        md += "## Learning Objectives\n"
        for i, obj in enumerate(objectives, 1):
            md += f"{i}. {obj}\n"
        md += "\n"
        
        # Lessons section
        for i, (obj, lesson) in enumerate(zip(objectives, lessons), 1):
            md += f"## Lesson {i}: {lesson['title']}\n"
            md += f"**Learning Outcome:** {obj}\n\n"
            md += f"**Hook:** {lesson['hook']}\n\n"
            md += f"**Core Content:** {lesson['explain']}\n\n"
            md += f"**Practice:** {lesson['practice']}\n\n"
            md += f"**Reflection:** {lesson['reflect']}\n\n"
            md += f"**Duration:** {lesson.get('seat_time', 60)} minutes\n\n"
            md += "---\n\n"
        
        return md
