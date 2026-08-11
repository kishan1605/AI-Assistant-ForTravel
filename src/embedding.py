from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embeddings(data):
    embeddings = model.encode(data).tolist()
    return embeddings