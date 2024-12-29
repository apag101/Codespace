#Medium Article :https://medium.com/@ashukumar27/dolly2-and-langchain-a-game-changer-for-text-data-analytics-7518d48d0ad7

# import torch
# from transformers import pipeline

# generate_text = pipeline(model="databricks/dolly-v2-12b", 
#                          torch_dtype=torch.bfloat16, 
#                          trust_remote_code=True, 
#                          device_map="auto",
#                          offload_folder="./offload", 
#                          force_reload=True
#                          )
# from transformers import  GenerationConfig, pipeline
# import torch

# generate_text('Is Dhoni the best batsman of IPL?')

from langchain_community import llms
from langchain_openai import OpenAI
llm=OpenAI(model_name = 'gpt-4o',openai_api_key="api-key")
llm("explain Indian premier league in 200 words")