from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


def load_embeddings():
    """
    Load embedding model.

    Returns:
        HuggingFaceEmbeddings
    """

    model_name = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2",
    )

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        },
    )

    return embeddings


if __name__ == "__main__":

    embeddings = load_embeddings()

    vector = embeddings.embed_query(
        "What is FAST University admission policy?"
    )

    print(len(vector))