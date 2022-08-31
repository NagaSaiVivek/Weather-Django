import speech_recognition as sr
import os
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
while True:
    wake=takeCommand().lower()
    if 'wake up' in wake:
        os.startfile('C:\\Users\\Vivek\\Desktop\\vicky\\Friday\\GUI\\Friday3.py')
