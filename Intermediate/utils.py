import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

def get_groq_llm():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=api_key
    )
    return llm