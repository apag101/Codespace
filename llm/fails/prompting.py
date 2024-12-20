def get_api_result(prompt):
    request = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[{"role": "user", "content": prompt}]
    )
    
    result = request['choices'][0]['message']['content']

    print(result)

def extract(prompt):
    prompt_template = """You are a ChatGPT language model that can generate Python code. Please provide a natural language input text, and I will generate the corresponding Python code.\nInput: {}\nPython code:""".format(prompt)

    get_api_result(prompt_template)

from sklearn.datasets import fetch_openml
import pandas as pd
adult_income = fetch_openml(name='adult', version=2)
df = pd.DataFrame(adult_income.data, columns=adult_income.feature_names)
df['target'] = adult_income.target

import pandas as pd

df = pd.read_csv("adult_income_prediction.csv")
df.columns = ["age", "workclass", "fnlwgt", "education", "education-num",
              "marital-status", "occupation", "relationship", "race",
              "sex", "capital-gain", "capital-loss", "hours-per-week",
              "native-country", "target"]

