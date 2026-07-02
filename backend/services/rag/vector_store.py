from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from .document_loader import load_documents
from .chunk_service import split_documents
from .embedding_service import get_embedding

COLLECTION_NAME = "knowledge_base"

client = QdrantClient(
    host="localhost",
    port=6333,
)


def create_collection():

    collections = client.get_collections().collections

    names = [c.name for c in collections]

    if COLLECTION_NAME in names:
        print("Collection already exists.")
        return

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=768,
            distance=Distance.COSINE,
        ),
    )

    print("Collection created.")


def index_documents():

    documents = load_documents()

    chunks = split_documents(documents)

    points = []

    for idx, chunk in enumerate(chunks):

        vector = get_embedding(chunk.page_content)

        points.append(
            PointStruct(
                id=idx,
                vector=vector,
                payload={
                    "text": chunk.page_content,
                    "source": chunk.metadata["source"],
                    "page": chunk.metadata["page"],
                },
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )

    print(f"Indexed {len(points)} chunks.")