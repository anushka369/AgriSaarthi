# app/embeddings.py
from langchain.embeddings import OpenAIEmbeddings
import os

def get_embeddings():
    api_key = os.getenv("OPENAI_API_KEY")
    # LangChain OpenAIEmbeddings uses OPENAI_API_KEY env var
    return OpenAIEmbeddings()