from fastapi import APIRouter, HTTPException
from app.model.model import ChatRequest, ChatResponse
from app.service.service import get_llm_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    try:
        response_text = get_llm_response(request.messages)
        
        return ChatResponse(response=response_text)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))