from dotenv import load_dotenv
load_dotenv()#load all the environment variable
import google.generativeai as genai
from retriever import retrieve_docs
import os

# # Load Gemini API Key

# api_key = os.getenv("GOOGLE_API_KEY")

# if not api_key:
#     raise Exception("GOOGLE_API_KEY not set!")

genai.configure(api_key="AIzaSyAJDOsHJoAYSQRyFFcT9eEYQmv8Vn7zKWY")

def generate_answer(user_query):
    print("Generating answer")
    retrieved_docs = retrieve_docs(user_query)
    if not retrieved_docs:
        return "I don't know."
    for i in retrieved_docs:
        print(i)
    context = "\n\n".join(retrieved_docs)
    print(context)
    prompt = f"""
    You are a helpful support assistant.

    You have access to internal document information (loaded from company documents).

    Rules:
    - Answer the user's question based ONLY on the provided similar context from documents.
    - Always answer briefly and accurately.

    Context from Documents:
    {context}

    User's Question:
    {user_query}

    Answer:
    """
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text
