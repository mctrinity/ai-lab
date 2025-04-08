# character_creator/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from character_engine import generate_character, generate_character_image
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class CharacterRequest(BaseModel):
    name: str
    role: str
    include_image: bool = True

@app.post("/generate")
def generate(request: CharacterRequest):
    try:
        character = generate_character(request.name, request.role)
        if request.include_image:
            image_url = generate_character_image(character)
            return {"image_url": image_url}
        return {"message": "Character created, image not requested."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# character_creator/character_engine.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_character(name: str, role: str) -> str:
    prompt = (
        f"Create a visual description of a fictional character named {name}, "
        f"who plays the role of a {role}. Keep it short and visually focused."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def generate_character_image(character_description: str) -> str:
    visual_prompt = character_description.split(". ")[0][:300]

    image = client.images.generate(
        model="dall-e-3",
        prompt=visual_prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    return image.data[0].url

