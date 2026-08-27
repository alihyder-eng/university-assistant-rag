import os
from dotenv import load_dotenv

from langchain_chroma import Chroma

from loader import load_all_pdfs
from text_splitter import split_documents
from embeddings import load_embeddings

load_dotenv()

CHROMA_PATH = os.getenv("CHROMA_DB", "chroma_db")


def create_vector_db():
    """
    Create a new Chroma vector database.
    """

    print("Loading PDFs...")
    documents = load_all_pdfs()

    print("Splitting documents...")
    chunks = split_documents(documents)

    print("Loading embeddings...")
    embeddings = load_embeddings()

    print("Creating vector database...")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
    )

    print(f"Stored {len(chunks)} chunks.")
    return db


def load_vector_db():
    """
    Load an existing Chroma database.
    """

    embeddings = load_embeddings()

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
    )

    return db


if __name__ == "__main__":
    create_vector_db()