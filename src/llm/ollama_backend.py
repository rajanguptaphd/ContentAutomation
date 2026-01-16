import requests
from src.llm.base import BaseLLM

class OllamaBackend(BaseLLM):
    def __init__(self, model_name, max_new_tokens):
        self.model_name = model_name
        self.max_new_tokens = max_new_tokens
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": self.max_new_tokens
            }
        }

        response = requests.post(self.url, json=payload)
        response.raise_for_status()
        return response.json()["response"].strip()
