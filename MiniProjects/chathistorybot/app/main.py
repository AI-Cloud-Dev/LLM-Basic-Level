from fastapi import FastAPI
from app.routes import chat_route

app= FastAPI(title="Mini LLM Chatbot with history")

app.include_router(chat_route.router)