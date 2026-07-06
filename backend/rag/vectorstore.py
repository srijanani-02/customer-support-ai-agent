from langchain_chroma import Chroma
from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embedding_model


def create_vector_store():

    chunks = split_documents()

    embedding_model = get_embedding_model()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    return vectorstore


if __name__ == "__main__":

    db = create_vector_store()

    print("✅ Vector Store Created Successfully!")