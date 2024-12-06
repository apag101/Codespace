# Proprietary LLM from e.g. OpenAI
# pip install openai
from langchain_openai import OpenAI
llm = OpenAI(model_name="text-embedding-ada-002")

# Alternatively, open-source LLM hosted on Hugging Face
# pip install huggingface_hub
#from langchain_community.llms import huggingface_hub
#from langchain_huggingface import HuggingFaceEndpoint
#llm = huggingface_hub.HuggingFaceHub(repo_id = "google/flan-t5-xl")

# The LLM takes a prompt as an input and outputs a completion
prompt = "Alice has a parrot. What animal is Alice's pet?"
completion = llm(prompt)

# Proprietary text embedding model from e.g. OpenAI
# pip install tiktoken
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# Alternatively, open-source text embedding model hosted on Hugging Face
# pip install sentence_transformers
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

# The embeddings model takes a text as an input and outputs a list of floats
text = "Alice has a parrot. What animal is Alice's pet?"
text_embedding = embeddings.embed_query(text)

