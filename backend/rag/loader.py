from pathlib import Path
from langchain_community.document_loaders import PyPDFDirectoryLoader


def load_documents():
    """
    Load all PDF files from the knowledge_base folder.
    """

    knowledge_base = Path(__file__).parent.parent / "knowledge_base"

    loader = PyPDFDirectoryLoader(str(knowledge_base))

    documents = loader.load()

    return documents


# Test Loader
if __name__ == "__main__":
    docs = load_documents()

    print(f"\nDocuments Loaded: {len(docs)}\n")

    for doc in docs:
        print(doc.metadata["source"])