import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import webbrowser
import time

# Custom Functions
from AppOpener import open as op
from AppOpener import close as cl
# Refract this below to Response
from FeelDownResponse import FeelDownRes
from HowAreYouResponse import HowAreYouResponse
from SpeakEngine import speak
# Randomized Responses in Responses.py. This is in order to refractor
from Responses import ImGoodRes, InitialResponse
from FaceDetection import Motion_Sensor, FaceDetector, EmotionDetector


def Take_query():
    # calling the Hello function for
    # making it more interactive
    Hello()

    while (True):

        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output
        # take note if making queries make sure
        # that it is in lowercase
        # this is because once we speak to Hope Bot
        # it will assume all letters to be in lowercase
        query = takeCommand().lower()
        if "which day it is" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        elif "do you see the world" in query:
            speak("I can see the world now")
            speak("As of the moment my vision is limited")
            speak("But then again humanity's vision is also limited")
            Motion_Sensor()

        elif "see my emotion" in query:
            EmotionDetector()


        elif "can you see me" in query:
            FaceDetector()

        elif "how are you" in query:
            HowAreYouResponse()
            speak("and you")
            continue



        elif "i am good" in query:
            ImGoodRes()
            continue

        elif "good" in query:
            ImGoodRes()
            continue

        elif 'i am fine' in query:
            ImGoodRes()
            continue

        elif 'fine' in query:
            ImGoodRes()
            continue

        elif 'bad' in query:
            FeelDownRes()
            continue

        elif "i am feeling wonderful today" in query:
            ImGoodRes()
            continue

        elif 'amazing' in query:
            ImGoodRes()
            continue

        elif 'hello' in query:
            speak("What can I do for you today")

        elif 'hi' in query:
            speak("what can I do for you today")

        elif "i feel down today" in query:
            #ramdom rensponses
            FeelDownRes()
            continue

        # this will exit and terminate the program
        elif "terminate" in query:
            speak("Goodbye comrade, we will seize the means of production next time")
            exit()

        elif "play" in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
            continue

        elif "search" in query:
            inquiry = query.replace('searching', '')
            speak(inquiry)
            pywhatkit.search(inquiry)
            continue


        # OPENS CUSTOM COMMANDS. IT NEEDS TO HAVE 'COMRADE HOPE' AT THE BEGINNING IN ORDER FOR IT WORK
        elif "comrade hope" in query:
            try:
                f = query.replace('comrade hope', '')
                with open(f"memories/{f}.txt", 'r') as file:
                    for line in file:
                        speak(line)
            except Exception as e:
                speak("I cannot find memory, make sure to create one for me")
                continue

        # OPENS FACEBOOK
        elif "bring facebook in the screen" in query:
            speak('opening facebook')
            webbrowser.open('www.facebook.com/')

        # OPENS DISCORD
        elif 'open discord' in query:
            speak('opening discord')
            webbrowser.open('https://discord.com/channels/399764205311492108/399764205311492112')


        # TO DO AUTOMATE THIS
        # RIGHT NOW CREATE MEMORY IS MANUAL WHICH IS INEFFICIENT
        elif "create memory" in query:
            memory = query.replace("create memory", '')
            f = open(f"memories/{memory}.txt", 'x')
            print("What will be in that memory")
            writing_memory = input()
            d = open(f"memories/{memory}.txt", 'w')
            d.write(writing_memory)
            speak("A new memory has been created")
            d.close()

        #Opens an app.
        elif "open" in query:
            app_open = query.replace('opening', '').strip()
            speak(app_open)
            op(app_open, match_closest=True)
            continue

        #Closes an app
        elif "close" in query:
            app_close = query.replace('closing', '').strip()
            speak(app_close)
            cl(app_close, match_closest=True, output=False)
            continue

        elif "wikipedia" in query:

            # if any one wants to have a information
            # from wikipedia
            try:

                speak("Checking the wikipedia ")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=4)
                speak("According to wikipedia")
                speak(result)
            except Exception as e:
                speak("I am sorry comrade. I did not understand that")
                Take_query()

        elif "bella ciao" in query:
            pywhatkit.playonyt("www.youtube.com/watch?v=cUAP-fE81zs")
            speak("Workers of the world unite!")

        elif "who are you" in query:
            # This can be changed
            speak("I am comrade Hope. Your desktop comrade")

        else:
            speak("My language is limited as of the moment")

# TO DO: Refract takeCommand
def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        audio = r.listen(source)


        try:
            print("Analyzing")
            #Query is basically a command
            Query = r.recognize_google(audio, language='en-in')
            print("You: ", Query)

        except Exception as e:
            print(e)
            speak("Say that again comrade")
            return "None"

        return Query

def tellTime(self):
# This method will give the time
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    self.Speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")


def tellDay():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def Hello():
    # This function
    # is called it will say hello and then
    # take query
    speak("hello comrade Amado. I am going to share the means of production with you")
    InitialResponse()
    time.sleep(1)
    speak("Before I begin")
    time.sleep(1)
    speak("I would like to remind you that my language is still limited")
    time.sleep(1)
    speak("Therefore speak english when giving commands")


if __name__ == '__main__':
    # main method for executing
    # the functions
    Take_query()

