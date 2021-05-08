import speech_recognition as sr
import webbrowser as wb





while True:
    r = sr.Recognizer()
    with  sr.Microphone() as source:

        print("sayy something")
        audio = r.listen(source)
        voice_data = r.recognize_google(audio)
        search='https://www.google.com/search?q='+voice_data
        wb.open_new(search)
        print(search)
