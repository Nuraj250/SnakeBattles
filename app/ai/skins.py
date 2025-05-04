from app.ai.huggingface_api import query_huggingface_model
import os
import base64

SKIN_MODEL_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
AVATAR_MODEL_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

def generate_snake_skin(username):
    prompt = f"A cartoon snake skin texture for {username}, colorful and vivid, game art"
    response = query_huggingface_model(SKIN_MODEL_URL, {"inputs": prompt})

    if isinstance(response, dict) and response.get("error"):
        raise Exception(f"HuggingFace Error: {response['error']}")
    
    image_data = base64.b64decode(response['data'])
    skin_path = f"app/static/images/skins/{username}_skin.png"
    with open(skin_path, "wb") as f:
        f.write(image_data)
    
    return f"/static/images/skins/{username}_skin.png"

def generate_player_avatar(username):
    prompt = f"Cute cartoon snake avatar for game player {username}, colorful, simple, round face"
    response = query_huggingface_model(AVATAR_MODEL_URL, {"inputs": prompt})

    if isinstance(response, dict) and response.get("error"):
        raise Exception(f"HuggingFace Error: {response['error']}")
    
    image_data = base64.b64decode(response['data'])
    avatar_path = f"app/static/images/avatars/{username}_avatar.png"
    with open(avatar_path, "wb") as f:
        f.write(image_data)
    
    return f"/static/images/avatars/{username}_avatar.png"
