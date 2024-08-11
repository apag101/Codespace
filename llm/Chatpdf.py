# On jupyter notebook you can uncomment the below lines to install the packages
# !pip install langchain
# !pip install pypdf
# !pip install chromadb
# https://medium.com/geekculture/automating-pdf-interaction-with-langchain-and-chatgpt-e723337f26a6


from langchain_community.document_loaders import PyPDFLoader # for loading the pdf
from langchain_openai import OpenAIEmbeddings# for creating embeddings
from langchain_community.vectorstores import Chroma # for the vectorization part
from langchain.chains import ChatVectorDBChain # for chatting with the pdf
from langchain_community.llms import OpenAI # the LLM model we'll use (CHatGPT)

import os

pdf_path = "../../Documents/paper.pdf"
loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()
print(pages[0].page_content)

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(pages, embedding=embeddings,
                                     persist_directory=".")
vectordb.persist()

pdf_qa = ChatVectorDBChain.from_llm(OpenAI(temperature=0.9, model_name="gpt-3.5-turbo"),
                                    vectordb, return_source_documents=True)

query = "What is the VideoTaskformer?"
result = pdf_qa({"question": query, "chat_history": ""})
print("Answer:")
print(result["answer"])