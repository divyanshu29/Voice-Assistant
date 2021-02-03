import pyttsx3 #used to convert voices into sentances
import datetime #used for providing date and time
import speech_recognition as sr 
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5') # used to take voices (sapi5)
voices =engine.getProperty('voices')
# print(voices[0].id) # [0]represents the voice of boy and [1] represents the voces of a girl
engine.setProperty('voice',voices[0].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good evening!")

    speak("I am Jarvis. Please tell me sir how may i help you!")

def takeCommand():
    #it takes microphone inputs from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio ,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e) use this command in that case you want to show the error
        print("Say that agian please...!")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() #logic for executing task
    
        if 'wikipedia' in query:
            speak('Searching Wikipeadia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")

        elif 'open google'in query:
            webbrowser.open("google.com")

        elif 'open whatsapp'in query:
            webbrowser.open("whatsapp.com")

        elif 'play music'in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}") 
            print(strTime)   
        
        elif 'open code' in query:
            codePath = "C:\\Users\\divya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
        elif 'shutdown' in query:
            speak('Have a good day sir now i am shutting down')
            print("Have a good day sir now i am shutting down")
            break