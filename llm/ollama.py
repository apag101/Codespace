from langchain_community.llms import Ollama
llm = Ollama(model="llama3")
response = llm.invoke("Why is the sky blue?")
print(response)

# from llama_index.legacy.llms.ollama import Ollama
# llm = Ollama(model="llama3")
# response=llm.complete("Why is the sky blue?")
# print(response)

