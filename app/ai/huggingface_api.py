import os
import requests

HUGGINGFACE_API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')

def query_huggingface_model(model_url, payload):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
    }
    response = requests.post(model_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
