from fastapi import APIRouter
from app.model.chat_model import ChatRequest, ChatResponse
from app.llm_service.chat_service import get_llm_response
from app.llm_service.memory_store import add_message, get_history

router = APIRouter()

@router.get("/", response_model=ChatResponse)
def read_root():
    return {"answer": "Hello!, Ask me anything"}

@router.get("/history/{user_id}")
def history(user_id: str):
    """Return chat history for a user"""
    return get_history(user_id)

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        # Get user history
        history = get_history(request.user_id)

        # Add user message to memory
        add_message(request.user_id, "user", request.question)

        # Get LLM response
        answer = get_llm_response(history)

        # Save assistant response
        add_message(request.user_id, "assistant", answer)

        return {"answer": answer}

    except Exception as e:
        # Catch all errors
        return {"answer": f"[Error]: {e}"}