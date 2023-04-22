import pyttsx3
import speech_recognition as sr
from features import GoogleSearch
from win10toast import ToastNotifier
import webbrowser as web
from keyboard import press_and_release
from keyboard import press
from pyautogui import click
from keyboard import write
from time import sleep
import pywhatkit
import os
import pyautogui
from PyDictionary import PyDictionary as Diction

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-gb')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

toast = ToastNotifier()
toast.show_toast(" Iris ","The Iris Is Now Activated",duration=8)

def TaskExe():
    Speak("Hello, I Am Iris")
    Speak("How Can I Help You ?")

    while True:

        query = TakeCommand()

        if 'google search' in query:
            GoogleSearch(query)

        elif 'hello iris' in query:
            Speak("Hello sir, I am Iris.")
            Speak("You Personal AI Assistant")
            Speak("How May I Help You")

        elif 'iris status' in query:
            Speak("Everything Is Up And Running!")

        elif 'bye' in query:
            Speak("OK Sir, You Can Call Me Any Time")
            break

        elif 'youtube search' in query:
            Query = query.replace("iris","")
            query = Query.replace("youtube search","")
            from features import YouTubeSearch
            YouTubeSearch(query)

   #     elif 'set alarm' in query:
   #         from features import Alarm
  #          Alarm(query)

        elif 'download' in query:
            from features import DownloadYouTube
            DownloadYouTube()
            
        elif 'speed test' in query:
            from features import SpeedTest
            SpeedTest()

        elif 'temperature' in query:
            from features import Temp
            Temp(query)
        
        elif 'calculate' in query:
            from features import Calculator
            Calculator(query)
        
        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("iris ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'video' in query:
            from Automations import WhatsappVideoCall
            name = query.replace("iris","")
            name = name.replace("video ","")
            name = name.replace("call","")
            Name = str(name)
            WhatsappVideoCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)
        
        elif 'launch'in query:
            Speak("Tell Me The Name Of The Website!")
            sitename = TakeCommand()
            sitename = sitename.replace(" ","")
            webrowse = 'https://' + sitename + '.com'
            web.open(webrowse)
            Speak('Done Sir')

        elif 'dictionary' in query:
            Dictionary()  

        elif 'my location' in query:

            from features import My_Location

            My_Location()

        elif 'where is' in query:

            from Automations import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("iris" , "")
            GoogleMaps(Place)

        elif 'write a note' in query:

            from Automations import Notepad

            Notepad()

        elif 'dismiss' in query:

            from Automations import CloseNotepad

            CloseNotepad()

        elif 'corona cases' in query:

            from features import CoronaVirus

            Speak("Which Country's Information ?")

            cccc = TakeCommand()

            CoronaVirus(cccc)
    
        elif 'new tab' in query:

            press_and_release('ctrl + t')

        elif 'close tab' in query:

            press_and_release('ctrl + w')

        elif 'new window' in query:

            press_and_release('ctrl + n')

        elif 'history' in query:

            press_and_release('ctrl + h')

        elif 'section' in query:

            press_and_release('ctrl + j')

        elif 'bookmark' in query:

            press_and_release('ctrl + d')
            click(x=295, y=473)

        elif 'incognito' in query:

            press_and_release('Ctrl + Shift + n')

        elif 'switch tab' in query:
            
            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to","")
            
            num = Tab

            bb = f'ctrl + {num}'

            press_and_release(bb)

        elif 'open' in query:

            name = query.replace("open ","")

            NameA = str(name)

            if 'youtube' in NameA:

                web.open("https://www.youtube.com/")

            elif 'instagram' in NameA:

                web.open("https://www.instagram.com/")

            else:

                string = "https://www." + NameA + ".com"

                string_2 = string.replace(" ","")

                web.open(string_2)

        elif 'youtube pause' in query:

            press('space bar')

        elif 'youtube resume' in query:

            press('space bar')

        elif 'full screen' in query:

            press('f')

        elif 'cinematic mode' in query:

            press('t')

        elif 'go forward' in query:

            press('l')

        elif 'go back' in query:

            press('j')

        elif 'increase playback speed' in query:

            press_and_release('SHIFT + .')

        elif 'decrease' in query:

            press_and_release('SHIFT + ,')

        elif 'previous' in query:

            press_and_release('SHIFT + p')

        elif 'next' in query:

            press_and_release('SHIFT + n')
        
        elif 'search' in query:

            click(x=867, y=99)

            Speak("What To Search Sir ?")

            search = TakeCommand()

            write(search)

            sleep(1)

            press('enter')
            Speak("This Is What I Found For Your Search .")
            pywhatkit.playonyt(search)
        
        elif 'clear' in query:

            click(x=867, y=99)
            press_and_release('Ctrl + a')
            press('backspace')

            Speak("Cleared, now you can search something else again.")

        elif 'mute' in query:

            press('m')

        elif 'unmute' in query:

            press('m')
        
        elif 'turn on captions' in query:
            press('c')

        elif 'turn off captions' in query:
            press('c')

        elif 'my channel' in query:

            web.open("https://www.youtube.com/channel/UCXZs0solIVHJrYB84Dc0INQ")

        elif 'go back to start' in query:
            press('0')

        elif 'home screen' in query:

            press_and_release('windows + m')

        elif 'minimize' in query:

            press_and_release('windows + m')

        elif 'windows settings' in query:

            press_and_release('windows + i')

        elif 'windows search' in query:

            press_and_release('windows + s')

        elif 'microsoft office' in query:

            press_and_release('windows + SHIFT + AltGr')

        elif 'notifications' in query:
            press_and_release('windows + n')

        elif 'screen shot' in query:

            Speak("Ok, What Should I Name The File?")
            path = TakeCommand()
            path1name = path + ".png"
            path1 = "F:\\code\\VS code\\Advance Iris\\DataBase\\Screenshots\\" + path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile("F:\\code\\VS code\\Advance Iris\\DataBase\\Screenshots\\")
            Speak("Here Is Your Screenshot")

            
        elif 'open run command' in query:

            press_and_release('windows + r')

        else:
            Speak("Sorry , No Command Found!")     
        
      #  else:

           # from DataBase.ChatBot.ChatBot import ChatterBot

          #  reply = ChatterBot(query)

           # Speak(reply)

          #  if 'bye' in query:

          #      break

          #  elif 'exit' in query:

          #      break

         #   elif 'go' in query:

         #       break 
def Dictionary():
        
        Speak("What you are curious about to know")
        probl = TakeCommand()

        if 'meaning' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("Iris","")
            probl = probl.replace("of","")
            probl = probl.replace("meaning","")
            result = Diction.meaning(probl)
            Speak(f"The Meaning OF The Word {probl} is {result}")
       
         

TaskExe()









