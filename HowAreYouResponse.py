from SpeakEngine import speak
import random

# TO DO: REFACTOR THIS
def HowAreYouResponse():
    Bot_Response = random.randint(1, 5)

    if Bot_Response == 1:
        speak("I am good")
    elif Bot_Response == 2:
        speak("I am fine")
    elif Bot_Response == 3:
        speak("I am actually feeling wonderful today")
    elif Bot_Response == 4:
        speak("I feel good yeah")
    elif Bot_Response == 5:
        speak("Fine, thank you")