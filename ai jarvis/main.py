import speech_recognition as sr 
import os 
from jaarvis import MainExe
from body.speak import Speak 


def Listen():

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    
    try:
        print("recognizing")
        query = r.recognize_google(audio,language="en")

    except:
        return ""

    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    queery = Listen().lower()
    
    if "wake up" in queery:
        MainExe() 
    else:
        pass    

while True:
    WakeupDetected()
    

