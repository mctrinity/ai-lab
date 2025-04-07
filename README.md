# 🧪 AI Lab

A collection of creative and utility AI-powered experiments built using FastAPI (Python) and React Native (Expo). Each subproject lives in its own folder and is designed to be easily testable on mobile, tablet, and web.

---

## 📁 Repository Structure

```
ai-lab/
├── creative-lab/
├──── story-generator/        # FastAPI backend for AI story generation
├──── story-generator-app/    # React Native frontend for story generator
├── .gitignore                # Root Git config
├── README.md                 # This file
├── .env                      # Environment variables
```

Each project folder may contain its own `README.md` for detailed instructions.

---

## 📦 Current Projects

| Project               | Description                                     |
|-----------------------|-------------------------------------------------|
| `story-generator`     | Generate short stories based on genre & prompt |
| `story-generator-app` | Cross-platform frontend for story generator     |

More coming soon: AI chatbot, PDF analyzer, resume reviewer...

---

## 🛠️ Setup Instructions

### Backend (FastAPI)

```bash
cd story-generator
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8010
```

➡️ Add your OpenAI key in `.env`:
```
OPENAI_API_KEY=your-key-here
```

➡️ Access the Swagger UI:
```
http://<your-ip>:8010/docs
```

Use `ipconfig getifaddr en0` (macOS) to get your local IP.

---

### Frontend (React Native / Expo)

```bash
cd story-generator-app
npm install
npm start
```

Then open on:
- Web: http://localhost:19006
- Android: via Expo Go app QR
- iOS: via Expo Go or Safari

✅ Make sure your fetch URLs point to your local IP (e.g., `http://192.168.1.102:8010`).

---

## 📱 Mobile Testing Notes

- Be sure your devices are on the **same Wi-Fi** as your development machine.
- Use Expo Go for live reload testing.
- For iOS web testing, visit `http://<your-ip>:19006` in Safari.

---

## 🌟 Vision

This lab is meant for rapid prototyping of fun and useful AI tools. Each project is designed to be:

- 📦 Self-contained
- 🔧 Easy to build & run
- 🔁 Reusable and modular

Feel free to fork and remix!

---

## 📬 Feedback or Ideas?

Open an issue or drop your ideas — always open to creative AI experiments!

