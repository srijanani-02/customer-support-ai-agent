from langchain_chroma import Chroma
from rag.embeddings import get_embedding_model

_vectorstore = None
_retriever = None


def get_retriever():
    global _vectorstore, _retriever

    if _retriever is None:

        print("Loading Embedding Model...")

        embedding_model = get_embedding_model()

        print("Opening ChromaDB...")

        _vectorstore = Chroma(
            persist_directory="chroma_db",
            embedding_function=embedding_model
        )

        _retriever = _vectorstore.as_retriever(
            search_kwargs={"k": 3}
        )

    return _retriever


if __name__ == "__main__":

    retriever = get_retriever()

    docs = retriever.invoke(
        "How do I reset my password?"
    )

    for doc in docs:
        print(doc.page_content)