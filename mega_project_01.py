# This project is made for learning purposes only. 
# It is not intended for any commercial use.
# This is my introduction which is not complete yet.
# MY NAME IS  ANKIT CHOUDHARY
# I am a student of B.TECH CSE 2nd year fourth sem .


import pyttsx3
import speech_recognition as sr
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say("I am your assistant")
    engine.runAndWait()
    
if __name__ == "__main__":
    speak("Initializing Ankit...")

      