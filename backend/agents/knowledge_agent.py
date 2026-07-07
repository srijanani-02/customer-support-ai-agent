from graph.state import AgentState

from rag.retriever import get_retriever

from utils.llm import (
    get_llm,
    llm_fallback,
)


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

    # --------------------------------------------------
    # Documents found in RAG
    # --------------------------------------------------

    if len(docs) > 0:

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        prompt = f"""
You are SmartAssist, an AI Customer Support Assistant.

Answer ONLY using the given context.

Rules:

- Never invent information.
- Never answer outside the provided context.
- If the answer cannot be found in the context, reply EXACTLY:

I couldn't find this information in our knowledge base.

Context:
{context}

Customer Question:
{state["user_query"]}
"""

        llm = get_llm()

        response = llm.invoke(prompt)

        answer = response.content.strip()

        # --------------------------------------------------
        # RAG couldn't answer -> Use Groq
        # --------------------------------------------------

        if "couldn't find this information in our knowledge base" in answer.lower():

            print("RAG could not answer. Using Groq fallback...")

            fallback = llm_fallback(
                state["user_query"],
                state["intent"]
            )

            state["response"] = fallback

            print("Fallback Response:", fallback)

            return state

        # --------------------------------------------------
        # RAG answered successfully
        # --------------------------------------------------

        state["response"] = answer

        print("Knowledge Agent completed.")

        return state

    # --------------------------------------------------
    # No documents retrieved -> Use Groq
    # --------------------------------------------------

    print("No documents found. Using Groq fallback...")

    fallback = llm_fallback(
        state["user_query"],
        state["intent"]
    )

    state["response"] = fallback

    print("Fallback Response:", fallback)

    return state