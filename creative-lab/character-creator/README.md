# 🧙‍♂️ Character Creator

A microservice that generates detailed fictional character profiles using OpenAI's GPT models. Give it a name, setting, and role — and it'll return a rich character description you can use for games, stories, or visual generation.

---

## 🔥 Features

- Prompt-based character profile generation
- Personality traits, backstory, motivations, and a twist
- Designed to integrate with visual AI tools (like Midjourney or DALL·E)
- Built with FastAPI

---

## 📦 Project Structure

```
character-creator/
├── main.py                # FastAPI app entrypoint
├── character_engine.py    # Core logic to talk to OpenAI
├── requirements.txt       # Python dependencies
├── .env                   # API key config (not committed)
```

---

## ⚙️ Setup

### 1. Clone and activate your virtual environment

```bash
cd character-creator
# make sure your venv is active
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key

Create a `.env` file:

```bash
OPENAI_API_KEY=your-api-key-here
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

Open in browser:
```
http://localhost:8000/docs
```

---

## 🧪 Example Request

POST to `/generate`:
```json
{
  "name": "Zara Nightshade",
  "setting": "cyberpunk dystopia",
  "role": "black market tech smuggler"
}
```

Returns:
```json
{
  "character": "Zara Nightshade is a tech-savvy loner with a mysterious past..."
}
```

---

## 🧠 Powered By

- [FastAPI](https://fastapi.tiangolo.com)
- [OpenAI API](https://platform.openai.com)
- [Python dotenv](https://pypi.org/project/python-dotenv/)

---

## 📬 Future Ideas

- Export to Markdown or PDF
- Add image generation prompt helper
- Add personality sliders (e.g. introvert vs. extrovert)
- Save and fetch previous characters

---

Let the character creation magic begin! ✨

