#Medium article: https://medium.com/gitconnected/lets-create-a-personal-chatbot-for-data-analysis-in-50-lines-of-python-code-2a8eb840d2aa

import pandas as pd

from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

import streamlit as st
from streamlit_chat import message
import os
#os.environ["OPENAI_API_KEY"] = '{your_api_key}'

if 'prompts' not in st.session_state:
    st.session_state.prompts = []
if 'responses' not in st.session_state:
    st.session_state.responses = []


def send_click():
    if st.session_state.user != '':
        prompt = st.session_state.user
        response = agent.run(prompt)

        st.session_state.prompts.append(prompt)
        st.session_state.responses.append(response)


st.title(':blue[Yeyu\'s Data Analysis Chatbot] ☕')
uploaded_file = st.file_uploader("Choose a csv file", type='csv')

if uploaded_file is not None:

    csv_data = uploaded_file.read()
    with open(uploaded_file.name, 'wb') as f: 
        f.write(csv_data)

    df = pd.read_csv(uploaded_file.name)
    st.dataframe(df.head(5))

    chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
    agent = create_pandas_dataframe_agent(chat, df, verbose=True)

    st.text_input("Ask Something:", key="user")
    st.button("Send", on_click=send_click)

    if st.session_state.prompts:
        for i in range(len(st.session_state.responses)-1, -1, -1):
            message(st.session_state.responses[i], key=str(i), seed='Milo')
            message(st.session_state.prompts[i], is_user=True, key=str(i) + '_user', seed=83)

