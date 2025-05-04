from app.ai.huggingface_api import query_huggingface_model

CHAT_MODEL_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-small"

def chat_with_ai(message):
    payload = {"inputs": {"text": message}}
    response = query_huggingface_model(CHAT_MODEL_URL, payload)
    
    reply = response.get('generated_text', "Sorry, I didn't understand that.")
    return reply
