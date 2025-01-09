
from apikey import apikey, serpapi, langSmithKey
import os
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = apikey
os.environ["SERPAPI_API_KEY"] = serpapi
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = langSmithKey
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "AI Financial Analyst"

llm = OpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools,
                         llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)

while True:
    company = input("Enter the name of the company or stock you want to analyze or 'quit'.\n")

    if company == 'quit':
        break
    else:
        agent.run(f"Analyze {company} stock and craft investment recommendations in a memo format.")
        break