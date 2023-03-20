from body.listen import Listen
from body.speak import Speak 


def MainExe():

    while True:

        query = Listen()

        if "hello" in query:
            Speak("hi ! i am jarvis !")
        
        elif "bye" in query:
            Speak("bye sir ")
        
        else :
            Speak("i am sleeping sir")