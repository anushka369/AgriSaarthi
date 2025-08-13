# app/ingestion.py
import os
from langchain.document_loaders import DirectoryLoader, TextLoader, UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
from embeddings import get_embeddings

QDRANT_COLLECTION = "agrisaarthi_docs"

def ingest_documents(docs_dir="data/docs"):
    # load PDFs and text files
    loader = DirectoryLoader(docs_dir, glob="**/*", loader_cls=UnstructuredPDFLoader)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = splitter.split_documents(docs)

    embeddings = get_embeddings()
    qdrant_client = QdrantClient(url=os.getenv("QDRANT_URL", "http://localhost:6333"))
    qdrant = Qdrant.from_documents(documents=docs,
                                   embedding=embeddings,
                                   client=qdrant_client,
                                   collection_name=QDRANT_COLLECTION)
    print(f"Ingested {len(docs)} documents into Qdrant collection {QDRANT_COLLECTION}")
