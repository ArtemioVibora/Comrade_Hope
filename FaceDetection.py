import cv2
import webbrowser
from deepface import DeepFace
import os
# import matplotlib.pyplot as plt
# import face_recognition
# import numpy as np
from SpeakEngine import speak
from Responses import Responses_From_Camera


# Camera set to 0 if there is a built-in webcam already
# for example using a laptop
cam = cv2.VideoCapture(0)

# Here is where the image is stored
# It verifies if it is you in the camera based upon the image
# Once pygame is installed TO DO: automate the image and automate the name

# This function deletes a face when session ends
def delete_face():
    #mikami acting ahh
    if os.path.exists("facial_image/user.png"):
        os.remove("facial_image/user.png")
    else:
        print("No file exists")

# This function captures a face
def capture_face():
    result, image = cam.read()
    while True:
        try:
            cv2.imshow('User', image)
            cv2.imwrite("facial_image/user.png", image)
            cv2.waitKey(5)
            break
        except Exception as e:
            speak("I cannot see the person in front of me")
            speak("Please try again")
            continue


# This function detects a face and then matches with a reference image
# NOTE: YOU STILL HAVE TO SAVE AN IMAGE INSIDE HOPE BOT
def FaceDetector(name):

    ret, frame = cam.read()
    reference_img = cv2.imread("facial_image/user.png")
    cv2.imshow("User", reference_img)
    cv2.imshow("Person in front of me", frame)

    while True:
        try:
            # use face-recognition py for this
            # especially if we are storing various images of people
            if DeepFace.verify(frame, reference_img.copy())['verified']:
                speak('I can see you')
                speak(f"hello {name}")
                break
            else:
                speak("I cannot see you")
                speak("Please make sure to introduce yourself first")
                break
        except Exception as e:
            speak("I cannot")
            speak("There is something wrong with my programming")
            speak("Please make sure to introduce yourself first")
            break


# This function captures and analyzes emotion
def EmotionDetector():
    ret, frame = cam.read()

    while True:
        cv2.imshow("Hope Bot's eyes", frame)

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
            print(emotionKeys[0] + " is " + emotionValues[0] + " percent")
            print(emotionKeys[1] + " is " + emotionValues[1] + " percent")
            print(emotionKeys[2] + " is " + emotionValues[2] + " percent")
            print(emotionKeys[3] + " is " + emotionValues[3] + " percent")
            print(emotionKeys[4] + " is " + emotionValues[4] + " percent")
            print(emotionKeys[5] + " is " + emotionValues[5] + " percent")
            print(emotionKeys[6] + " is " + emotionValues[6] + " percent")

            # cv2.addText(frame, "World", (50, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))

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
                speak("You look lonely, I can fix that")
                webbrowser.open("https://www.youtube.com/watch?v=lCsgZytKPv8")
            # surprise
            elif float(emotionValues[5]) >= 50:
                speak("surprise motherfucker")
            elif float(emotionValues[6]) >= 50:
                speak("bruh")
                speak("I am literally a talking machine")
                speak("How can you not give out emotions")
            cv2.destroyAllWindows()
            break

        except Exception as e:
            speak("I cannot see the person's face")
            cv2.destroyAllWindows()
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

        # Drawing rectangles
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


# TEST FUNCTIONS
# This is to see which method is effective to use for the face_recognition module
'''def Face_Recognition_Test():
    amado_image = face_recognition.load_image_file("me.jpeg")
    amado_encoding = face_recognition.face_encodings(amado_image)[0]

    known_face_encodings = [amado_encoding]
    known_face_names = ['amado']

    face_location = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:

        ret, frame = cam.read()

        if process_this_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            face_location = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_location)
            face_names = []

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                names = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    names = known_face_names[best_match_index]

                face_names.append(names)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), names in zip(face_location, face_names):
            top *=4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, names, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

def Face_Test2():
    knownImg = face_recognition.load_image_file("me.jpeg")
    knownFaces = face_recognition.face_encodings(face_image= knownImg, num_jitters=50, model='small')[0]


    while True:

        ret, frame = cam.read()

        face_locations = face_recognition.face_locations(frame)

        for face_location in face_locations:
            top, right, bottom, left = face_location
            frame = cv2.rectangle(frame, (right, top), (left, bottom), color = (0,0, 255), thickness=2)

        try:
            # Frame encoding
            Live_face_encoding = face_recognition.face_encodings(face_image=frame,
                                                                 num_jitters=23,
                                                                 model='small')[0]

            # Match with the known faces
            results = face_recognition.compare_faces([knownFaces], Live_face_encoding)

            if results:
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = cv2.putText(img, 'Amado', (30, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                 (255, 0, 0), 2, cv2.LINE_AA)
                plt.imshow(img)
                plt.show()
                break
        except:
            img = cv2.putText(frame, 'Not Amado', (30, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,
                             (255, 0, 0), 2, cv2.LINE_AA)
            # Display the resulting frame
            cv2.imshow('frame', img)
            # End the streaming
            if cv2.waitKey(1) == ord('q'):
                break

        # Release the capture
        cam.release()
        cv2.destroyAllWindows()'''
