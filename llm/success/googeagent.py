# Medium article: https://medium.com/@incle/how-to-create-your-own-llm-agent-from-scratch-a-step-by-step-guide-14b763e5b3b8

from googleapiclient.discovery import build
from py_expression_eval import Parser
from openai import OpenAI
import os, re, time

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

#Google search engine
def search(search_term):
    search_result = ""
    service = build("customsearch", "v1", developerKey=os.environ.get("GOOGLE_API_KEY"))
    res = service.cse().list(q=search_term, cx=os.environ.get("GOOGLE_CSE_ID"), num = 10).execute()
    for result in res['items']:
        search_result = search_result + result['snippet']
    return search_result

#Calculator
parser = Parser()
def calculator(str):
    return parser.parse(str).evaluate({})

System_prompt = """
Answer the following questions and obey the following commands as best you can.

You have access to the following tools:

Search: Search: useful for when you need to answer questions about current events. You should ask targeted questions.
Calculator: Useful for when you need to answer questions about math. Use python code, eg: 2 + 2
Response To Human: When you need to respond to the human you are talking to.

You will receive a message from the human, then you should start a loop and do one of two things

Option 1: You use a tool to answer the question.
For this, you should use the following format:
Thought: you should always think about what to do
Action: the action to take, should be one of [Search, Calculator]
Action Input: "the input to the action, to be sent to the tool"

After this, the human will respond with an observation, and you will continue.

Option 2: You respond to the human.
For this, you should use the following format:
Action: Response To Human
Action Input: "your response to the human, summarizing what you did and what you learned"

Begin!
"""

def Stream_agent(prompt):
    messages = [
        { "role": "system", "content": System_prompt },
        { "role": "user", "content": prompt },
    ]
    def extract_action_and_input(text):
          action_pattern = r"Action: (.+?)\n"
          input_pattern = r"Action Input: \"(.+?)\""
          action = re.findall(action_pattern, text)
          action_input = re.findall(input_pattern, text)
          return action, action_input
    while True:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0,
            top_p=1,)
        response_text = response.choices[0].message.content
        print(response_text)
        #To prevent the Rate Limit error for free-tier users, we need to decrease the number of requests/minute.
        time.sleep(20)
        action, action_input = extract_action_and_input(response_text)
        if action[-1] == "Search":
            tool = search
        elif action[-1] == "Calculator":
            tool = calculator
        elif action[-1] == "Response To Human":
            print(f"Response: {action_input[-1]}")
            break
        observation = tool(action_input[-1])
        print("Observation: ", observation)
        messages.extend([
            { "role": "system", "content": response_text },
            { "role": "user", "content": f"Observation: {observation}" },
            ])
        
Stream_agent("who is new openai board members")