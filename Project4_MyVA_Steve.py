import pyttsx3 
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser #inbuilt
import os #The OS module provides functions for interacting with the operating system. OS comes under Python's standard utility modules.
import random 
import smtplib #module which allows us to send email through gmail
import wolframalpha
from sys import exit
import pyjokes
import time
import googletrans
from googletrans import Translator

email = {"Shubhangi" : "shubhangi.ug19.cs@nitp.ac.in"}
engine = pyttsx3.init('sapi5') #init function to get an engine instance for the speech synthesis
voices = engine.getProperty('voices') #getProperty() gets the current value of a property
engine.setProperty('voices', voices[0].id) #sets the the voice with id 0

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #To run the speech.All the say() texts won't be said unless the interpreter  encounters runAndWait()

def wishMe(): #will wish according to the time of the day
    time1 = int(datetime.datetime.now().hour)
    if time1>=0 and time1<12:
        speak("Good Morning!")
    elif time1>=12 and time1<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I am Steve , your very own bot , Speed one terahertz, memory one zettabyte , at your service, how may I help you?")

def takeCommand():
    
    r = sr.Recognizer() 
    pyaudio.PyAudio()
    with sr.Microphone() as source:
        speak('Listening')
        audio = r.listen(source)
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        try:
                print("Recognizing...")
                query = r.recognize_google(audio,language="en-IN")#Performs speech recognition on ``audio`` , using the Google Speech Recognition API
                print(f"user said : {query}")
        
        except Exception as e:
                print("Couldn't recognize.Please say that again.")
                return "None"
        return query

def Translatehin():
    r = sr.Recognizer() 
    pyaudio.PyAudio()
    with sr.Microphone() as source:
        speak('Listening')
        audio = r.listen(source)
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        try:
                print("Recognizing...")
                query = r.recognize_google(audio,language="hi-IN")#Performs speech recognition on ``audio`` , using the Google Speech Recognition API
                print(f"user said : {query}")
        
        except Exception as e:
                print("Couldn't recognize.Please say that again.")
                return "None"
        return query

def trans():
    speak('What line do you want to translate')
    line = Translatehin()
    transl = Translator()
    k = transl.translate(line)
    res = k.text
    print(f"The line translates to : {res}")
    speak(f"The line translates to  ,  {res}")
    
    
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls() 
    server.login('royshubhu18@gmail.com','humptydumptysatonawall') 
    server.sendmail('royshubhu18@gmail.com',to,content)   
    speak('Email sent successfully!')
    server.close()
    
    
if __name__ == "__main__":
    

  wishMe()

      
  while True:  
        query = takeCommand().lower()
        myname = "Shubhangi"
        
        
        if 'wikipedia' in query:
             speak('Searching wikipedia...') 
             query = query.replace('wikipedia',"")
             result = wikipedia.summary(query, sentences=2)
             speak('According to wikipedia')
             speak(result)
        elif 'open youtube' in query:
             speak('Opening Youtube')
             webbrowser.open('Youtube.com')
        elif 'open google' in query:
                speak('Opening Google')
                webbrowser.open('https://www.google.co.in/')
        elif 'gmail' in query:
                speak('Opening Gmail')
                webbrowser.open('Gmail.com')
        elif 'open stackoverflow' in query:
                speak('Opening Stackoverflow')
                webbrowser.open('stackoverflow.com')
        elif 'open whatsapp' in query:
                speak('Opening whatsapp')
                webbrowser.open('web.whatsapp.com')
        elif 'open instagram' in query:
                speak('Opening Instagram')
                webbrowser.open('instagram.com')
        elif 'the time' in query:
                time1 = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Mam,The time is {time1}")
        elif 'play music' in query:
                musicdir = 'C:\\Users\\Lenovo\\Music\\mysongs' 
                songs = os.listdir(musicdir) #now songs has a list of all the files and folders in musicdir
                i = random.randint(0, len(musicdir)-1)
                os.startfile(os.path.join(musicdir,songs[i]))
                
        elif 'open vs code' in query:
               path = 'C:\\Users\\Shubhangi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
               os.startfile(path)
               
        elif 'send email' in query:
            speak('Whom do you want to send the mail to')
            a = takeCommand()
            if a in email.keys():
                
                try:
                    speak('What should I say?')
                    content = takeCommand()
                    to = email.get(a)
                    sendEmail(to,content)
                except Exception as e:
                    print(e)
                    print("Could not send email.Please try again.")
        elif 'what is my name' in query:
            speak(f'Your name is {myname} I like your name , mam') 
        
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            myname = query
            speak(f"Name changed From now I'll call you {myname}")
            
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Mam")
        
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif "don't listen" in query or "go to sleep" in query:
            speak("for how much time do you want me to stop listening commands")
            a = int(takeCommand())
            speak(f'Okay, will be back in {a} seconds')
            time.sleep(int(a))
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak(f"User asked to Locate {location}")
            webbrowser.open(f"https://www.google.co.in/maps/place/{location}")
        
        elif "calculate" in query or "what is" in query:
            app_id = "5UEPXQ-Y68LV26QHQ"
            client = wolframalpha.Client(app_id)
            if "calculate" in query:
              indx = query.lower().split().index('calculate')
            elif "what is" in query:
                indx = query.lower().split().index('is')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
        
        elif "translate" in query:
            trans()
        
        elif 'quit' in query:
            speak("Thank you for your time Hope I have helped you ma'am have a great day ahead")
            exit() 
        
        
                
           
            
            
        
            
            
    