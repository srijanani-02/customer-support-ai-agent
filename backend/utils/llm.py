import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

print("Loading OpenRouter Model...")

llm = ChatOpenAI(
    model=os.getenv("OPENROUTER_MODEL"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.3,
    default_headers={
        "HTTP-Referer": "http://localhost:5173",
        "X-Title": "SmartAssist Customer Support AI",
    },
)


def get_llm():
    return llm