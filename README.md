📚 RAG Study Assistant

A Retrieval-Augmented Generation (RAG) based study assistant designed to provide grounded, hallucination-resistant answers strictly based on lecture materials. The system ensures that responses are always traceable to source documents, including document name and page references, and supports isolated study projects for better organization.

✨ Features

- Retrieval-Augmented Generation (RAG)
Answers are generated strictly from provided lecture materials
Minimizes hallucinations by grounding responses in retrieved context

- Source Attribution
Every answer includes references to:
Document name
Page number

- Project-Based Isolation
Create multiple study projects
Each project has access only to its own uploaded documents
Ensures clean separation between courses or topics

- LLM-Powered Answering
Uses llama3.2 via Ollama for local inference
Context-aware responses based only on retrieved chunks

- Fast Semantic Search
Vector-based retrieval using embeddings
Efficient similarity search over lecture content

🧱 Tech Stack

- React Frontend
- FastAPI Backend
- Ollama (running llama3.2)
- Retrieval-Augmented Generation pipeline
- Vector Database: ChromaDB
- File Storage: MinIO (document and metadata storage)
- Docling (PDF parsing and structured extraction)

🏗️ Architecture Overview

User uploads lecture PDFs into a project ->
PDFs are parsed using Docling ->
Text is chunked and embedded ->
Embeddings are stored in ChromaDB (backed by MinIO) ->
User asks a question in the React frontend ->
FastAPI retrieves relevant chunks via similarity search ->
Context is passed to Llama 3.2 (Ollama) ->
Model generates an answer strictly grounded in retrieved context ->
Response includes document + page references ->
