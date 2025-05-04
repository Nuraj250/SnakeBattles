from app.ai.huggingface_api import query_huggingface_model

TTS_MODEL_URL = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech"

def generate_victory_voice(message="Victory! You have won the game!"):
    payload = {"inputs": message}
    response = query_huggingface_model(TTS_MODEL_URL, payload)
    
    audio_data = response['audio']
    audio_path = f"app/static/audio/victory.mp3"
    with open(audio_path, "wb") as f:
        f.write(audio_data)
    
    return "/static/audio/victory.mp3"
