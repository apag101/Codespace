#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 20:40:54 2023

@author: apag1
"""

import os
import requests



from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredURLLoader

import requests
url2 = "https://github.com/fabiomatricardi/cdQna/raw/main/KS-all-info_rev1.txt"
res = requests.get(url2)
with open("KS-all-info_rev1.txt", "w") as f:
  f.write(res.text)

from langchain.document_loaders import TextLoader
loader= TextLoader('./KS-all-info_rev1.txt')
documents = loader.load()
import textwrap

def wrap_text_preserve_newlines(text, width=110):
  lines = text.split('\n')
  wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
  wrapped_text = '\n'.join(wrapped_lines)
  return wrapped_text

from langchain import text_splitter
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
docs = text_splitter.split_documents(documents)

from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()

from langchain.vectorstores import FAISS
db = FAISS.from_documents(docs, embeddings)

#query = "What is Hierarchy 4.0?"
#docs = db.similarity_search(query)

len(docs)
#print(wrap_text_preserve_newlines(str(docs[0].page_content)))

from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

llm = HuggingFaceHub(repo_id = "declare-lab/flan-alpaca-large", model_kwargs={"temperature":0, "max_length":512})
chain = load_qa_chain(llm, chain_type="stuff")


query="What is the summary"
docs = db.similarity_search(query)
chain.run(input_documents=docs, question=query)

#query = input("What is your question: ")