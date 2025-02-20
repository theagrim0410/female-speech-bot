import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import yt_dlp
import requests
import os
import shutil



def say(text):

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def take():
  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            say("Sorry, I couldn't understand. Please try again.")
            return ""
        except sr.RequestError:
            say("Network error. Please check your connection.")
            return ""


def wishme():
    
    now = datetime.datetime.now()
    hour = now.hour
    if 4 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 16:
        greeting = "Good Afternoon"
    elif 16 <= hour < 20:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    say(f"{greeting}, sir.")


def chat():

    try:
        genai.configure(api_key="your api key here")  
        model = genai.GenerativeModel("gemini-pro")
        chat_session = model.start_chat(history=[])

        say("If you want to exit, just say 'quit' or 'exit'.")

        while True:
            text = take()
            if text in ["exit", "quit"]:
                say("Okay sir, let's restart.")
                return

            if text:
                response = chat_session.send_message(text)
                say(response.text)

    except Exception as e:
        say("An error occurred in chat mode.")
        print(f"Error: {e}")



def playsongs(query):
    search_url = f"ytsearch1:{query}"  

    try:
        ydl_opts = {
        
            "quiet": True,  
            "default_search": "ytsearch",
            "noplaylist": True,
            "nocheckcertificate": True, 
            "ignoreerrors": True, 
            "no_warnings": True,  
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(search_url, download=False)
            if "entries" in info and len(info["entries"]) > 0:
                video_url = info["entries"][0]["webpage_url"]
                say(f"Sir wait playing {query} song")
               
                brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Update if needed
                webbrowser.register("brave", None, webbrowser.BackgroundBrowser(brave_path))
                webbrowser.get("brave").open(video_url)

            else:
                say("Sorry sir this song is not found")
                

    except Exception as e:
        say("Sir some error occured")

    
def weather(city):
    try:
        api_weather = "weather api key here"
        url_weather = "weather api url"
        params = {
        "key": api_weather,
         "q": city,
        "aqi": "no" 
        }
        
        response = requests.get(url_weather, params=params)


        if response.status_code == 200:
                data = response.json()
    
                location = data['location']['name']
                temp_c = data['current']['temp_c']
                condition = data['current']['condition']['text']
                humidity = data['current']['humidity']
    
                say(f"temperature in {location} is {temp_c} degree celcius condition is {condition} and humidity is {humidity}")
                
        else:
            say("sir city is not found")
            
        

    except Exception as e:
        say("sir some error occurred")
    
    return

def app(app_name):
    
    if "calculator" in app_name:
        app_path="calc.exe"  #update if needed
    else:
        app_path = shutil.which(app_name)
        
    if app_path:
        say(f"sir opening the{app_name}")
        os.startfile(app_path)
    else:
        say("sir application not found")
        
    return
            
def main():
    
    say("Hello, I am laalli, the A.I.")

    while True:
        text = take()
       
        if not text:
            continue
        
        if "open" in text:
            word=text.split()
            if len(word)>1:
                website="".join(word[1:])
            
            say(f"Opening {website}")
            webbrowser.open(f"https://www.{website}.com")
            site_found = True
            break
               
        elif "the time" in text:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {current_time}")

        elif "talk with me" in text:
            say("Yes sir, let's begin.")
            chat()

        elif "what is your name" in text:
            say("Sir, my name is laalli")

        elif "wish me" in text:
            wishme()
            
        elif "show my songs" in text:
            say("okey sir showing")
            webbrowser.open("https://open.spotify.com/playlist/44kMHX5eWfaJmtHab86mBm")
            
            
        elif "play" in text:
            word= text.split()
            if len(word)>1:
                song = " ".join(word[1:])
                
            else:
                song="songs"
            
            playsongs(song)
            break
                
            
        elif "weather" in text or "tempreture" in text:
            word=text.split()
            if len(word)>2:
                city=" ".join(word[2:])
                weather(city)
            else:
                say("sir tell the city name")
                 
            
        elif "app" in text or "application" in text:
            word=text.split()
            if len(word)>1:
                app_name=" ".join(word[1:])
                app(app_name)
            else:
                say("sir application not found")
           
        elif "add" in text:
            word=text.split()
            if len(word)==4:
                num1=int(word[1])
                num2=int(word[3])
                say(str(num1+num2))
            else:
                say("wrong inputs")
        elif "subtract" in text:
            word=text.split()
            if len(word)==4:
                num1=int(word[1])
                num2=int(word[3])
                say(str(num1-num2))
            else:
                say("wrong inputs")
        elif "multiply" in text:
            word=text.split()
            if len(word)==4:
                num1=int(word[1])
                num2=int(word[3])
                say(str(num1*num2))
            else:
                say("wrong inputs")
            say(str(num1+num2))       
        elif "divide" in text:
            word=text.split()
            if len(word)==4:
                num1=int(word[1])
                num2=int(word[3])
                if num2==0:
                    say("sorry cannot divide")
                elif num2!=0:
                    say(str(num1//num2))
            else:
                say("wrong inputs") 
                      
       
            
        elif "what you can do"  in  text:
            say('''I Can do may things 
            1 i can open a website
            2 i can tell my name
            3 i can chat with you as chat bot
            4 i can open the applications
            5 i can play any songs
            6 i can wish you
            7 i can tell the weather conditions
            8 i can do simple calculations of four main operations
            9 i can tell you the current time
            ''')
            
        elif "exit please" in text:
            say("Okay sir, exiting.")
            break  
        
        
if __name__ == '__main__':
    main()
