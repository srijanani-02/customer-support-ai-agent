from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model


# Test
if __name__ == "__main__":

    embeddings = get_embedding_model()

    vector = embeddings.embed_query("How do I reset my password?")

    print(f"Embedding Dimension: {len(vector)}")

    print("\nFirst 10 Values:\n")

    print(vector[:10])