from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


KNOWLEDGE_BASE = Path("knowledge_base")


def load_documents():

    documents = []

    pdf_files = KNOWLEDGE_BASE.glob("*.pdf")

    for pdf in pdf_files:

        loader = PyPDFLoader(str(pdf))

        docs = loader.load()

        documents.extend(docs)

    return documents