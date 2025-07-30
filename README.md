# 🎙️ Nova - Your Personal Voice Assistant

**Nova** is a smart, Python-based voice assistant created by [Sreeja Thati](https://github.com/yourusername). Nova listens to your voice, understands commands, and performs helpful tasks — from opening apps to cracking jokes and giving Wikipedia summaries. Think of it as your own mini Jarvis!

---

## 🧠 Features

- 🎧 Voice command recognition
- 🕒 Tells the current time
- 🤖 Tells funny programming jokes using `pyjokes`
- 🌐 Opens apps like Chrome or VS Code
- 🎵 Plays songs on YouTube via `pywhatkit`
- 📚 Answers “Who is...?” queries using Wikipedia
- 🙋 Greets the user on start
- 👋 Says goodbye when exiting
- ❓ Handles unknown or silent voice input gracefully

---

## 🛠️ Tech Stack

- Python 3.8+
- `speech_recognition` – to listen to your voice
- `pyttsx3` – for text-to-speech
- `pywhatkit` – for playing YouTube and more
- `pyjokes` – for random jokes
- `wikipedia` – for fetching quick summaries
- `datetime`, `os`, `webbrowser` – for various tasks

---

## 🚀 Getting Started

### 🔁 1. Clone this repository

```bash
git clone https://github.com/yourusername/Nova-Voice-Assistant.git
cd Nova-Voice-Assistant
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run Nova
bash
Copy
Edit
python nova.py
