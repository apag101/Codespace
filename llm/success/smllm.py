#Medium article: https://medium.com/towards-data-science/leveraging-smaller-llms-for-enhanced-retrieval-augmented-generation-rag-bc320e71223d

import pandas as pd
import fitz  # PyMuPDF
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import lancedb
from sentence_transformers import SentenceTransformer
import json
import pyarrow as pa
import numpy as np
import re

def create_prompt(question):
    """
    Create a prompt as per LLAMA 3.2 format.
    """
    system_message = "You are a helpful assistant for summarizing text and result in JSON format"
    prompt_template = f'''
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{system_message}<|eot_id|><|start_header_id|>user<|end_header_id|>
{question}<|eot_id|><|start_header_id|>assistant1231231222<|end_header_id|>
'''
    return prompt_template

def process_prompt(prompt, model, tokenizer, device, max_length=500):
    """
    Processes a prompt, generates a response, and extracts the assistant's reply.
    """
    prompt_encoded = tokenizer(prompt, truncation=True, padding=False, return_tensors="pt")
    model.eval()
    output = model.generate(
        input_ids=prompt_encoded.input_ids.to(device),
        max_new_tokens=max_length,
        attention_mask=prompt_encoded.attention_mask.to(device),
        temperature=0.1  # More deterministic
    )
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    parts = answer.split("assistant1231231222", 1)
    if len(parts) > 1:
            words_after_assistant = parts[1].strip()
            return words_after_assistant
    else:
        print("The assistant's response was not found.")
        return "NONE"
    
model_name_long = "meta-llama/Llama-3.2-1B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name_long)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
log.info(f"Loading the model {model_name_long}")
bf16 = False
fp16 = True
if torch.cuda.is_available():
    major, _ = torch.cuda.get_device_capability()
    if major >= 8:
        log.info("Your GPU supports bfloat16: accelerate training with bf16=True")
        bf16 = True
        fp16 = False
# Load the model
device_map = {"": 0}  # Load on GPU 0
torch_dtype = torch.bfloat16 if bf16 else torch.float16
model = AutoModelForCausalLM.from_pretrained(
    model_name_long,
    torch_dtype=torch_dtype,
    device_map=device_map,
)
log.info(f"Model loaded with torch_dtype={torch_dtype}")

