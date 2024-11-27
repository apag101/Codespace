'''
Medium Article: How to Create a Doc Chatbot that Learns Everything for You in 15 Minutes
 https://medium.com/gitconnected/how-to-create-a-doc-chatbot-that-learns-everything-for-you-in-15-minutes-364fef481307
'''

import streamlit as st
import os
from llama_index.core.node_parser import SimpleFileNodeParser
from llama_index.core import Settings, SimpleDirectoryReader,  PromptHelper, ServiceContext, VectorStoreIndex, llms, download_loader
from langchain_community.llms import OpenAI    
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SentenceSplitter   


doc_path = '../data/'
index_file = 'index.json'

if 'response' not in st.session_state:
    st.session_state.response = ''

def send_click():
    st.session_state.response  = index.query(st.session_state.prompt)

index = None
st.title("AP Doc Chatbot")

sidebar_placeholder = st.sidebar.container()
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:

    doc_files = os.listdir(doc_path)
    for doc_file in doc_files:
        os.remove(doc_path + doc_file)

    bytes_data = uploaded_file.read()
    with open(f"{doc_path}{uploaded_file.name}", 'wb') as f: 
        f.write(bytes_data)

    SimpleDirectoryReader = download_loader("SimpleDirectoryReader")

    loader = SimpleDirectoryReader(doc_path, recursive=True, exclude_hidden=True)
    documents = loader.load_data()
    sidebar_placeholder.header('Current Processing Document:')
    sidebar_placeholder.subheader(uploaded_file.name)
    sidebar_placeholder.write(documents[0].get_text()[:10000]+'...')

    llm_predictor = OpenAI(temperature=0, model_name="text-davinci-003")

    max_input_size = 4096
    num_output = 256
    max_chunk_overlap = .5
    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

    service_context =  ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    Settings.llm = OpenAI(model="gpt-3.5-turbo")
    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
    Settings.num_output = 512
    Settings.context_window = 3900

    index = VectorStoreIndex.from_documents(
        documents, service_context=service_context
    )

    index.save_to_disk(index_file)

elif os.path.exists(index_file):
    index = VectorStoreIndex.load_from_disk(index_file)

    SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
    loader = SimpleDirectoryReader(doc_path, recursive=True, exclude_hidden=True)
    documents = loader.load_data()
    doc_filename = os.listdir(doc_path)[0]
    sidebar_placeholder.header('Current Processing Document:')
    sidebar_placeholder.subheader(doc_filename)
    sidebar_placeholder.write(documents[0].get_text()[:10000]+'...')

if index != None:
    st.text_input("Ask something: ", key='prompt')
    st.button("Send", on_click=send_click)
    if st.session_state.response:
        st.subheader("Response: ")
        st.success(st.session_state.response, icon= "🤖")