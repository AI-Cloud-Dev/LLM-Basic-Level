import logging
from fastapi import APIRouter, HTTPException
from app.service.services import get_ai_response
from app.model.models import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    logging.info(f"Received message: {request.message}")
    try:
        ai_reply = await get_ai_response(request.message)
        logging.info(f"Response generated Successfully")
        return ChatResponse(response=ai_reply)
    except Exception as e:
        logging.error(f"Error in /chat: {str(e)}")
        
        raise HTTPException(
            status_code=500,
            detail = f"Internal error: {str(e)}")