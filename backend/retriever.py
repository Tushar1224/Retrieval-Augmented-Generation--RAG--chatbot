# backend/retriever.py

import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np
import os

# Load FAISS index and documents
SOURCE_FOLDER = str(os.getcwd())
print(os.path.join(SOURCE_FOLDER, "vector_store.faiss"))
faiss_index = faiss.read_index(os.path.join(SOURCE_FOLDER, "vector_store.faiss"))
with open(os.path.join(SOURCE_FOLDER, "documents.pkl"), "rb") as f:
    documents = pickle.load(f)

# Load embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_docs(query, top_k=3):
    print("Retrieving documents")
    query_embedding = embedder.encode([query])
    D, I = faiss_index.search(np.array(query_embedding), top_k)
    
    results = []
    for idx, score in zip(I[0], D[0]):
        if score < 0.75:  # Threshold (lower is better in FAISS L2 distance)
            continue
        results.append(documents[idx])
    return results
