from langchain_community.llms import Ollama
llm = Ollama(model="llama3")
response = llm.invoke("create a quiz for Data Science on Microsoft Azure Exam")

# from llama_index.legacy.llms.ollama import Ollama
# llm = Ollama(model="llama3")
# response=llm.complete("Why is the sky blue?")
# print(response)

