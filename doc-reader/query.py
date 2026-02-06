import faiss
import pickle
from utils.embeddings import embed_text

VECTOR_DIR = "vectorstore"

def search(query, k=5):
    # Load FAISS index
    index = faiss.read_index(f"{VECTOR_DIR}/index.faiss")

    # Load stored chunks
    with open(f"{VECTOR_DIR}/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    # Embed the query
    query_vector = embed_text([query])

    # Search similar chunks
    distances, indices = index.search(query_vector, k)

    # Return matching chunks
    return [chunks[i] for i in indices[0]]
