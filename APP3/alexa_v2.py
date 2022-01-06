import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty("rate", 165)
engine.setProperty('voice', voices[1].id)
def speak(audio):

    engine.say(audio)
    engine.runAndWait()

speak("I am aditya ke alexa please say the word whose meaning you want ")

def takecommand():
    

    r=sr.Recognizer()  
    with sr.Microphone() as source:
        print ("please speak: ")
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("the application is running: ")
        query=r.recognize_google(audio,language="en-in")
        print (f"user said: {query}")
        import json
        from difflib import get_close_matches
        data = json.load(open("C://Users//aditya//Desktop//LifePY//Applications//APP3//data.json"))
        n=str(query)
        n=n.lower()
        print(n)
        if n in data:
           a=data[n]
           speak("The meaning is ")
           speak(a)
        elif len(get_close_matches(n,data.keys())) > 0:
           speak("Did you mean %s instead?  speak yes or no : " % get_close_matches(n,data.keys())[0])
           r=sr.Recognizer()  
           with sr.Microphone() as source:
               print ("please speak: ")
               r.pause_threshold=1
               audio=r.listen(source)
               print("the application is running: ")
            
               query=r.recognize_google(audio,language="en-in")
               print (f"user said: {query}")

               yn=str(query)
               yn=yn.lower()
           if yn=="yes":
              speak(str(data[get_close_matches(n,data.keys())[0]]))
           elif yn=="no":
               speak("The word doesn't exist.Please double check it'")
           else:
              speak("We didn't understand ur query")

    except Exception as e:
        print (e)
        print ("say that again: ")
        return "None"

takecommand()