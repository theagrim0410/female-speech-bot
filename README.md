# Laalli - AI Assistant

## Overview
Laalli is a voice-controlled AI assistant that can perform various tasks, including opening websites, playing songs, checking the weather, performing calculations, and chatting using AI. It uses speech recognition, text-to-speech, and web automation for seamless interaction.

## Features
- Open websites
- Play songs from YouTube
- Chat using Google Gemini AI
- Open applications on the system
- Provide weather updates
- Perform basic mathematical calculations
- Tell the current time
- Wish the user based on the time of day

## Installation
### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### Dependencies
Install the required Python packages using:
```
pip install speechrecognition pyttsx3 google-generativeai yt-dlp requests
```

### Additional Requirements
- **For Speech Recognition**: Install `pyaudio`
  - Windows:
    ```
    pip install pipwin
    pipwin install pyaudio
    ```
    
- **For Playing Songs**: Ensure `Brave Browser` or another supported browser is installed.
- **For Weather Information**: Sign up at [WeatherAPI](https://www.weatherapi.com/) to get an API key.

## Usage
Run the script:
```
python speech.py
```

### Commands
- **"Open Google"** → Opens Google.com
- **"Play [song name]"** → Plays the song on YouTube
- **"Talk with me"** → Starts a chatbot session
- **"Weather in [city]"** → Provides weather updates
- **"What is your name?"** → Replies with AI's name
- **"Wish me"** → Greets the user based on the time
- **"Add/Subtract/Multiply/Divide [num1] and [num2]"** → Performs calculations
- **"The time"** → Tells the current time
- **"Exit please"** → Closes the AI assistant

## API Keys
- Replace the placeholder API key in the `chat()` function with a valid Google Generative AI API key.
- Replace the WeatherAPI key with your own.

## Disclaimer
This AI assistant is for educational purposes. Use responsibly!

Developed by Agrim Saxena....
