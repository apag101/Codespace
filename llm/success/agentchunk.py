#Medium Article: https://medium.com/towards-data-science/agentic-chunking-for-rags-091beccd94b1

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

chunks = {}

def create_new_chunk(chunk_id, proposition):
    summary_llm = llm.with_structured_output(ChunkMeta)

    summary_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Generate a new summary and a title based on the propositions.",
            ),
            (
                "user",
                "propositions:{propositions}",
            ),
        ]
    )

    summary_chain = summary_prompt_template | summary_llm

    chunk_meta = summary_chain.invoke(
        {
            "propositions": [proposition],
        }
    )

    chunks[chunk_id] = {
        "summary": chunk_meta.summary,
        "title": chunk_meta.title,
        "propositions": [proposition],
    }

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

chunks = {}

def create_new_chunk(chunk_id, proposition):
    summary_llm = llm.with_structured_output(ChunkMeta)

    summary_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Generate a new summary and a title based on the propositions.",
            ),
            (
                "user",
                "propositions:{propositions}",
            ),
        ]
    )

    summary_chain = summary_prompt_template | summary_llm

    chunk_meta = summary_chain.invoke(
        {
            "propositions": [proposition],
        }
    )

    chunks[chunk_id] = {
        "summary": chunk_meta.summary,
        "title": chunk_meta.title,
        "propositions": [proposition],
    }

from pydantic import BaseModel, Field

class ChunkMeta(BaseModel):
    title: str = Field(description="The title of the chunk.")
    summary: str = Field(description="The summary of the chunk.")

def add_proposition(chunk_id, proposition):
    summary_llm = llm.with_structured_output(ChunkMeta)

    summary_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "If the current_summary and title is still valid for the propositions return them."
                "If not generate a new summary and a title based on the propositions.",
            ),
            (
                "user",
                "current_summary:{current_summary}\n\ncurrent_title:{current_title}\n\npropositions:{propositions}",
            ),
        ]
    )

    summary_chain = summary_prompt_template | summary_llm

    chunk = chunks[chunk_id]

    current_summary = chunk["summary"]
    current_title = chunk["title"]
    current_propositions = chunk["propositions"]

    all_propositions = current_propositions + [proposition]

    chunk_meta = summary_chain.invoke(
        {
            "current_summary": current_summary,
            "current_title": current_title,
            "propositions": all_propositions,
        }
    )

    chunk["summary"] = chunk_meta.summary
    chunk["title"] = chunk_meta.title
    chunk["propositions"] = all_propositions

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

chunks = {}

def create_new_chunk(chunk_id, proposition):
    summary_llm = llm.with_structured_output(ChunkMeta)

    summary_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Generate a new summary and a title based on the propositions.",
            ),
            (
                "user",
                "propositions:{propositions}",
            ),
        ]
    )

    summary_chain = summary_prompt_template | summary_llm

    chunk_meta = summary_chain.invoke(
        {
            "propositions": [proposition],
        }
    )

    chunks[chunk_id] = {
        "summary": chunk_meta.summary,
        "title": chunk_meta.title,
        "propositions": [proposition],
    }

from pydantic import BaseModel, Field

class ChunkMeta(BaseModel):
    title: str = Field(description="The title of the chunk.")
    summary: str = Field(description="The summary of the chunk.")

def add_proposition(chunk_id, proposition):
    summary_llm = llm.with_structured_output(ChunkMeta)

    summary_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "If the current_summary and title is still valid for the propositions return them."
                "If not generate a new summary and a title based on the propositions.",
            ),
            (
                "user",
                "current_summary:{current_summary}\n\ncurrent_title:{current_title}\n\npropositions:{propositions}",
            ),
        ]
    )

    summary_chain = summary_prompt_template | summary_llm

    chunk = chunks[chunk_id]

    current_summary = chunk["summary"]
    current_title = chunk["title"]
    current_propositions = chunk["propositions"]

    all_propositions = current_propositions + [proposition]

    chunk_meta = summary_chain.invoke(
        {
            "current_summary": current_summary,
            "current_title": current_title,
            "propositions": all_propositions,
        }
    )

    chunk["summary"] = chunk_meta.summary
    chunk["title"] = chunk_meta.title
    chunk["propositions"] = all_propositions


def find_chunk_and_push_proposition(proposition):

    class ChunkID(BaseModel):
        chunk_id: int = Field(description="The chunk id.")

    allocation_llm = llm.with_structured_output(ChunkID)

    allocation_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You have the chunk ids and the summaries"
                "Find the chunk that best matches the proposition."
                "If no chunk matches, return a new chunk id."
                "Return only the chunk id.",
            ),
            (
                "user",
                "proposition:{proposition}" "chunks_summaries:{chunks_summaries}",
            ),
        ]
    )

    allocation_chain = allocation_prompt | allocation_llm

    chunks_summaries = {
        chunk_id: chunk["summary"] for chunk_id, chunk in chunks.items()
    }

    best_chunk_id = allocation_chain.invoke(
        {"proposition": proposition, "chunks_summaries": chunks_summaries}
    ).chunk_id

    if best_chunk_id not in chunks:
        best_chunk_id = create_new_chunk(best_chunk_id, proposition)
        return

    add_proposition(best_chunk_id, proposition)