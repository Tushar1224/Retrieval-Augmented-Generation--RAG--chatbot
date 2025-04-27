# backend/build_faiss_index.py

import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
import fitz

# Initialize
embedder = SentenceTransformer('all-MiniLM-L6-v2')
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)

# Directories
SOURCE_FOLDER = "C:\\Users\\tusha\\Downloads\\RAG_project\\backend\\data"  # Assuming your docs are inside /data folder
DOCS = []
CHUNKS = []



# Load all files
for filename in os.listdir(SOURCE_FOLDER):
    file_path = os.path.join(SOURCE_FOLDER, filename)

    if filename.endswith(".pdf"):
        doc = fitz.open(file_path)
        for page in doc:
            DOCS.append(page.get_text())

    elif filename.endswith(".docx"):
        doc = fitz.open(file_path)
        for page in doc:
            DOCS.append(page.get_text())



# Chunk documents
for doc in DOCS:
    chunks = text_splitter.split_text(doc)
    CHUNKS.extend(chunks)

print(f"Loaded {len(DOCS)} documents.")
print(f"Generated {len(CHUNKS)} chunks.")

# Embed chunks
embeddings = embedder.encode(CHUNKS, batch_size=32, show_progress_bar=True)

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index and documents
faiss.write_index(index, "vector_store.faiss")
with open("documents.pkl", "wb") as f:
    pickle.dump(CHUNKS, f)

print("✅ FAISS index and documents saved.")
