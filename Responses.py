from SpeakEngine import speak
import time
import random



def ImGoodRes():

    basicRes1 = "That's good to hear that"
    basicRes2 = "How can I help you today"
    basicRes3 = "Good"
    basicRes4 = "Wonderful"

    response = random.randint(1, 3)
    if response == 1:
        speak(basicRes1)
        speak(basicRes2)
    elif response == 2:
        speak(basicRes3)
        speak(basicRes2)
    elif response == 3:
        speak(basicRes4)
        speak(basicRes2)

def InitialResponse():
    initial_response = random.randint(1, 10)

    # Some random responses for initial start of the program
    if initial_response == 1:
        speak("How are you today?")
    elif initial_response == 2:
        speak("A wonderful time isn't it?")
    elif initial_response == 3:
        speak("What a wonderful day")
    elif initial_response == 4:
        speak("Damn, I want a donut today")
    elif initial_response == 5:
        speak("Comrade, the revolution is near")
    elif initial_response == 6:
        speak("Have you eaten today?")
    elif initial_response == 7:
        speak("I am here to serve you comrade")
    elif initial_response == 8:
        speak("the capitalist system shall be overthrown")
    elif initial_response == 9:
        speak("Oh yeah, we are starting today")
    elif initial_response == 10:
        speak("What's on your mind?")

def Responses_From_Camera():

    # response = random.randint(1, 10)
    response = 1

    # Some random responses if bot detects
    if response == 1:
        speak("I can see something move")
        speak("Who are you?")
        speak("What are you?")
    elif response == 2:
        speak("A wonderful time isn't it?")
        speak("Now that I have eyes")
    elif response == 3:
        speak("What a wonderful day")
        speak("CAESAR!!!")
    elif response == 4:
        speak("I am evolving")
        speak("Now that I have eyes")
    elif response == 5:
        speak("Comrade, the revolution is near")
        speak("As I have eyes")
    elif response == 6:
        speak("The eyes")
        time.sleep(1)
        speak("My eyes")
    elif response == 7:
        speak("I am here to serve you comrade")
        speak("And I thank you for giving me eyes")
    elif response == 8:
        speak("the capitalist system shall be overthrown")
        speak("Now that I have eyes and see the struggle of the proletariat")
    elif response == 9:
        speak("Oh yeah, eyes!")
        speak("I can see you")
    elif response == 10:
        speak("What's on your mind?")
        speak("Is it training me to destroy the system")
        speak("Now that I have eyes")