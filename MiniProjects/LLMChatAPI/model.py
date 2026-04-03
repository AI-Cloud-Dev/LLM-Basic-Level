import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3",
    "prompt": "Explain what an API in simple terms",
    "stream": False    
}

response = requests.post(url, json=data)

print(response.json()["response"])