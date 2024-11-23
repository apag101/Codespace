'''
Medium article 
A step-by-step guide to building a chatbot based on your own documents with GPT
https://medium.com/towards-data-science/4-ways-of-question-answering-in-langchain-188c6707cc5a


'''
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader

import openai



# Load the PDF document
loader = PyPDFLoader("230317564.pdf")
documents = loader.load()

# split the documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
# select which embeddings we want to use
embeddings = OpenAIEmbeddings()
# create the vectorestore to use as the index
db = Chroma.from_documents(texts, embeddings)
# expose this index in a retriever interface
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":2})
# create a chain to answer questions 
qa = RetrievalQA.from_chain_type(
    llm = OpenAI(api_key=openai.api_key), chain_type="stuff", retriever=retriever, return_source_documents=True)
query = "What is the summary of the document?"
result = qa({"query": query})
print(result)