import traceback
from fastapi import FastAPI, HTTPException
from app.schemas import CreateAgentRequest
from app.services import vapi, retell
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post("/create-agent")
def create_agent(request: CreateAgentRequest):
    try:
        if request.provider == "vapi":
            return vapi.create_vapi_agent(request)
        elif request.provider == "retell":
            return retell.create_retell_agent(request)
        else:
            raise HTTPException(status_code=400, detail="Invalid provider")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
