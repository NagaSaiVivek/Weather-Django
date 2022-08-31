from FridayUi import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from ChatBot import *
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
import sys
from playsound import playsound
from selenium import webdriver
chrome = webbrowser.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
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


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.Task_Gui()

    def takeCommand(self):
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


    def Task_Gui(self):
        wishMe()
        while True:
            self.query = self.takeCommand().lower()
            if 'you need a break' in self.query:
                speak("Ok Sir , You Can Call Me Anytime !")
                speak("Just Say Wake Up Friday!")
                exit()
            elif 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            #Opening websites 
            elif 'website' in self.query:
                self.query = self.query.replace("website", "")
                web1 = self.query.replace("open", "")
                web1 = web1.replace(" ", "")
                if 'amazon' in self.query:
                    web2 = 'amazon' + '.in'
                else:
                    x = '.com'
                    web2 = web1 + x
                speak("Launching " + web1 + " website")
                chrome.open(web2)
            elif 'open cbit lms' in self.query:
                speak('Opening Learning CBIT')
                chrome.open('learning.cbit.org.in')
            elif 'time' in self.query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak(" The current time is " + time)
            elif 'joke' in self.query:
                speak("Here is a joke for you")
                a = pyjokes.get_joke()
                speak(a)
            #Play on Youtube
            elif 'on youtube' in self.query:
                video = self.query.replace('play', '')
                speak('playing ' + video)
                pywhatkit.playonyt(video)
            #Opening Apps
            elif 'code' in self.query:
                speak('Opening VS Code')
                codepath = "C:\\Users\\Vivek\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
                os.startfile(codepath)
            elif 'scilab' in self.query:
                speak('Opening Scilab')
                scipath = "C:\\Program Files\\scilab-6.1.0\\bin\\WScilex.exe"
                os.startfile(scipath)
            elif 'chrome' in self.query:
                speak('Opening Google Chrome')
                cpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(cpath)
            elif 'firefox' in self.query:
                speak('Opening Mozilla Firefox')
                fpath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                os.startfile(fpath)
            elif 'whatsapp' in self.query:
                speak('Opening WhatsApp')
                os.startfile('C:\\Users\\Vivek\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
            #Google search
            elif 'search' in self.query:
                self.query = self.query.replace('search', '')
                self.query = self.query.replace('about', '')
                speak('Searching about '+self.query+' in google')
                pywhatkit.search(self.query)
                speak('here is what i found')
            # Playing Songs in PC
            elif 'my songs' in self.query:
                speak("Playing your songs collection on PC.")
                os.startfile('C:\\Users\\Vivek\\Music\\songs\\The Plan.mp3')
            #Taking screenshot
            elif 'screenshot' in self.query:
                speak("Sure sir!")
                scr = pyautogui.screenshot()
                ran = random.randint(1, 10000)
                scr.save('C:\\Users\\Vivek\\Desktop\\'+str(ran)+'.jpg')
            # Youtube Automation
            elif 'pause' in self.query:
                press('space bar')
            elif 'play' in self.query:
                press('space bar')
            elif 'full screen' in self.query:
                press('f')
            elif 'forward' in self.query:
                press('l')
            elif 'rewind' in self.query:
                press('j')
            elif 'previous' in self.query:
                press_and_release('SHIFT + p')
            elif 'next' in self.query:
                press_and_release('SHIFT + n')
            elif 'mute' in self.query:
                press('m')
            elif 'unmute' in self.query:
                press('m')
            elif 'volume up' in self.query:
                pyautogui.press('volumeup')
            elif 'volume down' in self.query:
                pyautogui.press('volumedown')
            elif 'alarm' in self.query:
                speak('Tell me the time sir!, for example set an alarm for 5:30 AM')
                tt= self.takeCommand().lower()
                tt=tt.replace("set an alarm for ","")
                tt=tt.replace(".","")
                tt=tt.upper()
                while True:
                    timenow= datetime.datetime.now()
                    now = timenow.strftime("%I:%M %p")
                    if now==tt:
                        speak("Time to wake up sir!")
                        playsound('alarm.wav')
                    elif now>tt:
                        break
            elif 'weather' in self.query:
                driver = webdriver.Chrome()
                speak("Give me your city's name")
                city= self.takeCommand()
                driver.get(f"https://www.weather-forecast.com/locations/{city}/forecasts/latest")
                speak(driver.find_elements_by_class_name("b-forecast__table-description-cell--js")[0].text)
            elif 'none' in self.query:
                pass
            elif 'none' not in self.query:
                reply=ChatterBot(self.query)
                speak(reply)
                if 'later' or 'bye' or 'exit' or 'sleep' in self.query:
                    exit()
                else:
                    continue


startFunction = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.friday_ui = Ui_MainWindow()
        self.friday_ui.setupUi(self)

        self.friday_ui.START.clicked.connect(self.startFunc)
        self.friday_ui.EXIT.clicked.connect(self.close)
    
    def startFunc(self):
        self.friday_ui.movies_GIF2 = QMovie("earth.gif")
        self.friday_ui.GIF2.setMovie(self.friday_ui.movies_GIF2)
        self.friday_ui.movies_GIF2.start()

        self.friday_ui.movies_voice1 = QMovie("__02-____.gif")
        self.friday_ui.Voice.setMovie(self.friday_ui.movies_voice1)
        self.friday_ui.movies_voice1.start()

        self.friday_ui.movies_q3 = QMovie("ezgif.com-gif-maker.gif")
        self.friday_ui.label_3.setMovie(self.friday_ui.movies_q3)
        self.friday_ui.movies_q3.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startFunction.start()

    def showtime(self):
        current_time = QTime.currentTime()
        label_4 = current_time.toString("hh:mm:ss")
        labbel = " TIME :  " + label_4 
        self.friday_ui.label_4.setText(labbel)

Gui_App =QApplication(sys.argv)
Gui_Friday = Gui_Start()
Gui_Friday.show()
sys.exit(Gui_App.exec_())