# Retrieval-Augmented Generation (RAG) chatbot
 Retrieval-Augmented Generation (RAG) chatbot

command to run the application:
streamlit run app.py

Project Details:

Situation(Objective):

Develop a Retrieval-Augmented Generation (RAG) chatbot trained on customer support documentation to assist users by answering queries and providing relevant support information.
Tasks : 1. Your bot should be able to answer questions only based on information present in the sources shared with this email. 2. It should reply back with `I Don't know` if a question is asked from outside these information sources. 3. Build a user-friendly chatbot interface to demonstrate the chatbot

We aim to develop a Retrieval-Augmented Generation (RAG) based chatbot that assists users by answering customer support queries using a predefined set of documents.
The chatbot will only provide answers sourced from the uploaded documents and should respond with "I don't know" for any out-of-scope questions.

The sources include:

1. Medical insurance documents

2. Plan summaries

3. Policy rules

The final solution must have a simple, user-friendly interface demonstrating the chatbot capabilities.

Behavior(Solution):

 1. System Architecture
 Data ingestion: Upload customer support documents (PDFs, DOCXs).
 
 Text preprocessing: Split documents into chunks (e.g., 300–500 tokens).
 
 Embedding generation: Create vector embeddings of document chunks using a model (e.g., OpenAI, HuggingFace, or Gemini embeddings).
 
 Vector storage: Store embeddings in a vector database (e.g., FAISS, ChromaDB, Pinecone).
 
 2. Retrieval
 Query handling:
 
 User inputs a question.
 
 Query is embedded into the same vector space.
 
 Similar chunks (top-k matches) are retrieved from the database.
 
 3. Generation
 Prompt assembly:
 
 Combine retrieved context + user question.
 
 Send assembled prompt to a generative model (e.g., Gemini Pro).
 
 Post-processing:
 
 If no relevant context found (similarity score too low), respond "I don't know".
 
 Otherwise, generate a natural language answer based strictly on context.
 
 4. Frontend Interface
 Chatbot UI: Developed using Streamlit (or React).
 
 Features:
 
 Chat history.
 
 Loading indicators while fetching answer.
 
 Clear error messages.
 
 "New Chat" or "Reset" button.


Impact:
Accurate Support: Users receive correct answers only from trusted, vetted company documentation.

Risk Mitigation: Prevents hallucinated (fake) responses — if information is missing, clearly replies "I don't know".

Efficiency: Fast, automated support reduces human customer service workload.

User Experience: Provides a simple and smooth interaction interface, making it easy for non-technical users.

Scalability: The system can later scale to larger datasets or be integrated into customer-facing apps.


Tech Stack Summary


Document - ingestion	PyMuPDF, python-docx
Embedding	- Google Gemini Embeddings, Sentence Transformers
Vector DB	- FAISS, Chroma
LLM	- Gemini Pro (via google.generativeai)
Backend -	FastAPI
Frontend -	Streamlit (currently) or optionally React
.env management -	python-dotenv
Deployment -	Localhost / GCP (optional later)
