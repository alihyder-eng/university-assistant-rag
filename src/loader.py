from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    """
    Load a single PDF.

    Args:
        file_path (str): Path to PDF

    Returns:
        list: LangChain Document objects
    """
    loader = PyPDFLoader(file_path)
    return loader.load()


def load_all_pdfs(data_dir="data"):
    """
    Load all PDFs from the data directory.

    Args:
        data_dir (str)

    Returns:
        list
    """
    documents = []

    pdf_files = Path(data_dir).glob("*.pdf")

    for pdf in pdf_files:
        print(f"Loading: {pdf.name}")

        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())

    print(f"\nLoaded {len(documents)} pages.")

    return documents


if __name__ == "__main__":
    docs = load_all_pdfs()
    print(docs[0].page_content[:500])