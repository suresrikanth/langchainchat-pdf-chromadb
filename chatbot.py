import os
from langchain.document_loaders import PyMuPDFLoader,TextLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

os.environ['OPENAI_API_KEY'] = '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'

loader=PyMuPDFLoader('machine_learning_tutorial.pdf')
documents = loader.load()
print(documents)

