# 📝 Story Generator / Plot Twister

This microservice takes a prompt and genre, then spins up a short story. Think of it as your AI-powered bedtime story engine—with a twist.

---

## 🔧 How to Use

Start the server:

```bash
uvicorn main:app --reload
```

POST to `/generate`:

```json
{
  "genre": "sci-fi",
  "prompt": "humans discover time travel"
}
```

Response:

```json
{
  "story": "In a sci-fi world, where 'humans discover time travel', something unexpected happened..."
}
```

---

## 📄 File Structure

```
story-generator/
├── main.py            # FastAPI app
├── story_engine.py    # Handles story generation logic
├── requirements.txt   # Python dependencies
└── README.md          # Project-specific overview
```

---

## ✨ To Do
- Integrate OpenAI or local LLM
- Add character and tone options
- Random plot twist button
- Export as PDF or text

