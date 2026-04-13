import requests
from Backend.Shared.config import LANGUAGE_MODEL, LANGUAGE_MODEL_ENDPOINT
def generate_answer(prompt:str):

    try:

        response = requests.post(
            LANGUAGE_MODEL_ENDPOINT,
            json = {
                "model": LANGUAGE_MODEL,
                "num_batch": 64,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]
    
    except Exception as e:
        
        raise RuntimeError(f"Failed to generate Response") from e


def warmup_ollama():

    try:
    
        response = requests.post(
            LANGUAGE_MODEL_ENDPOINT,
            json = {
            "model": LANGUAGE_MODEL,
            "num_batch": 64,
            "prompt": "Respond with: Model is ready",
            "stream": False,
            "keep_alive": -1,
            }
        )

        return response.json()["response"]
    
    except Exception as e:
        
        raise RuntimeError(f"Failed to Warm up Ollama") from e

