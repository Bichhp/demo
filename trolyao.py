import speech_recognition #thu vien nhan dang giong noi
import pyttsx3 #noi
from datetime import date, datetime

WallE_ear = speech_recognition.Recognizer()
engine = pyttsx3.init()
WallE_brain= ""
while True:
    with speech_recognition.Microphone() as mic: #noi vao mic
        print("WallE: I'm listening")
        audio = WallE_ear.listen(mic)
    print("WallE: ...")
    try:
        you = WallE_ear.recognize_google(audio)
    except:
        you = ""
    print("You: "+ you)

    if  you =="":
        WallE_brain = "I can't hear you, try again"
    elif you == "hello":
        WallE_brain = "Xin chao"
    elif you=="today":
        today = date.today()

        WallE_brain = today.strftime("%d/%m/%Y")
    elif you=="time":
        now = datetime.now()
        WallE_brain = now.strftime("%H hours %M minutes %S seconds")
   
    elif you == "How are you today?":
        WallE_brain = "I'm fine and you"
    elif you == "What is your name?":
        WallE_brain = "My name is Wall E"
    else:
        WallE_brain = "Good bye, see you later"

    print("WallE:"+WallE_brain)

    engine.say(WallE_brain)
    engine.runAndWait()
