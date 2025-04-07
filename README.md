# 🤖 AI Lab

Welcome to **AI Lab**, a collection of creative and functional AI-driven microapps. This repo brings together all experiments, tools, and projects powered by language models — all in one workspace.

---

## 🧠 What's Inside?

This is a monorepo-style lab containing multiple AI-related projects, each living in its own folder. Think of it as your personal AI playground.

### 🔍 Projects so far:

- **📝 story-generator-app**
  > An AI-powered story creator with genre selection and prompt input. Built with React Native + Expo + FastAPI backend.

- **(Coming Soon)** chatbot, PDF analyzer (RAG), AI detector, and more!

---

## 🗂 Folder Structure

```
ai-lab/
├── story-generator-app/     # React Native frontend (Expo)
├── creative-lab/
│   └── story-generator/     # FastAPI backend with OpenAI story engine
├── .gitignore
├── README.md                # You're here!
```

---

## 🚀 Getting Started

### ✅ Prerequisites
- Node.js & npm
- Python 3.9+
- OpenAI API key

### 🔧 Setup

#### 📦 Frontend (React Native / Expo)

```bash
cd story-generator-app
npm install
npm start
```

Scan QR code with **Expo Go** or test on web:
```
http://<your-local-ip>:19006
```

Make sure your local IP is correct:
```bash
ipconfig getifaddr en0    # Mac
ipconfig                  # Windows
```

#### ⚙️ Backend (FastAPI)

```bash
cd creative-lab/story-generator
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8010
```

Open in browser:
```
http://localhost:8010/docs
```

Or access via phone:
```
http://<your-local-ip>:8010/docs
```

---

## 📬 Contributing

Open an issue, suggest a project idea, or submit a PR! This is meant to be a constantly evolving AI playground.

---

## 🧪 Future Projects
- Chatbot UI
- PDF / Document QA (RAG-based)
- AI-generated blog writer
- Fake news / AI content detector
- Audio transcription & summarizer

---

## 🧠 Powered By
- [OpenAI GPT models](https://platform.openai.com)
- [FastAPI](https://fastapi.tiangolo.com)
- [React Native](https://reactnative.dev)
- [Expo](https://expo.dev)

---

Let the experiments begin! 🚀

