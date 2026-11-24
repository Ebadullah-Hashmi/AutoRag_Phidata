from typing import List
import nest_asyncio
import logging
import os

from phi.assistant import Assistant
from phi.document import Document
from phi.document.reader.pdf import PDFReader
from phi.llm.groq import Groq
from phi.embedder.ollama import OllamaEmbedder
from phi.knowledge import AssistantKnowledge
from phi.tools.wikipedia import WikipediaTools  
from phi.vectordb.pgvector import PgVector2
from phi.storage.assistant.postgres import PgAssistantStorage


os.environ["GROQ_API_KEY"] = "Your GROQ_API_KEY"  # Replace with your actual GROQ API key

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
logger = logging.getLogger(__name__)

def setup_assistant(llm) -> Assistant:
    return Assistant(
        name="auto_rag_assistant",
        llm=llm,
        storage=PgAssistantStorage(table_name="auto_rag_assistant_ollama", db_url=db_url),
        knowledge_base=AssistantKnowledge(
            vector_db=PgVector2(
                db_url=db_url,
                collection="auto_rag_documents_ollama",
                embedder=OllamaEmbedder(model="nomic-embed-text", dimensions=768),
            ),
            num_documents=3,
        ),
        description="You are a helpful Assistant called 'AutoRAG' and your goal is to assist the user in the best way possible.",
        instructions=[
            "Given a user query, first ALWAYS search your knowledge base using the `search_knowledge_base` tool to see if you have relevant information.",
            "If you don't find relevant information in your knowledge base, use your search tool ONCE to find the answer.",
            "Carefully read the information you have gathered and provide a clear and concise answer to the user.",
            "Do not use phrases like 'based on my knowledge' or 'depending on the information'.",
        ],
        show_tool_calls=True,
        search_knowledge=True,
        read_chat_history=True,
        tools=[WikipediaTools()],
        function_call_limit=3,
        markdown=True,
        add_chat_history_to_messages=True,
        add_datetime_to_instructions=True,
        debug_mode=True,
    )

def add_document_to_kb(assistant: Assistant, file_path: str):
    reader = PDFReader()
    documents: List[Document] = reader.read(file_path)
    if documents:
        assistant.knowledge_base.load_documents(documents, upsert=True)
        logger.info(f"Document '{file_path}' added to the knowledge base.")

def query_assistant(assistant: Assistant, question: str):
    response = ""
    for delta in assistant.run(question):
        response += delta  # type: ignore
    return response

if __name__ == "__main__":
    nest_asyncio.apply()
    llm = Groq(model="Place Model Name", api_key=os.getenv("GROQ_API_KEY"))  
    assistant = setup_assistant(llm)

    add_document_to_kb(assistant, "sample.pdf")

    query = "who won asia cup 2023?"
    response = query_assistant(assistant, query)
    print("Query:", query)
    print("Response:", response)