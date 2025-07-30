import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import pyautogui
import webbrowser
import time

# 🧠 Memory to store reminders
memory = ""

# ✅ Initialize speech engine
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
except Exception as e:
    print("❌ Speech engine failed:", e)
    sys.exit()

def talk(text):
    print("🎙️ GIRI:", text)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("❌ Speak Error:", e)

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower().strip()
        print("🗣️ You said:", command)
        return command
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
    except sr.RequestError:
        talk("Network issue with Google service.")
    except Exception as e:
        print("⚠️ Error:", e)
        talk("Unexpected error occurred.")
    return ""

def run_giri():
    global memory
    command = take_command()

    if "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song} on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time_now} ⏰")

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        talk(f"Today is {today} 📅")

    elif "who is sreeja" in command or "who is uday_codes" in command:
        info = (
            "Sreeja — just a curious and creative girl who loves learning cool stuff, especially in AI and tech. "
            "She’s doing her B.Tech in Artificial Intelligence and Machine Learning. She builds projects, joins hackathons, "
            "and dreams big. But she’s also into self-care, skincare, and staying organized like a mini CEO. 🌸"
        )
        talk(info)

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=2)
            talk(info)
        except:
            talk("Sorry, I couldn’t find info about that person.")

    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        talk(f"Searching {query} on Google 🔍")
        webbrowser.open(url)

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        talk("Opening YouTube 🎬")

    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        talk("Opening Gmail 📧")

    elif "open drive" in command:
        webbrowser.open("https://drive.google.com")
        talk("Opening Google Drive 💾")

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found 😬")

    elif "open code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif "open notepad" in command:
        talk("Opening Notepad 📝")
        os.system("notepad")

    elif "open calculator" in command:
        talk("Opening Calculator ➗")
        os.system("calc")

    elif "tell me a joke" in command or "joke" in command:
        talk(pyjokes.get_joke())

    elif "remember that" in command:
        memory = command.replace("remember that", "").strip()
        talk(f"I’ll remember: {memory} 🧠")

    elif "do you remember" in command:
        talk(f"You told me to remember: {memory}" if memory else "I don't remember anything yet.")

    elif "screenshot" in command:
        screenshot = pyautogui.screenshot()
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshot.save(filename)
        talk("Screenshot taken 📸")

    elif "lock screen" in command:
        talk("Locking the screen 🔒")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif "shutdown" in command:
        talk("Shutting down... bye 💀")
        os.system("shutdown /s /t 3")

    elif "restart" in command:
        talk("Restarting the system 🔄")
        os.system("shutdown /r /t 3")

    elif "logout" in command:
        talk("Logging out... 📴")
        os.system("shutdown -l")

    elif "exit" in command or "stop" in command:
        talk("Okay bro, see you later 👋")
        sys.exit()

    elif command:
        talk("I heard you, but I don’t understand that yet 😅")

# 💬 Startup greeting
talk("Yo! I'm sreeja's personal voice assistant. What can I do for you?")
while True:
    run_giri()
