import os
import requests
from fastapi import HTTPException

def create_vapi_agent(request):
    api_key = os.getenv("VAPI_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    body = {
    "name": request.name,
    "voice": {
        "provider": "11labs",
        "voiceId": request.voice_id
    },
    "model": {
        "provider": "openai",
        "model": "gpt-3.5-turbo"
    }
}


    response = requests.post("https://api.vapi.ai/assistant", json=body, headers=headers)

    try:
        response_json = response.json()
    except Exception:
        response_json = {"error_message": response.text}

    if response.status_code >= 400:
        raise HTTPException(status_code=response.status_code, detail=response_json)

    return response_json
