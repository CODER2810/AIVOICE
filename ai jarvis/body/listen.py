# 3 functions 
#listen function 
#english translate 
#connect

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator  #pip install googletrans==3.1.0a0 , pip instal PyAudio

# 1 listen english or hindi 
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
    return query




#  2 translator 
def Translationhintoeng(Text): 

    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"you said : {data}")
    return data 

#3 MicExecute 
def Micexecute():
    query = Listen()
    data = Translationhintoeng(query)
    return data 
    
Micexecute()