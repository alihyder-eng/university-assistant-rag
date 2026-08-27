from vector_store import load_vector_db


def create_retriever():

    db = load_vector_db()

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 4
        }
    )

    return retriever


if __name__ == "__main__":

    retriever = create_retriever()

    docs = retriever.invoke(
        "What is the attendance policy?"
    )

    print(f"Retrieved {len(docs)} documents.\n")

    for doc in docs:
        print(doc.metadata)
        print(doc.page_content[:300])
        print("-" * 60)