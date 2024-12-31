
# Medium article: https://towardsdatascience.com/build-your-personal-assistant-with-agents-and-tools-048637ac308e

from vertexai.generative_models import (
    GenerativeModel,
    GenerationConfig,
    Part
)

gemini_model = GenerativeModel(
    "gemini-1.5-flash",
    generation_config=GenerationConfig(temperature=0),
)
chat = gemini_model.start_chat()

response = chat.send_message("What is the current exchange rate for USD vs EUR ?")
answer = response.candidates[0].content.parts[0].text