from dotenv import load_dotenv
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.callbacks.tracers import ConsoleCallbackHandler

load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()
db = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma/factos"
)
retriever = db.as_retriever()

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)

result = chain.invoke({
    "query":  "What is an interesting fact about the English language?"
}, config={'callbacks': [ConsoleCallbackHandler()]})

print(result)
