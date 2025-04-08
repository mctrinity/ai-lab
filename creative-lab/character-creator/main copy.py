# character_creator/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from character_engine import generate_character
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class CharacterRequest(BaseModel):
    name: str
    setting: str
    role: str

@app.post("/generate")
def generate(request: CharacterRequest):
    try:
        character = generate_character(request.name, request.setting, request.role)
        return {"character": character}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))