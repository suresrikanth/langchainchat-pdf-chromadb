import chardet
from langchain.document_loaders import PyMuPDFLoader,TextLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        print(result)
    return result['encoding']

encoding = detect_encoding("sample.txt")

with open("sample.txt", 'r', encoding=encoding) as f:
    text = f.read()

with open("sample_utf8.txt", 'w', encoding='utf-8') as f:
    f.write(text)

print(sample_utf8.txt)

loader = TextLoader("sample_utf8.txt")
print('sample')
documents = loader.load()