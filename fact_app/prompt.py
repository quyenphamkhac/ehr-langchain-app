from dotenv import load_dotenv
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
load_dotenv()

embeddings = OpenAIEmbeddings()

db = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma/factos"
)
