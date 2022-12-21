import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
#import pyttsx3
from time import ctime
from gtts import gTTS
import datetime
r = sr.Recognizer()
print(ctime())
def record_audio(ask = False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en-us")
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('sorry my service is down right now')
        return voice_data

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    
    audio_file = 'audio' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def wishMe():
    hour = int(datetime.datetime.now().hour) #get The Time Now 
    if hour>= 0 and hour<12:
        speak("Good Morning Youssef !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Youssef !")  
  
    else:
        speak("Good Evening Youssef !") 
        
xxx=wishMe()
  
def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Nemo ')
        
    if 'What is the time' in voice_data:
        
        speak(time.ctime())
        
        
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('here is what I found for ' + search)
        
    if 'find location' in voice_data:
        location = record_audio('whast is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('here is the location of ' + location)
        
    if 'open desktop' in voice_data:
        os.startfile("C:/Users/Youssef/Desktop")
  
    if 'you can go to sleep now' in voice_data:
        speak('bye bye')
        exit()

time.sleep(1)
while 1:  
    speak('How can I help you?')
    voice_data = record_audio()
    respond(voice_data)