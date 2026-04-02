from fastapi import FastAPI
from app.model.models import ChatRequest, ChatResponse
import logging
from app.routes.routes import router

logging.basicConfig(
    level = logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()

app.include_router(router)

# @app.get("/")
# def home():
#     return {"message": "AI ChatBot App is Running Successfully"}

# @app.post("/chat")
# def chat(request: ChatRequest):
#     user_message = request.message
#     # Here we would call AI model gpt 4.0
#     response_message = f"Echo: {user_message}"
#     return {"response": response_message}