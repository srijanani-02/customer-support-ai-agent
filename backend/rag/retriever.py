from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model


print("Loading Embedding Model...")

embedding_model = get_embedding_model()

print("Opening ChromaDB...")

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


def get_retriever():

    return retriever


if __name__ == "__main__":

    docs = retriever.invoke(
        "How do I reset my password?"
    )

    for doc in docs:

        print(doc.page_content)