# Define Pyfantic shemas model for request and response

from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    reply: str