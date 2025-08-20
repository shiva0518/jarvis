import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
def secondyearCSEA():
    from datetime import date
    import calendar
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    my_date=date.today()
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    #print (Time)
    Day=calendar.day_name[my_date.weekday()]
    #print(Day)
    if(Day=="Monday"):
        speak("Today is monday")
        if(Time>"9:30:00" and Time < "10:40:00"):
            print("Now they have IPR class")
            speak("Now they have IPR class")
        elif (Time>"10:40:00" and Time < "11:40:00"):
            print("Now they have CN class")
            speak("Now they have CN class")
        elif(Time>"11:40:00" and Time < "11:50:00"):
            print("now they have break next they have DM class")
            speak("now they have break next they have DM class")
        elif(Time>"11:50:00" and Time < "12:50:00"):
            print("Now they have DM class")
            speak("Now they have DM class")
        elif(Time>"12:50:00" and Time < "13:40:00"):
            print("Now they have Lunch break next they have OOP class")
            speak("Now they have Lunch break next they have OOP class")
        elif(Time>"13:40:00" and Time < "14:40:00"):
            print("Now they have OOP class")
            speak("Now they have OOP class")
        elif(Time>"14:40:00" and Time < "15:40:00"):
            print("Now they have FLAT class")
            speak("Now they have FLAT class")
        else:
            print("Now they have no classes")
            speak("Now they have no classes")
    elif (Day=="Tuesday"):
        if(Time>"9:30:00" and Time < "10:40:00"):
            print("Now they have FLAT class")
            speak("Now they have FLAT class")
        elif (Time>"10:40:00" and Time < "11:40:00"):
            print("Now they have DBMS class")
        elif(Time>"11:40:00" and Time < "11:50:00"):
            print("now they have break next they have GE&PC class")
        elif(Time>"11:50:00" and Time < "12:50:00"):
            print("Now they have GE&PC class")
        elif(Time>"12:50:00" and Time < "13:40:00"):
            print("Now they have Lunch break next they have OOP class")
        elif(Time>"13:40:00" and Time < "14:40:00"):
            print("Now they have OOP class")
        elif(Time>"14:40:00" and Time < "15:40:00"):
            print("Now they have CN class")
        else:
            print("Now they have no classes")
    elif(Day=="Wednesday"):
        if(Time>"9:30:00" and Time < "10:40:00"):
            print("Now they have DM class")
            speak("Now they have DM class")
        elif (Time>"10:40:00" and Time < "11:40:00"):
            print("Now they have IPR class")
            speak("Now they have IPR class")
        elif(Time>"11:40:00" and Time < "11:50:00"):
            print("now they have break next they have DBMS class")
            speak("now they have break next they have DBMS class")
        elif(Time>"11:50:00" and Time < "12:50:00"):
            print("Now they have DBMS class")
            speak("Now they have DBMS class")
        elif(Time>"12:50:00" and Time < "13:40:00"):
            print("Now they have Lunch break next they have OOP lab")
            speak("Now they have Lunch break next they have OOP lab")
        elif(Time>"13:40:00" and Time < "14:40:00"):
            print("Now they have OOP lab")
            speak("Now they have OOP lab")
        elif(Time>"14:40:00" and Time < "15:40:00"):
            print("Now they have OOP lab")
            speak("Now they have OOP lab")
        else:
            print("Now they have no classes")
            speak("Now they have no classes")
    elif(Day=="Thursday"):

        if(Time>"9:30:00" and Time < "10:40:00"):
            print("Now they have CN class")
        elif (Time>"10:40:00" and Time < "11:40:00"):
            print("Now they have DM class")
        elif(Time>"11:40:00" and Time < "11:50:00"):
            print("now they have break next they have DBMS class")
        elif(Time>"11:50:00" and Time < "12:50:00"):
            print("Now they have DBMS class")
        elif(Time>"12:50:00" and Time < "13:40:00"):
            print("Now they have Lunch break next they have FLAT class")
        elif(Time>"13:40:00" and Time < "14:40:00"):
            print("Now they have FLAT class")
        elif(Time>"14:40:00" and Time < "15:40:00"):
            print("Now they have OOP class")
        else:
            print("Now they have no classes")
    elif(Day=="Friday"):
        speak("Today is friday")
        if(Time>"9:30:00" and Time < "10:40:00"):
            print("Now they have OOP class")
            speak("Now they have OOP class")
        elif (Time>"10:40:00" and Time < "11:40:00"):
            print("Now they have CN class")
            speak("Now they have CN class")
        elif(Time>"11:40:00" and Time < "11:50:00"):
            print("now they have break next they have IPR class")
            speak("now they have break next they have IPR class")
        elif(Time>"11:50:00" and Time < "12:50:00"):
            print("Now they have IPR class")
            speak("Now they have IPR class")
        elif(Time>"12:50:00" and Time < "13:40:00"):
            print("Now they have Lunch break next they have FLAt class")
            speak("Now they have Lunch break next they have FLAt class")
        elif(Time>"13:40:00" and Time < "14:40:00"):
            print("Now they have FLAT class")
            speak("Now they have FLAT class")
        elif(Time>"14:40:00" and Time < "15:40:00"):
            print("Now they have DM class")
            speak("Now they have DM class")
        else:
            print("Now they have no classes")
            speak("Now they have no classes")
    elif(Day=="Saturday"):
        if(Time>"9:30:00" and Time < "10:40:00"):
            print("Now they have IPR class")
        elif (Time>"10:40:00" and Time < "11:40:00"):
            print("Now they have DBMS lab")
        elif(Time>"11:40:00" and Time < "11:50:00"):
            print("now they have break next they have DBMS lab")
        elif(Time>"11:50:00" and Time < "12:50:00"):
            print("Now they have DBMS lab")
        elif(Time>"12:50:00" and Time < "13:40:00"):
            print("Now they have Lunch break next they have DBMS class")
        elif(Time>"13:40:00" and Time < "14:40:00"):
            print("Now they have DBMS class")
        elif(Time>"14:40:00" and Time < "15:40:00"):
            print("Now they have GE&PC class")
        else:
            print("Now they have no classes")
    else:
        speak("Today is sunday")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis . Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play song' in query:
            music_dir = 'C:\Anime\Death Note'
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "Downloads"
            os.startfile(codePath)


        elif "youtube" in query:
            speak("This is what I found for your search!")
            query = query.replace("youtube search", "")
            query = query.replace("youtube", "")
            query = query.replace("jarvis", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            # pywhatkit.playonyt(query)
            exit()

        elif "google" in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            speak("This is what I found on google")

            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query, 1)
                speak(result)

            except:
                speak("I can't find that..")
            exit()

        elif "time table" in query:
            os.startfile("C:\\VS Code Practice\\.vscode\\second year CSE-A.pdf")
            book = open("C:\\VS Code Practice\\.vscode\\second year CSE-A.pdf",'rb')
            secondyearCSEA()
            exit()
            
        elif "bye" in query:
            exit()

