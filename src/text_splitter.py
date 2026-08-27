
from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_documents(
    documents,
    chunk_size=1000,
    chunk_overlap=200,
):
    """
    Split documents into chunks.

    Args:
        documents
        chunk_size
        chunk_overlap

    Returns:
        list
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    return chunks


if __name__ == "__main__":

    from loader import load_all_pdfs

    docs = load_all_pdfs()

    chunks = split_documents(docs)

    print(chunks[0].page_content)