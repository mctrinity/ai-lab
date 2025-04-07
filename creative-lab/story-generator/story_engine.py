import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story(prompt: str, genre: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a creative story writer specializing in {genre}."},
            {"role": "user", "content": f"Write a short {genre} story based on: {prompt}"},
        ],
        temperature=0.8,
        max_tokens=600,
    )
    return response.choices[0].message.content.strip()
