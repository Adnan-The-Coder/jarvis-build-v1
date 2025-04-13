# 🤖 JARVIS - Python Virtual Assistant 
### Version - 1

Welcome to **JARVIS**, your AI-powered personal assistant developed using Python. Inspired by Tony Stark's iconic assistant, this project enables voice-activated control of your system — from fetching the weather and managing system settings to answering general questions, searching Wikipedia, telling jokes, and more.

---

## 🧠 Features

- 🎙️ **Voice Recognition** using Google Speech Recognition
- 🧾 **Natural Voice Responses** via pyttsx3 TTS engine
- 🌐 **Internet-based Queries** (weather, news, Wikipedia, WolframAlpha)
- 🧮 **Built-in Calculator**
- 🧑‍💻 **System Commands** (lock PC, shutdown, restart, open applications, etc.)
- 📅 **Date & Time Updates**
- 📂 **Note Taking** & Text File Logging
- 🌍 **Google Maps Location Search**
- 🎵 **Bluetooth Device Connection**
- 💡 **Night Light, Battery Saver & Location Toggle**
- 📊 **System Resource Reporting** (CPU, memory, network)
- 🤣 **Random Jokes**
- 📰 **Top News from Times of India**
- 🌥️ **Live Weather Reports via Google**

---

## 🚀 Getting Started

### 📦 Prerequisites

Make sure you have the following installed:

- Python 3.7+
- Pip (Python package installer)
- Microphone and speakers/headphones

### 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/jarvis-python-assistant.git
cd jarvis-python-assistant
```
Install all required packages:
```
pip install -r requirements.txt
```
Note: You may need to configure access for microphone input and speaker output, especially on Windows.

# 🔑 API Keys
This assistant uses WolframAlpha for computations.

Create a WolframAlpha account and get an API key.

Replace the placeholder in api_key = "your_api_key" with your own key (in a secure way ideally).

# 🎤 Usage
Run the assistant:
```
python main.py
```
JARVIS will:
- Greet you based on the time of day
- Check internet connectivity
- Start listening for voice commands


# 🛠️ Customization
Want to teach JARVIS new tricks? Use the command loop in jarvis.py to add custom voice commands using:
```
elif 'your keyword' in query:
    # Your logic here
```
You can also modify:
- Wake word
- Default city for weather
- System apps to launch
- Jokes API or news source


# ✅ To Do (coming in v2 Build)
- Add GUI interface
- Enable Email & SMS features securely
- Add voice training module
- Integrate OpenAI or GPT APIs for natural conversation
- Add error logging and diagnostics


# 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

# 👨‍💻 Author
Made with ❤️ by ADNAN
Connect with me on LinkedIn | GitHub