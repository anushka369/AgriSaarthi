# app/rag_agent.py
import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
from embeddings import get_embeddings

QDRANT_COLLECTION = "agrisaarthi_docs"

def build_agent():
    embeddings = get_embeddings()
    qdrant_client = QdrantClient(url=os.getenv("QDRANT_URL","http://localhost:6333"))
    vectorstore = Qdrant(client=qdrant_client, collection_name=QDRANT_COLLECTION, embeddings=embeddings)
    # Choose LLM: OpenAI GPT (or an alternative)
    llm = OpenAI(temperature=0.0)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever(search_kwargs={"k":4}))
    return qa

def answer_query(qa_chain, query, metadata=None):
    # returns {'result': ..., 'source_docs': [...]}
    res = qa_chain({"query": query})
    return res
