import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)
def speak(audio):

    engine.say(audio)
    engine.runAndWait()

speak("I am aditya ke alexa please say the word whose meaning you want:")


def takecommand():
    

    r=sr.Recognizer()  
    with sr.Microphone() as source:
        print ("Listening sir")
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("running ")
        query=r.recognize_google(audio,language="en-in")
        print (f"user said: {query}")
        import json
        from difflib import get_close_matches
        data = json.load(open("C:/Users/aditya/Desktop/LifePY/Applications/APP2/data.json"))
        n=str(query)
        n=n.lower()
        print(n)
        if n in data:
           a=data[n]
           speak("The meaning is ")
           speak(a)
        elif len(get_close_matches(n,data.keys())) > 0:
           yn= input("Did you mean %s instead?  Enter Y if yes , N if no : " % get_close_matches(n,data.keys())[0])
    

           if yn=="Y":
              speak(str(data[get_close_matches(n,data.keys())[0]]))
           elif yn=="N":
               speak("The word doesn't exist.Please double check it'")
           else:
              speak("We didn't understand ur query")

    except Exception as e:
        print (e)
        print ("say that again: ")
        return "None"


# speak("aditya is a good man")

takecommand()