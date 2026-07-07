from langchain_huggingface import HuggingFaceEmbeddings

_embedding_model = None


def get_embedding_model():
    global _embedding_model

    if _embedding_model is None:
        print("Loading Embedding Model...")

        _embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    return _embedding_model


if __name__ == "__main__":

    embedding_model = get_embedding_model()

    vector = embedding_model.embed_query(
        "How do I reset my password?"
    )

    print(len(vector))