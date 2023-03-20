import speech_recognition as sr 
import os 

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
    
    if "wake up " in queery :
        os.startfile(r"D:\ai jarvis\main.py")
    else:
        pass    

while True:
    WakeupDetected()
