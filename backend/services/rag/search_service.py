from qdrant_client import QdrantClient
from .embedding_service import get_embedding

COLLECTION_NAME = "knowledge_base"

client = QdrantClient(
    host="localhost",
    port=6333,
)


def search(query: str, limit: int = 5):

    vector = get_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=limit,
    )

    return  results.points