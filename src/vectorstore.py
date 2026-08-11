from qdrant_client import QdrantClient
from qdrant_client.http.models import  VectorParams, Distance
from src.config import QDRANT_API_KEY, QDRANT_HOST, COLLECTION_NAME

def get_qdrant():
    return QdrantClient(
        url = QDRANT_HOST,
        api_key = QDRANT_API_KEY
    )

def init_qdrant():
    client = get_qdrant()

    existing_collections = [col.name for col in client.get_collections().collections]

    if COLLECTION_NAME not in existing_collections:
        print(f"creation collection {COLLECTION_NAME}")
        client.recreate_collection(
            collection_name = COLLECTION_NAME,
            vectors_config = VectorParams(size = 384, distance = Distance.COSINE)
        )

    return client