#Medium Atricle: https://medium.com/towards-data-science/a-gentle-intro-to-chaining-llms-agents-and-utils-via-langchain-16cd385fca81

from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableSequence


prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)


# OUTPUT
# What is a good name for a company that makes podcast player?
#=======================
# llm = OpenAI(
#           model_name="gpt-4o-mini", # default model
#           temperature=0.9) #temperature dictates how whacky the output should be
# llmchain = LLMChain(llm=llm, prompt=prompt)
# llmchain.run("podcast player")
# ===================
# chatopenai = ChatOpenAI(
#                 model_name="gpt-4")
# llmchain_chat = chain = prompt | chatopenai
# llmchain_chat.invoke("podcast player")

# print(prompt.format(product="podcast player"))
#========================

import langchain_community.agents
from langchain_community.agents import AgentType
from langchain_community.agents import load_tools

llm = OpenAI(temperature=0)
tools = load_tools(["pal-math"], llm=llm)

agent = initialize_agent(tools,
                         llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)