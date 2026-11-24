# AutoRAG Assistant — Agentic RAG with Phidata, Groq & PgVector

An autonomous Retrieval-Augmented Generation (RAG) assistant built with **Phidata**, **PostgreSQL (`pgvector`)**, **Groq**, and **Ollama**.
The assistant ingests PDF documents into a persistent vector database, retrieves relevant context for user queries, falls back to external search when information is not found in the knowledge base,
and maintains multi-turn conversation history in PostgreSQL.

## Key Features

- **Autonomous Knowledge Retrieval:** Automatically searches the `pgvector` knowledge base before answering user questions.
- **Hybrid Cloud + Local Inference:** Combines ultra-fast **Groq** LLM inference (`llama-3.3-70b-versatile`) with unlimited local **Ollama** embeddings (`nomic-embed-text`, 768 dimensions).
- **Persistent Vector & Chat Storage:** Stores document embeddings (`PgVector2`) and conversation history (`PgAssistantStorage`) inside a Dockerized PostgreSQL database.
- **External Tool Fallback:** Uses Wikipedia/web search tools when answers are outside the uploaded PDF scope.

## Tech Stack

- **Agent Framework:** Phidata (`phi.assistant`)
- **LLM Provider:** Groq (`GPT OSS 20B`)
- **Embedding Model:** Ollama (`nomic-embed-text`)
- **Vector Database & Memory:** PostgreSQL 16 + `pgvector` (`phidata/pgvector:16`)
- **Document Processing:** `pypdf` via Phidata `PDFReader`

## Project Structure

```text
AutoRagPhiData/
├── app.py              # Main AutoRAG assistant, PDF ingestion, and query pipeline
├── docker.txt          # Docker command to spin up PostgreSQL with pgvector
├── requirements.txt    # Python dependencies
├── sample.pdf          # Sample PDF document for knowledge base testing
└── README.md           # Project documentation
