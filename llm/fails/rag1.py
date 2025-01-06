import chromadb
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

config_list = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": "<Enter OpenAI API key>"
    }
]

assistant = RetrieveAssistantAgent(
    name="assistant", 
    system_message="You are a helpful assistant.",
    llm_config={
        "request_timeout": 600,
        "seed": 42,
        "config_list": config_list,
    },
)

# The text file of the synopsis of One Piece that was saved earlier.
corpus_file = "Artificial_intelligence.txt"

ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    retrieve_config={
        "task": "qa",
        "docs_path": corpus_file,
        "chunk_token_size": 2000,
        "model": "gpt-3.5-turbo",
        "client": chromadb.PersistentClient(path="./db"),
        "collection_name": "natural-questions",
        "chunk_mode": "one_line",
        "embedding_model": "all-MiniLM-L6-v2",
    },
)

ragproxyagent.initiate_chat(
    assistant,
    problem="What is Artificial_intelligence ", n_results=30
)