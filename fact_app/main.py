from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
load_dotenv()

# LangChain provides classes to help load data from different types of files
# These are called 'loaders'
# -- facts.txt -> TextLoader
# -- report.pdf -> PyPDFLoader
# -- users.json -> JSONLoader
# -- blog.md -> UnstructuredMarkdownLoader

# An embedding is a list of numbers between 1 and  -1 that score how much a piece of text is talking about some particular quality
# Real embedding frequently have 700 - 1500 "dimessions"

embeddings = OpenAIEmbeddings()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)


loader = TextLoader("docs/facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)

db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="chroma/factos"
)
