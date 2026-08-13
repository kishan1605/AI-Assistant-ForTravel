from src.embedding import get_embeddings
from src.vectorstore import get_qdrant
from src.config import COLLECTION_NAME

async def get_response(query:str , top_k = 5):

    client = get_qdrant()

    query_vector = get_embeddings([query])[0]

    res = client.query_points(
        collection_name = COLLECTION_NAME,
        query = query_vector,
        limit = top_k
    )

    print("Retrival successful...")
    out = [hit.payload.get("text") for hit in res.points]
    return out

