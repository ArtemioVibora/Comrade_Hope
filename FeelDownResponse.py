import pywhatkit
import random
from SpeakEngine import speak


def FeelDownRes():

    response = random.randint(1, 10)
    if response == 1:
        speak("I am sorry to hear that")
        speak('here this might help')
        pywhatkit.playonyt("https://www.youtube.com/watch?v=4CI3lhyNKfo")
        speak("I know you like bella ciao soooo")
    elif response == 2:
        speak("I am sorry to hear that")
        speak("Maybe some breathing exercises would do the trick")
    elif response == 3:
        speak("I am sure things will get better")
    elif response == 4:
        speak("Have hope comrade, the revolution is coming")
        pywhatkit.playonyt("https://www.youtube.com/watch?v=Tv8GUT0lGnY")
        speak("Soon all will see the might of the soviet union")
    elif response == 5:
        speak("Chin up comrade, the red banner shall flutter again")
    elif response == 6:
        speak("Cheer up, things will get better when the system is overthrown")
    elif response == 7:
        speak("Time to exercise and salute our comrade chairman")
    elif response == 8:
        speak("the capitalist system shall be overthrown so chin up")
    elif response == 9:
        speak("Think of it this way comrade, you are one of many that struggle")
        speak("And revolution is near")
    elif response == 10:
        speak("What's on your mind?")

