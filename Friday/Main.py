import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
import pyautogui
import random
from keyboard import *


chrome = webbrowser.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Friday. What can I do for you sir!")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=500
        r.adjust_for_ambient_noise(source)  
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        if 'Friday' in query:
            query = query.replace("Friday", "")

    except Exception as e:
        # print(e)
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
            print(results)
            speak(results)
        #Opening websites 
        elif 'website' in query:
            query = query.replace("website", "")
            web1 = query.replace("open", "")
            web1 = web1.replace(" ", "")
            if 'amazon' in query:
                web2 = 'amazon' + '.in'
                chrome.open(web2)
            else:
                x = '.com'
                web2 = web1 + x
            speak("Launching " + web1 + " website")
            chrome.open(web2)
        elif 'open cbit lms' in query:
            speak('Opening Learning CBIT')
            chrome.open('learning.cbit.org.in')
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(" The current time is " + time)
        elif 'joke' in query:
            speak("Here is a joke for you")
            a = pyjokes.get_joke()
            speak(a)
        #Play on Youtube
        elif 'on youtube' in query:
            video = query.replace('play', '')
            speak('playing ' + video)
            pywhatkit.playonyt(video)
        #Opening Apps
        elif 'code' in query:
            speak('Opening VS Code')
            codepath = "C:\\Users\\Nag\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)
        elif 'scilab' in query:
            speak('Opening Scilab')
            scipath = "C:\\Program Files\\scilab-6.1.0\\bin\\WScilex.exe"
            os.startfile(scipath)
        elif 'chrome' in query:
            speak('Opening Google Chrome')
            cpath = "C:\Program Files\Google\Chrome\Application\\chrome.exe"
            os.startfile(cpath)
        elif 'firefox' in query:
            speak('Opening Mozilla Firefox')
            fpath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(fpath)
        #Google search
        elif 'search' in query:
            query = query.replace('search', '')
            query = query.replace('about', '')
            speak('Searching about '+query+' in google')
            pywhatkit.search(query)
            speak('here is what i found')
        # Playing Songs in PC
        elif 'my songs' in query:
            speak("Playing your songs collection on PC.")
            os.startfile('C:\\Users\\Nag\\Music\\songs\\The Plan.mp3')
        #Taking screenshot
        elif 'screenshot' in query:
            speak("Sure sir!")
            scr = pyautogui.screenshot()
            ran = random.randint(1, 10000)
            scr.save('C:\\Users\\Nag\\Desktop\\'+str(ran)+'.jpg')
        # Youtube Automation
        elif 'pause' in query:
            press('space bar')
        elif 'resume' in query:
            press('space bar')
        elif 'full screen' in query:
            press('f')
        elif 'forward' in query:
            press('l')
        elif 'rewind' in query:
            press('j')
        elif 'previous' in query:
            press_and_release('SHIFT + p')
        elif 'next' in query:
            press_and_release('SHIFT + n')
        elif 'mute' in query:
            press('m')
        elif 'unmute' in query:
            press('m')
        

        