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
    
    context = "\n\n".join(retrieved_docs)
    prompt = f"""
You are a helpful support assistant. Answer based ONLY on the context provided.

Context:
{context}

Question: {user_query}

If the answer is not in the context, reply "I don't know."
"""
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text
