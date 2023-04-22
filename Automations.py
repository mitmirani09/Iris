from datetime import datetime
from os import startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
from notifypy import notify
import pyttsx3
import speech_recognition as sr
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

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

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def WhatsappMsg(name,message):
     
    startfile("C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=238, y=107)

    sleep(1)

    write(name)

    sleep(2)

    click(x=188, y=249)

    sleep(1)

    click(x=851, y=1003)

    sleep(1)

    write(message)

    press('enter')

def WhatsappCall(name):

    startfile("C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=238, y=107)

    sleep(1)

    write(name)

    sleep(2)

    click(x=188, y=249)

    sleep(1)

    click(x=1766, y=62)

def WhatsappVideoCall(name):

    startfile("C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(8)

    click(x=238, y=107)

    sleep(1)

    write(name)

    sleep(2)

    click(x=188, y=249)

    sleep(1)

    click(x=1709, y=52)

def WhatsappChat(name):

    startfile("C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(4)
    press_and_release('Ctrl + f')
    sleep(4)

    write(name)
    press('enter')



def ChromeAuto(command):

    query = str(command)

    if 'new tab' in query:

        press_and_release('ctrl + t')

    elif 'close tab' in query:

        press_and_release('ctrl + w')

    elif 'new window' in query:

        press_and_release('ctrl + n')

    elif 'history' in query:

        press_and_release('ctrl + h')

    elif 'download' in query:

        press_and_release('ctrl + j')

    elif 'bookmark' in query:

        press_and_release('ctrl + d')

        press('enter')

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


def WindiowsAuto(command):

    query = str(command)

    if 'home screen' in query:

        press_and_release('windows + m')

    elif 'minimize' in query:

        press_and_release('windows + m')

    elif 'start button' in query:

        press('windows')

    elif 'open setting' in query:

        press_and_release('windows + i')

    elif 'open search' in query:

        press_and_release('windows + s')

    elif 'screen shot' in query:

        press_and_release('windows + SHIFT + s')

    elif 'restore windows' in  query:

        press_and_release('Windows + Shift + M')

    elif 'open run command' in query:

        press_and_release('windows + r')

    else:
        Speak("Sorry , No Command Found!")

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    web.open(url=Url_Place)

    location = location.raw['address']

    target = {'city is' : location.get('city',''),
                'state is' : location.get('state',''),
                'country is' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)


    Speak(target)
    Speak(f"{Place} is {distance} Kilometre Away From Your Location . ")

def Notepad():

    Speak("I Am Ready To Write .")

    writes = TakeCommand()

    time = datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","_") + "note"

    startfile("C:\\Windows\\System32\\notepad.exe")
    sleep(4)

    write(writes)
    press_and_release('Ctrl + s')
    sleep(2)
    press('backspace')
    sleep(2)
    write(filename)
    sleep(2)
    press('enter')


def CloseNotepad():

  os.system("TASKKILL /F /im Notepad.exe")


