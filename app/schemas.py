from pydantic import BaseModel

class CreateAgentRequest(BaseModel):
    provider: str
    name: str
    description: str
    voice_id: str
