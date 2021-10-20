import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 13:
        speak("Good Morning!")

    elif hour >= 13 and hour < 20:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may i help you ")


def takeCommand():
    #It takes microphone input from the user and returns string input

    r = sr.Recognizer()
    r.energy_threshold = 10000
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"

    return query

loop = True

if __name__ == "__main__":
    wishMe()
    while loop:
        query = takeCommand().lower()  #logic for executing tasks based on queries
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")

        elif 'open chess' in query:
            webbrowser.get(chrome_path).open("chess.com")

        elif 'open amazon' in query:
            webbrowser.get(chrome_path).open("amazon.es")

        elif 'open books' in query:
            book_path = "C:\\Documentos\\Books"
            os.startfile(book_path)

        elif 'play music' in query:
            music_dir = "C:\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'open netflix' in query:
            netflix_path = "C:\\Python\\Dev\\jarvis\\startnetflix.bat"
            subprocess.call([netflix_path])

        elif 'open code' in query:
            code_path = "C:\\Users\\Eddie\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'jarvis quit' in query:
            loop = False

        elif 'mute' in query:
            status = True
            while status:
                query = takeCommand().lower()
                if 'jarvis' in query:
                    speak('Yes sir?')
                    status = False