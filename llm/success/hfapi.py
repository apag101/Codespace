# Medium Article: https://medium.com/artificial-corner/hugging-face-api-token-the-secret-to-building-your-own-ai-app-for-free-9a134dd213db

# Python app for HuggingFace Inferences
# Only API Access token from Huggingface.co
# libraries for AI inferences
from huggingface_hub import InferenceClient
from langchain_community.llms import HuggingFaceHub
import requests
# Internal usage
import os
import datetime

yourHFtoken = 'apikey'  #paste your token here

def imageToText(url):
    from huggingface_hub import InferenceClient
    client = InferenceClient(token=yourHFtoken)
    model_Image2Text = "Salesforce/blip-image-captioning-base"
    # tasks from huggingface.co/tasks
    text = client.image_to_text(url,model=model_Image2Text)
    print(text)
    return text

basetext = imageToText("./photo.jpeg")