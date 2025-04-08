import os
from openai import OpenAI

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
