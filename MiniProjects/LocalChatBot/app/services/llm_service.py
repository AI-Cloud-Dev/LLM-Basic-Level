import requests


def get_ollama_response(user_input: str) -> str:
    payload = {
        "model": "llama3",
        "prompt": user_input,
        "stream": False}
    response = requests.post("http://localhost:11434/api/generate", json = payload)
    data = response.json()
    # if response.status_code == 200:
    #     return response.json().get("response", "").strip()
    # else:
    #     # return f"Error: {response.status_code} - {response.text}"
    return data.get("response")