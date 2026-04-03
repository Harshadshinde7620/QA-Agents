import requests


def call_llm(prompt: str, model: str = 'mistral', temperature: float = 0.2, max_tokens: int = 512) -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "stream": False
            }
        )

        result = response.json()
        return result.get("response", "").strip()

    except Exception as e:
        return f"Ollama Error: {str(e)}"