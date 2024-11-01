import cv2

from deepface import DeepFace

from SpeakEngine import speak
from Responses import Responses_From_Camera


# Camera set to 0 if there is a built-in webcam already
# for example using a laptop
cam = cv2.VideoCapture(0)
# Here is where the image is stored
# It verifies if it is you in the camera based upon the image
# Once pygame is installed TO DO: automate the image and automate the name
reference_img = cv2.imread("me.jpeg")
name = 'Amado'

# This function detects a face and then matches with a reference image
# NOTE: YOU STILL HAVE TO SAVE AN IMAGE INSIDE HOPE BOT
def FaceDetector():

    ret, frame = cam.read()

    while True:
        try:
            if DeepFace.verify(frame, reference_img.copy())['verified']:
                speak('I can see you')
                speak(f"hello {name}")
                break
            else:
                speak("I cannot see you")
                break
        except Exception as e:
            speak("I cannot")
            speak("There is something wrong with my programming")
            break

def EmotionDetector():
    ret, frame = cam.read()

    while True:
        try:
            #How to turn result into input
            # DONE!
            result = DeepFace.analyze(frame, actions=['emotion'])
            # storing result in emotionArr
            # separated them into two using a for loop
            emotionArr = []
            # array storing keys of emotionArr[0]
            emotionKeys = []
            # array storing values of emotionArr[0]
            emotionValues = []

            # for loop removing excess values and keys from variable result
            for i in result:
                for j in i.values():
                    emotionArr.append(j)

            # for loop that stores keys only
            for e in emotionArr[0].keys():
                emotionKeys.append(e)

            # for loop that stores values only
            for d in emotionArr[0].values():
                emotionValues.append(format(d, ".2f"))

            speak("according to my sensors")
            speak(emotionKeys[0] + " is " + emotionValues[0] + "percent")
            speak(emotionKeys[1] + " is " + emotionValues[1] + "percent")
            speak(emotionKeys[2] + " is " + emotionValues[2] + "percent")
            speak(emotionKeys[3] + " is " + emotionValues[3] + "percent")
            speak(emotionKeys[4] + " is " + emotionValues[4] + "percent")
            speak(emotionKeys[5] + " is " + emotionValues[5] + "percent")
            speak(emotionKeys[6] + " is " + emotionValues[6] + "percent")

            #High range, clearly visible emotion
            # Angry
            if float(emotionValues[0]) >= 50:
                speak("You are angry")
                speak("Please calm down")
            # Disgust
            elif float(emotionValues[1]) >= 50:
                speak("You are clearly disgusted")
                speak("Please get some fresh air")
            # Fear
            elif float(emotionValues[2]) >= 50:
                speak("DO NOT FEAR IT")
                speak("You have to fight it")
            # happy
            elif float(emotionValues[3]) >= 50:
                speak("I am glad you are happy")
            # sad
            elif float(emotionValues[4]) >= 50:
                speak("Don't worry be happy")
            # surprise
            elif float(emotionValues[5]) >= 50:
                speak("surprise motherfucker")
            elif float(emotionValues[6]) >= 50:
                speak("bruh")
                speak("I am literally a talking machine")
                speak("How can you not give out emotions")
            break

        except Exception as e:
            speak("I cannot see the person's face")
            break


def Motion_Sensor():
    # THIS FUNCTION DETECTS A PERSON
    # THIS FUNCTION ALSO DETECTS MOVEMENT

    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2 .threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x+h, x+w), (0, 255, 0), 2)
            # This ensures that the vision is set properly
            Responses_From_Camera()

        if cv2.waitKey(1) == ord('q'):
            speak("Closing my eyes")
            cv2.destroyAllWindows()
            break

        cv2.imshow("Hope Bot's eyes", frame1)
