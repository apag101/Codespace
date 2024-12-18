# Medium Atricle: https://medium.com/towards-artificial-intelligence/understanding-langchain_community-%EF%B8%8F-part-2-ed6c487dc295

#    IMPORTS
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from PyPDF2 import PdfReader
from langchain_community.llms import OpenAI
from langchain_openai import ChatOpenAI

from langchain_community.vectorstores import Chroma, VectorStore
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain

from langchain_community.document_loaders import TextLoader
# from langchain_community import ConversationalRetrievalChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import LLMChain
# from langchain_community import retrievers
import langchain_community
from langchain.chains.conversation.memory import ConversationBufferMemory
import os

llm = ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo")

from langchain_community.document_loaders import DirectoryLoader
pdf_loader = PdfReader(r'./data/230213971v1.pdf')

#Preprocessing of file

raw_text = ''
for i, page in enumerate(pdf_loader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

# print(raw_text[:100])


text_splitter = CharacterTextSplitter(        
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

embeddings = OpenAIEmbeddings()
# vectorstore = Chroma.from_documents(documents, embeddings)
vectorstore = FAISS.from_texts(texts, embeddings)

prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say GTGTGTGTGTGTGTGTGTG, don't try to make up an answer.
{context}
Question: {question}
Helpful Answer:"""
QA_PROMPT = PromptTemplate(
    template=prompt_template, input_variables=['context',"question"]
)

qa = ConversationalRetrievalChain.from_llm(ChatOpenAI(temperature=0.8), vectorstore.as_retriever(),qa_prompt=QA_PROMPT)

# Front end web app
# import gradio as gr
# with gr.Blocks() as demo:
#     gr.Markdown("## Grounding DINO ChatBot")
#     chatbot = gr.Chatbot()
#     msg = gr.Textbox()
#     clear = gr.Button("Clear")
#     chat_history = []

# def user(user_message, history):
#     print("Type of use msg:",type(user_message))
#      # Get response from QA chain
#     response = qa({"question": user_message, "chat_history": history})
#     # Append user message and response to chat history
#     history.append((user_message, response["answer"]))
#     print(history)
#     return gr.update(value=""), history
#     msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False)
#     clear.click(lambda: None, None, chatbot, queue=False)
#     ############################################

# if __name__ == "__main__":
#     demo.launch(debug=True)
