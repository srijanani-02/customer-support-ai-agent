from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.loader import load_documents


def split_documents():
    """
    Split the loaded documents into smaller chunks.
    """

    documents = load_documents()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


# Test Splitter
if __name__ == "__main__":
    chunks = split_documents()

    print(f"\nTotal Chunks Created: {len(chunks)}\n")

    print("First Chunk:\n")
    print(chunks[0].page_content)