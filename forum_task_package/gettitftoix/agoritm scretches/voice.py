import speech_recognition as sr
import os

rec = sr.Recognizer()
mic = sr.Microphone()


def zap(text):
    if str(text) == "shall":
        os.system("start cmd.exe")


try:
    while True:
        with mic as source:
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)
            result = rec.recognize_google(audio, language="ru_RU")
            result = result.lower()
            print(format(result))
            zap(format(result))
except sr.UnknownValueError:
    print("google упал ")
