# CrewAI Curriculum Demo

Turns one course idea into a complete syllabus using CrewAI's multi-agent system.
Features specialized agents for objectives, lessons, assessments, and quality review.

## Quick-start

```bash
git clone <repo-url>
cd crewai-curriculum-demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env               # add your OpenAI key
streamlit run src/app_streamlit.py # or python -m src.run_demo
```

## Structure

```
crewai-curriculum-demo/
├── README.md
├── .env.example
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── llm.py            # central LLM configuration
│   ├── config.py         # crew configuration
│   ├── crew.py           # main crew setup
│   ├── run_demo.py
│   ├── app_streamlit.py
│   └── agents/           # specialized agents
```

## Agents

- **Objective Agent**: Creates SMART learning objectives
- **Lesson Designer**: Builds lesson blueprints
- **Assessment Creator**: Generates quizzes and exercises
- **Quality Reviewer**: Ensures alignment and quality
