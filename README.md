# 🤖 SmartAssist – AI Customer Support Assistant

SmartAssist is an AI-powered customer support application built using **FastAPI, React, LangGraph, RAG, ChromaDB, and Groq LLM**. It provides intelligent customer assistance through a multi-agent workflow, retrieves information from a knowledge base, and escalates complex queries when required.

### 🌐 Live Demo

**Frontend:** https://customer-support-ai-agent-nu.vercel.app

**Backend API:** https://customer-support-ai-agent-oz0j.onrender.com

### ✨ Features

- Multi-Agent workflow using LangGraph
- Retrieval-Augmented Generation (RAG) with ChromaDB
- Groq LLM fallback for general assistance
- Automatic clarification for vague queries
- Human escalation for policy and account-related requests
- Modern React + Vite frontend with FastAPI backend

### 🔄 Workflow

1. **Conversation Agent** greets the user and starts the conversation.
2. **Inquiry Agent** identifies the user's intent and requests additional information if the query is unclear.
3. **Knowledge Agent** retrieves relevant information from the knowledge base using RAG and generates an appropriate response.
4. If the knowledge base cannot answer, the request is passed to the **Groq LLM Fallback**, which either provides general guidance or determines whether human intervention is required.
5. Queries involving company policies, account-specific information, or sensitive actions are forwarded to the **Resolution Agent** for human support escalation.
6. Finally, the **Support Agent** confirms whether the user's issue has been resolved and offers additional assistance through quick action options.

### 🛠️ Tech Stack

**Frontend:** React, Vite, Axios, CSS

**Backend:** FastAPI, LangGraph, LangChain, ChromaDB, Hugging Face Embeddings, Groq LLM, Python
