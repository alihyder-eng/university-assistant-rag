from langchain.chains import RetrievalQA

from llm import load_llm
from retriever import create_retriever
from prompts import prompt


def create_rag_chain(vector_db=None):
    """
    Returns a RetrievalQA chain.
    """

    llm = load_llm()

    if vector_db is None:
        retriever = create_retriever()
    else:
        retriever = vector_db.as_retriever(
            search_kwargs={"k": 4}
        )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={
            "prompt": prompt
        },
    )

    return qa_chain


if __name__ == "__main__":

    chain = create_rag_chain()

    while True:

        question = input("\nQuestion: ")

        if question.lower() == "exit":
            break

        result = chain.invoke(
            {"query": question}
        )

        print("\nAnswer:\n")
        print(result["result"])

        print("\nSources:\n")

        for doc in result["source_documents"]:

            print(doc.metadata)