"""
Centralised LLM configuration for CrewAI
"""

import os
from functools import lru_cache
from crewai import LLM

@lru_cache
def get_llm():
    return LLM(
        model= os.getenv("LLM_MODEL"),
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.openai.com/v1"),
        temperature=0.2,
    )
