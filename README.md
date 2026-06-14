# 🚀 PyRAG - Retrieval Augmented Generation (RAG) Application

## Overview

PyRAG is a Retrieval-Augmented Generation (RAG) application built using:

* Angular (Frontend)
* FastAPI (Backend API)
* ChromaDB (Vector Database)
* OpenAI Embeddings
* OpenAI GPT Models
* LangChain

The application enables users to ask questions about their documents and receive context-aware answers generated from the knowledge base.

---

# Architecture

```text
┌─────────────────┐
│ Angular Client  │
└────────┬────────┘
         │ REST API
         ▼
┌─────────────────┐
│ FastAPI Backend │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  RAG Service    │
└────────┬────────┘
         │
 ┌───────┴─────────┐
 ▼                 ▼
Embedding      Vector Search
Model          (ChromaDB)
 │                 │
 └───────┬─────────┘
         ▼
     Retrieved
      Context
         │
         ▼
┌─────────────────┐
│ OpenAI GPT      │
└────────┬────────┘
         ▼
      Response
```

---

# Features

* Document ingestion
* Document chunking
* Embedding generation
* Vector similarity search
* Context-aware responses
* Source retrieval
* REST API architecture
* Dependency Injection
* Angular Chat UI
* Health monitoring endpoint

---

# Technology Stack

## Frontend

* Angular
* TypeScript
* RxJS
* Angular Forms
* HttpClient

## Backend

* Python 3.12+
* FastAPI
* Uvicorn
* Pydantic

## AI Components

* LangChain
* OpenAI Embeddings
* GPT Models

## Vector Database

* ChromaDB

---

# Project Structure

```text
pyrag/
│
├── app/
│   ├── api/
│   │   ├── rag_controller.py
│   │   └── health_controller.py
│   │
│   ├── services/
│   │   └── rag_service.py
│   │
│   ├── rag/
│   │   ├── ingest.py
│   │   └── rag_engine.py
│   │
│   ├── models/
│   │   ├── rag_request.py
│   │   └── rag_response.py
│   │
│   └── main.py
│
├── chroma_db/
│
├── data/
│   ├── sample.pdf
│   └── documents
│
├── .env
├── pyproject.toml
└── README.md
```

---

# Data Ingestion Pipeline

The ingestion pipeline performs:

1. Load document
2. Split document into chunks
3. Generate embeddings
4. Store embeddings in ChromaDB

```text
PDF/DOCX/TXT
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Embedding Model
      │
      ▼
ChromaDB
```

---

# API Endpoints

## Health Check

```http
GET /health
```

Response:

```json
{
  "status": "UP"
}
```

---

## Ask Question

```http
POST /api/v1/rag/ask
```

Request:

```json
{
  "question": "What is RAG?"
}
```

Response:

```json
{
  "answer": "RAG stands for Retrieval Augmented Generation..."
}
```

---

# Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-repository/pyrag.git

cd pyrag
```

---

## Install Dependencies

Using UV:

```bash
uv sync
```

Or manually:

```bash
uv add fastapi
uv add uvicorn
uv add langchain
uv add langchain-openai
uv add langchain-community
uv add chromadb
```

---

# Run Document Ingestion

```bash
uv run ingest.py
```

This will:

* Read documents
* Generate embeddings
* Store vectors in ChromaDB

---

# Run Backend API

```bash
uv run uvicorn main:app --reload
```

Application:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

# Angular Client Setup

Install dependencies:

```bash
npm install
```

Run:

```bash
ng serve
```

Application:

```text
http://localhost:4200
```

---

# Request Flow

```text
User Question
      │
      ▼
Angular UI
      │
      ▼
FastAPI API
      │
      ▼
RAG Service
      │
      ▼
Embedding Search
      │
      ▼
ChromaDB
      │
      ▼
Retrieve Top-K Chunks
      │
      ▼
OpenAI GPT
      │
      ▼
Generated Response
      │
      ▼
Angular UI
```

---

# Future Enhancements

* Streaming Responses
* Source Citations
* Conversation Memory
* Multi-document Search
* Role-based Authentication
* Docker Deployment
* Kubernetes Deployment
* Agentic RAG
* MCP Integration
* Hybrid Search (Keyword + Vector)

---

# Benefits of RAG

* Reduces hallucinations
* Uses enterprise knowledge
* Provides contextual answers
* Scalable architecture
* Improves answer accuracy
* Supports document-driven AI applications

---

# License

MIT License

---

# Author

PyRAG - Retrieval Augmented Generation Platform
