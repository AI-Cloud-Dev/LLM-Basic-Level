# Chat routes

from fastapi import APIRouter
from app.model.chat_model import ChatRequest, ChatResponse
from app.services.llm_service import get_ollama_response

router = APIRouter()

@router.get("/", response_model=ChatResponse)
def get_greeting():
    return {"reply": "Hello! I am your mini cahtbot. ask me anything."}

@router.post("/chat", response_model=ChatResponse)
def post_chat(request: ChatRequest):
    reply = get_ollama_response(request.question)
    return {"reply": reply}