import os
from langchain.document_loaders import PyMuPDFLoader,TextLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

os.environ['OPENAI_API_KEY'] = 'open ai key'

loader =TextLoader('sample.txt', 'r', encoding='utf-8', errors='ignore')
print("successfully")
documents = loader.load()
print(documents)


text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
texts = text_splitter.split_documents(documents)


persist_directory = "./storage"
embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=texts, 
                                 embedding=embeddings,
                                 persist_directory=persist_directory)
vectordb.persist()


retriever = vectordb.as_retriever()
llm = ChatOpenAI(model_name='gpt-3.5-turbo')
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

while True:
        user_input = input("Enter a query: ")
        if user_input == "exit":
            break

        query = f"###Prompt {user_input}"
        try:
            llm_response = qa(query)
            print(llm_response["result"])
        except Exception as err:
            print('Exception occurred. Please try again', str(err))