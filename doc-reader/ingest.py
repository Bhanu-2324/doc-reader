import faiss
import os
import pickle
from utils.loader import load_pdf
from utils.chunker import chunk_text
from utils.embeddings import embed_text

VECTOR_DIR = "vectorstore"
os.makedirs(VECTOR_DIR, exist_ok=True)

def ingest_pdf(path):
    text = load_pdf(path)
    chunks = chunk_text(text)
    vectors = embed_text(chunks)

    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    faiss.write_index(index, f"{VECTOR_DIR}/index.faiss")

    with open(f"{VECTOR_DIR}/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("Ingestion complete")

if __name__ == "__main__":
    ingest_pdf("data/uploads/sample.pdf")