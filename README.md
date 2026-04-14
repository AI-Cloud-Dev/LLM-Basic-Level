# 🤖 LLM App Development

> End-to-end examples of building LLM-powered applications using LangChain, OpenAI, and FastAPI — from prompt engineering to deployable AI agents.

---

## 📌 Overview

This repository documents my hands-on journey building real-world applications with Large Language Models. It covers foundational concepts through to production-ready patterns including RAG pipelines, tool-using agents, and API-served LLM endpoints.

---

## ✨ Features

- 🔗 **LangChain Chains & Agents** — ReAct agents, tool use, memory patterns
- 📚 **RAG Pipeline** — Document ingestion, vector storage, retrieval-augmented generation
- ⚡ **FastAPI Integration** — LLM logic served as a REST API
- 🧪 **Prompt Engineering** — Few-shot, chain-of-thought, and structured output prompting
- ☁️ **AWS-ready** — Notes on deploying to AWS Lambda / EC2

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| LLM Framework | LangChain |
| LLM Providers | OpenAI GPT-4, Anthropic Claude |
| Vector Store | FAISS / ChromaDB |
| API Layer | FastAPI |
| Cloud | AWS (S3, Lambda) |
| Containerization | Docker |

---

## 🚀 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/AI-Cloud-Dev/llm-app-development.git
cd llm-app-development
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
# Edit .env and add your API keys
```

---

## 📁 Project Structure

```
llm-app-development/
├── README.md
├── requirements.txt
├── .env.example
├── notebooks/
│   ├── 01_prompt_engineering.ipynb
│   ├── 02_langchain_basics.ipynb
│   └── 03_rag_pipeline.ipynb
├── src/
│   ├── chains.py          # LangChain chain definitions
│   ├── agents.py          # Tool-using agent setup
│   ├── retriever.py       # RAG retrieval logic
│   └── api.py             # FastAPI app entry point
└── docs/
    └── architecture.md
```

---

## 💡 Usage

```python
from src.agents import create_agent

agent = create_agent(tools=["search", "calculator"])
response = agent.run("Summarize the latest trends in AI agents")
print(response)
```

---

## 📖 Key Learnings

- How to structure LangChain applications for maintainability
- RAG vs fine-tuning trade-offs for domain-specific Q&A
- Deploying LLM endpoints with FastAPI + Docker

---

## 🗺️ Roadmap

- [ ] Add streaming responses via FastAPI WebSockets
- [ ] Integrate LangSmith for observability
- [ ] Deploy to AWS Lambda with containerized FastAPI

---

## 📬 Contact

**Sreeja** | AI Engineer  
🔗 [GitHub](https://github.com/AI-Cloud-Dev) | [LinkedIn](#) | [Portfolio](#)
