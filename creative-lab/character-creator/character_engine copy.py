import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_character(name: str, setting: str, role: str) -> str:
    prompt = (
        f"Create a detailed character profile for a fictional character named {name}, "
        f"who exists in a {setting} setting and plays the role of a {role}. "
        f"Include personality traits, background, goals, and an interesting twist."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
