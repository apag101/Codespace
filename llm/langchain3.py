'''
Medium article 
A step-by-step guide to building a chatbot based on your own documents with GPT
https://medium.com/towards-data-science/4-ways-of-question-answering-in-langchain-188c6707cc5a

'''
import os
import openai


# load document
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("230317564.pdf")
documents = loader.load()

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# Initialize the OpenAI LLM
llm = OpenAI(api_key=openai.api_key)

# Load the QA chain
chain = load_qa_chain(llm, chain_type="map_reduce")

# Run the chain with the input documents and question
result = chain.run(input_documents=documents, question="What is the summary of the document?")

print(result)
