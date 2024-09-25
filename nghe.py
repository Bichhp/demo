import speech_recognition

WallE_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Wall E: I'm listening")
    audio = WallE_ear.listen(mic)

try:
    you = WallE_ear.recognize_google(audio)
except:
    you = ""
print("You: "+ you)
