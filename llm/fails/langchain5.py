# Medium article: https://medium.com/towards-data-science/implementing-a-sales-support-agent-with-langchain-63c4761193e7

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import GitLoader, DataFrameLoader
from langchain_community.document_loaders import YoutubeLoader
import pandas as pd
import requests
from bs4 import BeautifulSoup
from  langchain import embeddings
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI


# Knowledge base
kb_loader = GitLoader(
    clone_url="https://github.com/neo4j-documentation/knowledge-base",
    repo_path="./repos/kb/",
    branch="master",
    file_filter=lambda file_path: file_path.endswith(".adoc")
    and "articles" in file_path,
)
kb_data = kb_loader.load()
print(len(kb_data)) # 309

# Define text chunk strategy
splitter = CharacterTextSplitter(
  chunk_size=2000, 
  chunk_overlap=50,
  separator=" "
)
# GDS guides
gds_loader = GitLoader(
    clone_url="https://github.com/neo4j/graph-data-science",
    repo_path="./repos/gds/",
    branch="master",
    file_filter=lambda file_path: file_path.endswith(".adoc") 
    and "pages" in file_path,
)
gds_data = gds_loader.load()
# Split documents into chunks
gds_data_split = splitter.split_documents(gds_data)
print(len(gds_data_split)) #771

yt_loader = YoutubeLoader("1sRgsEKlUr0")
yt_data = yt_loader.load()
yt_data_split = splitter.split_documents(yt_data)
print(len(yt_data_split)) #10

article_url = "https://raw.githubusercontent.com/tomasonjo/blog-datasets/main/medium/neo4j_articles.csv"
medium = pd.read_csv(article_url, sep=";")
medium["source"] = medium["url"]
medium_loader = DataFrameLoader(
    medium[["text", "source"]], 
    page_content_column="text")
medium_data = medium_loader.load()
medium_data_split = splitter.split_documents(medium_data)
print(len(medium_data_split)) #4254

so_data = []
for i in range(1, 20):
    # Define the Stack Overflow API endpoint and parameters
    api_url = "https://api.stackexchange.com/2.3/questions"
    params = {
        "order": "desc",
        "sort": "creation",
        "filter": "!-MBrU_IzpJ5H-AG6Bbzy.X-BYQe(2v-.J",
        "tagged": "neo4j",
        "site": "stackoverflow",
        "pagesize": 100,
        "page": i,
    }
    # Send GET request to Stack Overflow API
    response = requests.get(api_url, params=params)
    data = response.json()
    # Retrieve the resolved questions
    resolved_questions = [
        question
        for question in data["items"]
        if question["is_answered"] and question.get("accepted_answer_id")
    ]

    # Print the resolved questions
    for question in resolved_questions:
        text = (
            "Title:",
            question["title"] + "\n" + "Question:",
            BeautifulSoup(question["body"]).get_text()
            + "\n"
            + BeautifulSoup(
                [x["body"] for x in question["answers"] if x["is_accepted"]][0]
            ).get_text()
            if any(x["is_accepted"] for x in question["answers"])
            else "",)
        source = question["link"]
        so_data.append(Document(page_content=str(text), metadata={"source": source}))
print(len(so_data)) #777

sales_data = medium_data_split + yt_data_split
print(len(sales_data)) #4264
sales_store = Chroma.from_documents(
    sales_data, embeddings, collection_name="sales"
)

support_data = kb_data + gds_data_split + so_data
support_store = Chroma.from_documents(
    support_data, embeddings, collection_name="support"
)

llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0,
    max_tokens=512,
)
