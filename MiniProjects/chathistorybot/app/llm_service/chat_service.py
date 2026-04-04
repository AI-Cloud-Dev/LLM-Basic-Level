import requests

# def get_llm_response(messages: list):
#     payload ={
#         "model": "llama3",
#         "messages": messages,
#         "stream": False        
#     }
#     response = requests.post("http://localhost:11434/api/generate", json = payload)
#     data = response.json()
#     return data["message"]["content"]



def get_llm_response(messages: list):
    """
    Sends the chat history to the LLM (Ollama) and returns assistant response.
    messages: list of dicts with {"role": ..., "content": ...}
    """
    payload = {
        "model": "llama3",
        "messages": messages,
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/chat", json=payload)
        response.raise_for_status()  # Raise error if HTTP failed
        data = response.json()
        # Ollama returns content under: data["message"]["content"]
        return data["message"]["content"]
    except Exception as e:
        return f"[LLM Error]: {e}"