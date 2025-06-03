import os
import requests
from fastapi import HTTPException
from app.schemas import CreateAgentRequest

def create_retell_agent(request: CreateAgentRequest):
    api_key = os.getenv("RETELL_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Retell API key not set")

    url = "https://api.retellai.com/v1/create-agent"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Build request body
    body = {
        "agent_name": request.name,
        "voice_id": request.voice_id,
        "response_engine": {
            "type": "retell-llm",
            "llm_id": os.getenv("RETELL_LLM_ID")  # You must set this in .env
        },
        "description": request.description
    }

    response = requests.post(url, json=body, headers=headers)

    # Try to parse JSON response, fall back to raw text
    try:
        response_json = response.json()
    except Exception:
        response_json = {"error_message": response.text}

    if response.status_code >= 400:
        raise HTTPException(status_code=response.status_code, detail=response_json)

    return response_json
