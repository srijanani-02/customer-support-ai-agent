from langchain_huggingface import HuggingFaceEmbeddings


print("Loading Embedding Model...")


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def get_embedding_model():

    return embedding_model


if __name__ == "__main__":

    vector = embedding_model.embed_query(
        "How do I reset my password?"
    )

    print(len(vector))