# Medium article: https://medium.com/@fareedkhandev/scikit-llm-sklearn-meets-large-language-models-11fc6f30e530

# importing SKLLMConfig to configure OpenAI API (key and Name)
from skllm.config import SKLLMConfig

# Set your OpenAI API key
SKLLMConfig.set_openai_key("<your openai key>")

# Set your OpenAI organization (optional)
SKLLMConfig.set_openai_org("<your openai org>")

# Importing the GPTSummarizer class from the skllm.preprocessing module
from skllm.text2text import GPTSummarizer

# Importing the get_summarization_dataset function
from skllm.datasets import get_summarization_dataset

# Calling the get_summarization_dataset function
X = get_summarization_dataset()

# Creating an instance of the GPTSummarizer
s = GPTSummarizer(model='gpt-3.5-turbo', max_words=15)

# Applying the fit_transform method of the GPTSummarizer instance to the input data 'X'.
# It fits the model to the data and generates the summaries, which are assigned to the variable 'summaries'
summaries = s.fit_transform(X)