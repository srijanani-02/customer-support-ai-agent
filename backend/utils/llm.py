import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

print("Loading Groq Model...")

llm = ChatGroq(
    model=os.getenv("GROQ_MODEL"),
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
)


def get_llm():
    return llm


# --------------------------------------------------
# LLM Fallback when RAG cannot answer
# --------------------------------------------------

def llm_fallback(user_query: str, intent: str) -> str:

    prompt = f"""
You are SmartAssist, an AI Customer Support Assistant.

The company's knowledge base could not answer the user's question.

Detected Intent:
{intent}

Customer Query:
{user_query}

Your job is to decide whether to continue the conversation or escalate.

====================================================
CONTINUE THE CONVERSATION
====================================================

Reply naturally if the user:

- needs troubleshooting help
- describes a problem
- asks a vague question
- asks for clarification
- needs guidance
- is explaining an issue

Examples:

User: I need help
Assistant: I'd be happy to help. Could you tell me more about the issue you're facing?

User: Password
Assistant: Are you trying to reset, recover, or change your password?

User: Login issue
Assistant: Could you describe the login issue you're experiencing?

User: My app isn't working
Assistant: I'm sorry you're experiencing that. Could you tell me what happens when you open the app?

====================================================
ESCALATE
====================================================

Reply ONLY with:

ESCALATE

if the request needs:

- official company policy
- refund policy
- refund processing
- order status
- shipment tracking
- payment information
- invoices
- customer account information
- account modifications
- deleting an account
- money transfer
- any company-specific information not present in the knowledge base
- anything requiring human intervention

Never choose ESCALATE for troubleshooting or general support.

Reply ONLY with either:

1. A helpful conversational response

OR

2. ESCALATE

Do not explain your decision.
"""

    response = llm.invoke(prompt)

    return response.content.strip()