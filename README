# 🤖 AI Support Agent

An AI-powered customer support agent that combines Large Language Models (LLM), Retrieval-Augmented Generation (RAG), and MCP tools to provide intelligent customer support.

---
                User
                  │
                  ▼
         React Frontend
                  │
                  ▼
          FastAPI Backend
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
     AI Planner          Session
        │
   Decide Tool/RAG
        │
 ┌──────┴─────────┐
 │                │
 ▼                ▼
Tool Path      RAG Path
 │                │
 ▼                ▼
Argument      Qdrant Search
Collection         │
 │                 ▼
 ▼            Retrieved Docs
MCP Tools          │
 │                 │
 └──────┬──────────┘
        ▼
Response Generator
        │
        ▼
     Frontend
        │
        ▼
       User


## ✨ Features

- AI Planner
- RAG Knowledge Base
- MCP Tool Calling
- Dynamic Tool Selection
- Multi-turn Conversations
- Argument Collection
- Session Management
- Natural Language Responses

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- Ollama
- MCP
- Qdrant
- SQLite

### Frontend
- React
- Vite
- Axios

---

# 🏗️ System Architecture

<p align="center">
<img src="docs/architecture.png" width="900">
</p>

---

## 🔄 Request Flow

1. User sends a message.
2. Planner decides:
   - Tool
   - RAG
3. If Tool:
   - Extract arguments
   - Validate missing arguments
   - Execute MCP Tool
4. If RAG:
   - Search Qdrant
5. Response Generator creates a natural answer.
6. Return response to the user.

---

## 🔧 Available Tools

| Tool | Description |
|------|-------------|
| Calculator | Mathematical calculations |
| Support Ticket | Create support tickets |
| Order Status | Track customer orders |

---

## 📚 Knowledge Base

The RAG system indexes PDF documents including:

- API Documentation
- FAQ
- Company Policies
- Refund Policy
- Technical Support Guide

using Qdrant Vector Database.

---

## 📂 Project Structure

backend/
├── services/
├── routes/
├── models/
├── knowledge_base/
├── mcp/
└── app.py

frontend/
├── src/
└── package.json

---

## 🚀 Run Backend

```bash
cd backend

python -m venv venv

pip install -r requirements.txt

python index_documents.py

uvicorn app:app --reload
```

---

## 🚀 Run Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 📌 Future Improvements

- Authentication
- Docker Support
- More MCP Tools
- Streaming Responses
- Conversation History

---

## 📄 License

MIT
