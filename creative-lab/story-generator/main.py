from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from story_engine import generate_story

app = FastAPI()

# Allow frontend access (adjust IPs as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:19006", "http://192.168.X.X:19006"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StoryRequest(BaseModel):
    prompt: str
    genre: str

@app.post("/generate")
async def generate(request: StoryRequest):
    try:
        story = generate_story(request.prompt, request.genre)
        return {"story": story}
    except Exception as e:
        return {"story": f"Error generating story: {e}"}
