import json
import sys
import os
import streamlit as st
from dotenv import load_dotenv

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
load_dotenv(os.path.join(project_root, '.env'))

from src.crew import CurriculumCrew

load_dotenv()
st.set_page_config(page_title="CrewAI Curriculum Generator", layout="wide")
st.title("🤖 CrewAI Multi-Agent Curriculum Generator")
st.markdown("*Showcasing specialized AI agents collaborating on curriculum development*")

# Add agent description
with st.expander("Meet the AI Agents"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🎯 Objective Agent**")
        st.markdown("Creates SMART learning objectives using Bloom's taxonomy")
        
        st.markdown("**📚 Lesson Designer**") 
        st.markdown("Builds comprehensive lesson blueprints with hooks and activities")
    
    with col2:
        st.markdown("**📝 Assessment Creator**")
        st.markdown("Designs aligned MCQs and evaluation rubrics")
        
        st.markdown("**✅ Quality Reviewer**")
        st.markdown("Ensures alignment and maintains educational standards")

course_idea = st.text_input("Course idea", value="Introduction to Data Ethics")
audience = st.text_input("Target audience", value="Non-technical managers in fintech startups")
generate_btn = st.button("Generate curriculum")

if generate_btn and course_idea and audience:
    crew = CurriculumCrew()
    
    # Create progress tracking
    progress_bar = st.progress(0)
    status_text = st.empty()
    log_container = st.container()
    
    with log_container:
        st.subheader("CrewAI Multi-Agent Progress")
        workflow_logs = st.empty()
    
    # Initialize logs
    logs = []
    
    def update_progress(step, total, message):
        progress = step / total
        progress_bar.progress(progress)
        status_text.text(f"Agent {step}/{total}: {message}")
        logs.append(f"🤖 {message}")
        workflow_logs.text("\n".join(logs))
    
    try:
        update_progress(1, 4, "Objective Agent: Analyzing course requirements...")
        import time
        time.sleep(1)
        
        update_progress(2, 4, "Lesson Designer: Creating comprehensive blueprints...")
        time.sleep(1)
        
        update_progress(3, 4, "Assessment Creator: Designing aligned evaluations...")
        time.sleep(1)
        
        update_progress(4, 4, "Quality Reviewer: Ensuring curriculum alignment...")
        time.sleep(0.5)
        
        # Execute CrewAI workflow
        result = crew.generate_curriculum(course_idea, audience)
        
        progress_bar.progress(1.0)
        status_text.text("✅ CrewAI agents completed successfully!")
        logs.append("✅ Multi-agent collaboration complete")
        workflow_logs.text("\n".join(logs))
        
    except Exception as e:
        st.error(f"Error during CrewAI execution: {str(e)}")
        st.write("**Debug info:**")
        st.write(f"Error type: {type(e).__name__}")
        st.write(f"Error details: {str(e)}")
        st.stop()

    # Display agent collaboration details
    agent_meta = result.package_json.get("agent_collaboration", {})
    if agent_meta:
        st.info(f"🤖 {agent_meta.get('agents_used', 4)} specialized agents collaborated using {agent_meta.get('workflow_type', 'sequential')} approach")
        
        with st.expander("Agent Contributions"):
            st.write("**Specializations:**")
            specializations = agent_meta.get("specializations", [])
            for i, spec in enumerate(specializations, 1):
                st.write(f"{i}. {spec.replace('_', ' ').title()}")

    st.subheader("Curriculum Preview")
    st.markdown(result.package_md)

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Assessment Details")
        for assessment in result.assessments:
            with st.expander(f"📝 {assessment['lesson_title']}"):
                st.write(f"**Objective Measured:** {assessment['objective_measured']}")
                st.write(f"**MCQs:** {len(assessment['mcqs'])}")
                st.write(f"**Short Answer:** {assessment['short_answer']['question']}")
    
    with col2:
        st.subheader("JSON Export")
        st.json(result.package_json)
        st.download_button(
            "Download JSON",
            data=json.dumps(result.package_json, indent=2),
            file_name="syllabus.json",
            mime="application/json",
        )

    st.subheader("Quality Review")
    st.success(result.review_notes)
