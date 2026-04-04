from fastapi import FastAPI
from app.routes import chat

app = FastAPI(title = "Mini Chatbot")

app.include_router(chat.router)

