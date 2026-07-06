from graph.state import AgentState

from rag.retriever import get_retriever
from utils.gemini import get_llm


def knowledge_agent(state: AgentState):

    print("\nKnowledge Agent")

    retriever = get_retriever()

    docs = retriever.invoke(state["user_query"])

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a helpful customer support assistant.

Answer ONLY using the information below.

Context:
{context}

Question:
{state["user_query"]}
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    state["retrieved_docs"] = [doc.page_content for doc in docs]
    state["response"] = response.content

    return state