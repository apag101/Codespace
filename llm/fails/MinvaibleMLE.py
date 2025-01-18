# Medium Article: https://medium.com/towards-data-science/minimum-viable-mle-306877dd6030

# Filename: main.py
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
classifier = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

class SentimentOutput(BaseModel):
    text: str
    sentiment: str
    score: float

@app.post("/predict", response_model=SentimentOutput)
async def predict_sentiment(input_data: TextInput):
    result = classifier(input_data.text)[0]
    return SentimentOutput(
        text=input_data.text,
        sentiment=result["label"],
        score=result["score"]
    )