# from multiprocessing.spawn import _main
# from tkinter.tix import MAIN
# from pip import main
from datetime import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio_txt):
    engine.say(audio_txt)
    engine.runAndWait()

def takeCommand():
    ''' takes input from the microphone and returns output string '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognisng...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said : {query}\n")
    except Exception as e:
        # print(e)
        print("Please say that again!")
        return "None"
    return query

if __name__ == "__main__":
    speak("hello revanth")
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            speak(f"According to wikipedia {result}")
            # speak(result)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.get("chrome").open("youtube.com")
        elif "start practice" in query:
            speak("opening codechef")
            webbrowser.get("chrome").open("codechef.com")
        elif "play music" in query:
            speak("playing music")
            music_dir = 'C:\\Users\\USER\\Downloads\\B9ECED6F.ASUSPCAssistant_qmba6cd70vzyy!App\\Link_to_MyASUS'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[5]))
        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is \n  {strtime}")
        elif "start visual" in query:
            speak("opening visual code")
            filepath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(filepath)
        elif "hello" in query:
            filepath = "C:\\Users\\USER\\Desktop\\jarvis"
            files = os.listdir(filepath)
            print(files)
            os.startfile(os.path.join(filepath,files[0]))
        elif "stop jarvis" in query:
            break
#for sending mails use smtlib module