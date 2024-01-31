import pyttsx3                     
import speech_recognition as sr     
import datetime     
import wikipedia                    
import webbrowser
import os

engine = pyttsx3.init('sapi5')       
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):     
    '''
    Enables the program to speak using 'pyttsx3' speech library
    '''
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    Greets the user based on the current time
    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  

    speak("I am your Virtual Assistant. How may I help you?")       

def takeCommand():
    '''
    Takes voice command from the user and returns a string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open calendar' in query:
            webbrowser.open("calendar.google.com")

        elif 'open stackoverflow' in query or 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Kumarran Mahesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open discord' in query:
            codePath = "C:\\Users\\Kumarran Mahesh\\AppData\\Local\\Discord\\Update.exe"
            os.startfile(codePath)

        elif 'open sublime' in query:
            codePath = "C:\\Program Files\\Sublime Text\\sublime_text.exe"
            os.startfile(codePath)

        elif 'open spotify' in query or 'play music' in query:
            codePath = "C:\\Users\\Kumarran Mahesh\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath) 
        
        elif 'quit' in query:
            speak("Have a good day sir.")
            exit()
