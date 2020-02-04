import GUI_class
import time
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import urllib.request
import urllib.parse
import re
from cv2 import *

window = GUI_class.GUI()
global img_win
img_win = 0

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('rate', 190)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        window.set_status("Listening...", "green")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
        audio = r.listen(source)
        window.set_status("Processing...", "red")

    try:
        q = r.recognize_google(audio, language='en-in')
        window.msg_box.delete('1.0', GUI_class.END)
        window.msg_box.update()
        print("User said :", q)
        window.set_msg(f"User said :{q}")
        process(q)


    except Exception as e:
        return "none"
    return q


def take():
    speak("Zira Online")
    window.set_msg("Zira Online...")
    while True:
        takeCommand()


def process(q):
    global window
    global img_win

    query = q.lower()

    if ('who are you' in query):
        print("Hi! I am Zira.\nI am a personal ChatBot developed by Aastik a.k.a Jingax\n")
        window.set_msg("Hi! I am Zira.\nI am a personal ChatBot developed by Aastik a.k.a Jingax")
        speak("Hi I am zira and I am a personal ChatBot developed by Aastik a k a Jingax\n")


    elif ('wikipedia' in query):

        print("Searching Wikipedia...")
        window.set_msg("Searching Wikipedia...")
        speak("Okay. searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print("According to wikipedia...\n")
        print(results)
        window.set_msg("According to wikipedia...")
        window.set_msg(f"{results}")

        speak("According to wikipedia...\n")
        speak(results)

    elif ('open youtube' in query):
        # query = query.replace("open youtube","")
        print("Opening YouTube..")
        window.set_msg("Opening YouTube..")
        speak("okay. Opening youtube")

        webbrowser.open("youtube.com/")

    elif ('youtube' in query or 'play ' in query):
        query = query.replace("on youtube", "")
        query = query.replace("play", "")
        print(f"Playing {query} on YouTube...")
        window.set_msg(f"Playing {query} on YouTube...")
        speak(f"okay. playing {query} on youtube")

        html_content = urllib.request.urlopen(
            "https://www.youtube.com/results?search_query=" + query.lstrip(' ').replace(' ', '+'))

        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        link = "http://www.youtube.com/watch?v=" + search_results[0]
        webbrowser.open(link)

    elif ('google' in query):
        print("Opening Google..")
        window.set_msg("Opening Google..")
        speak("okay. Opening google")
        webbrowser.open("google.com/")

    elif ('take a picture' in query or 'take a photo' in query):

        cam = VideoCapture(0)
        speak('taking photo in 3, 2, 1, say cheeeze')
        s, img = cam.read()

        if s:  # frame captured without any errors
            img_win = 1
            imwrite("userIMG.png", img)  # save image
            cam.release()
            imshow("Your Photo", img)


        else:
            print("Sorry ,Can't take picture a the moment...")
            window.set_msg("Sorry ,Can't take picture a the moment...")
            speak("Sorry ,Can't take picture a the moment")


    elif (('thank you' in query or 'close' in query) and img_win == 1):
        destroyAllWindows()
        img_win = 0

    elif ('news' in query):
        html_content = urllib.request.urlopen("https://www.timesnownews.com/")
        search_results = re.findall(r'/article/(.+?)"', html_content.read().decode())

        new = []
        for i in range(5):
            news = urllib.request.urlopen("https://www.timesnownews.com/india/article/" + search_results[i])
            head = re.findall(r'<h1>(.+?)</h1>', news.read().decode())
            new.append(head[0])

        print("Here's some news from www.timesnow.com/")
        window.set_msg("Here's some news from www.timesnow.com/")
        speak("Okay, here's some news from times now dot com")

        for i in range(5):
            print(f"{i + 1}) ", new[i])
            window.set_msg(f"{i + 1}) {new[i]}")

        speak(new[0] + ', ' + new[1] + ', ' + new[2] + ', ' + new[3] + ', ' + new[4])
        print("That's all for now...")
        window.set_msg("That's all for now...")
        speak("that's all for now")

    elif ('offline' in query):
        speak("Going Offline")
        quit()

    else:
        print("Sorry Say that again...")
        window.set_msg("Sorry Say that again...")
        speak("Sorry Say that again...")


if __name__ == "__main__":
    window_width = 590  # width of window
    window_height = 728  # height of window

    window.geometry(f"{window_width}x{window_height}")
    window.title("Naina - Voice Assistant")

    b1 = GUI_class.Button(window.background_label, text="Invoke Zira", command=take)
    b1.pack()

    window.create_statusbar_msgbox()
    window.set_status("Ready", "blue")

    window.mainloop()
