from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model


def get_retriever():

    embedding_model = get_embedding_model()

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    query = "How do I reset my password?"

    docs = retriever.invoke(query)

    print("\nRetrieved Documents:\n")

    for doc in docs:
        print("=" * 60)
        print(doc.page_content)