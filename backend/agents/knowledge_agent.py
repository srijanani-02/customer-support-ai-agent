from graph.state import AgentState

from rag.retriever import get_retriever
from utils.llm import get_llm


def knowledge_agent(state: AgentState):

    print("\n========== Knowledge Agent ==========")

    # Inquiry Agent requested more information
    if state["needs_more_info"]:

        print("Waiting for additional information from user.")

        return state

    retriever = get_retriever()

    docs = retriever.invoke(state["user_query"])

    state["retrieved_docs"] = [
        doc.page_content for doc in docs
    ]

    # No documents found
    if len(docs) == 0:

        state["response"] = (
            "I couldn't find any relevant information "
            "in the knowledge base."
        )

        print("No documents retrieved.")

        return state

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are SmartAssist, an AI Customer Support Assistant.

You MUST answer ONLY from the given context.

If the answer is not present in the context, reply exactly:

I couldn't find this information in our knowledge base.

Do not make assumptions.
Do not generate information outside the context.

Context:
{context}

Customer Question:
{state["user_query"]}
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    state["response"] = response.content.strip()

    print("Knowledge Agent completed.")

    return state