# AutoRAG Assistant (Phidata + Groq + Ollama + PgVector)

An Agentic Retrieval-Augmented Generation (RAG) assistant built with **Phidata** that answers user queries by searching 
a local PDF knowledge base stored in **PostgreSQL (`pgvector`)** and falling back to **Google Search** for real-time web information.

## Features
- **PDF Knowledge Base:** Parses and embeds PDF documents (`sample.pdf`) into PostgreSQL using `PgVector2`.
- **Hybrid AI Stack:** Uses **Groq** for fast LLM inference and tool calling, paired with local **Ollama (`nomic-embed-text`)** for 768-dimensional embeddings.
- **Persistent Chat Storage:** Stores conversation history in PostgreSQL via `PgAssistantStorage`.
- **Web Search Fallback:** Automatically queries `GoogleSearch` when the answer is not present in the uploaded document.
- **Output Export:** Logs queries and generated responses into `output.txt`.

## Project Structure
- `app.py` — Main AutoRAG assistant setup, PDF ingestion, query execution, and output export.
- `docker.txt` — Docker command to run the PostgreSQL + `pgvector` container on port `5532`.
- `requirements.txt` — Python dependencies required to run the project.
- `sample.pdf` — Sample document loaded into the vector knowledge base.

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/Ebadullah-Hashmi/AutoRagPhiData.git](https://github.com/Ebadullah-Hashmi/AutoRagPhiData.git)
   cd AutoRagPhiData
