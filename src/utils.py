from pathlib import Path


def print_separator():

    print("=" * 60)


def get_pdf_files(data_dir="data"):

    return list(Path(data_dir).glob("*.pdf"))


def format_sources(source_documents):

    sources = []

    for doc in source_documents:

        source = doc.metadata.get("source", "Unknown")

        page = doc.metadata.get("page", "N/A")

        sources.append(
            f"{source} (Page {page})"
        )

    return list(set(sources))