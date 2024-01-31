import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from app.chat.embeddings.openai import embeddings

pc = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(
    name=os.getenv("PINECONE_INDEX_NAME"),
    host=os.getenv("PINECONE_HOST")
)

vector_store = Pinecone(index=index, embedding=embeddings, text_key="text")
