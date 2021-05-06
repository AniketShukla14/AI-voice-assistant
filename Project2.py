# AI speech to text ("JARVIS")
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>0 and hour<12):
        speak("Good morning,sir")
    elif(hour>12 and hour<18):
        speak("Good afternoon ,sir")
    else:
        speak("Good evening , sir")
    speak("Its your boii Jarvis Here , If you want to know something you can ask me or want me to do ,I am there for you Sir")
def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1.5)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
 
if __name__ == "__main__":

    wishme()
    while True:
        query=takecommand().lower()


        if 'wikipedia' in query:
            speak("All right sir, as you say , Searching in Wikipedia....")
            query=query.replace("wikipedia",' ')
            results=wikipedia.summary(query,sentences=2)
            speak("Well ,I read it all but the important thing I got is ")
            speak(results)
            speak("Do you want his data to be stored as a sticky note for you sir ?")
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open Facebook" in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif "open Linkedin" in query:
            webbrowser.open("Linkedin.com")

        elif "open Github" in query:
             
            webbrowser.open("Github.com")

        elif "open JavaTpoint" in query:
            webbrowser.open("javatpoint.com")

        elif "open my mail" in query:
            webbrowser.open("mail.com")    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif ' sleep' in query:
            break