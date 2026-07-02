# 🤖 AI Support Agent

An AI-powered customer support agent that combines Large Language Models (LLM), Retrieval-Augmented Generation (RAG), and Model Context Protocol (MCP) tools to provide intelligent customer support.

---

# ✨ Features

- 🤖 AI Planner for intelligent request routing
- 📚 Retrieval-Augmented Generation (RAG)
- 🔧 Dynamic MCP Tool Calling
- 💬 Multi-turn conversations
- 📝 Automatic argument extraction
- ✅ Missing argument validation
- 🗂 Session management
- 💡 Natural language response generation
- 📄 PDF knowledge base
- 🔍 Semantic search using Qdrant

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- Ollama
- MCP (Model Context Protocol)
- Qdrant
- SQLite

## Frontend

- React
- Vite
- Axios

---

# 🏗️ System Architecture

```text
                     User
                       │
                       ▼
               React Frontend
                       │
                       ▼
               FastAPI Backend
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        AI Planner         Session Manager
             │
      Decide Tool / RAG
             │
      ┌──────┴─────────┐
      ▼                ▼
   Tool Path       RAG Search
      │                │
      ▼                ▼
 Argument        Qdrant Vector DB
 Collection             │
      │                 ▼
      ▼          Knowledge Base
 Execute MCP Tool
      │
      ▼
Response Generator
      │
      ▼
     User
```

---

# 🔄 Request Flow

1. User sends a message.
2. The AI Planner determines whether the request requires:
   - A tool
   - The knowledge base (RAG)
3. If a tool is required:
   - Extract available arguments
   - Validate required arguments
   - Ask for any missing information
   - Execute the appropriate MCP tool
4. If no tool is required:
   - Search the Qdrant vector database
   - Retrieve the most relevant knowledge
5. Generate a natural language response.
6. Return the final response to the user.

---

# 🔧 Available MCP Tools

| Tool | Description |
|------|-------------|
| Calculator | Perform mathematical calculations |
| Support Ticket | Create customer support tickets |
| Order Status | Retrieve customer order status |

---

# 📚 Knowledge Base

The RAG system indexes company documents stored as PDF files, including:

- API Documentation
- Company Policies
- Frequently Asked Questions (FAQ)
- Orders & Shipping Guide
- Refund Policy
- Subscription & Pricing
- Technical Support Guide

All documents are embedded and stored inside **Qdrant Vector Database** for semantic retrieval.

---

# 📂 Project Structure

```text
AI-Support-Agent
│
├── backend
│   ├── app.py
│   ├── routes
│   ├── models
│   ├── services
│   │   ├── agent
│   │   ├── rag
│   │   ├── llm
│   │   └── mcp
│   ├── knowledge_base
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
└── README.md
```

---

# 🚀 Running the Project

## Backend

```bash
cd backend

python -m venv venv

pip install -r requirements.txt

python index_documents.py

uvicorn app:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 💡 Example Requests

### Calculator

```
Calculate 25 + 18
```

### Support Ticket

```
Create a support ticket because I can't log in.
```

### Order Tracking

```
Where is my order 10025?
```

### Knowledge Base (RAG)

```
What is the refund policy?
```

---

# 🚀 Future Improvements

- User authentication
- Docker deployment
- Streaming responses
- More MCP tools
- Conversation history
- Admin dashboard
- Tool auto-discovery
- Multi-agent architecture

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Amjad Zhour**

Artificial Intelligence Graduate

GitHub:
https://github.com/amjadfsfsf
