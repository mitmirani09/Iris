import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests
import wolframalpha


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

def GoogleSearch(query):
    query = query.replace("iris","")
    query = query.replace("what is","")
    query = query.replace("google search","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace("who is","")
    query = query.replace("what do you mean by","")

    writeab = str(query)

    oooooo = open('F:\\code\\VS code\\Advance Iris\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()

    Query = str(query)

    
      
    pywhatkit.search(Query)



   # os.startfile('F:\\code\\VS code\\Advance Iris\\DataBase\\extrapro\\start.py')

    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        Speak(how_to_func[0].summary)

    else:

        search = wikipedia.summary(Query,2)

        Speak(f": According To Your Search : {search}")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You .")

#def Alarm(query):

 #   TimeHere =  open('F:\\code\\VS code\\Advance Iris\\Data.txt','a')
 #   TimeHere.close()
 #   

  #  RingerNow()

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=811,y=52)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('F:\\code\\VS code\\Advance Iris\\DataBase\\Youtube\\')


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('F:\\code\\VS code\\Advance Iris\\DataBase\\Youtube\\')

def SpeedTest():
    
    Speak("I Am Checking Speed Sir , Wait For A While .")

    import speedtest

    speed = speedtest.Speedtest()

    upload = speed.upload()

    correct_Up = int(int(upload)/800000)

    download = speed.download()

    correct_down = int(int(download)/800000)

    Speak(f"Downloading Speed Is {correct_down} M B Per Second .")
    Speak(f"Uploading Speed Is {correct_Up} M B Per Second .")



def WolfRam(query):

    api_key = "E93LU8-3TTAVE8W3V"

    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        Answer = next(requested.results).text

        return Answer

    except:
        Speak("Data Not Found for your search")

def Calculator(query):

    Term = str(query)
    Term = Term.replace("iris","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("into","*")
    Term = Term.replace("divided by","/")
    Term = Term.replace("divided","/")

    Final = str(Term)

    try:
        result = WolfRam(Final)
        Speak(f"{result}")

    except:
        Speak("Data Not Found For Your Search")

def Temp(query):

    temp = str(query)
    temp = temp.replace("iris","")
    temp = temp.replace("temperature","")
    temp = temp.replace("in","")
    temp = temp.replace("what is the","")

    temp_query = str(temp)

    if 'outside' in temp_query:
        var1 = "Temperature in Mumbai"

        answer = WolfRam(var1)

        Speak(f"{var1} Is {answer} .")

    else:
        var2 = "Temperature In " + temp_query

        answ = WolfRam(var2)

        Speak(f"{var2} Is {answ}")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def My_Location():

    op = "https://www.google.com/maps/place/Shiv+Sai+Paradise,+Majiwada+Village+Rd,+Samata+Nagar,+Sainath+Nagar,+Majiwada,+Thane,+Maharashtra+400601/@19.2156914,72.9804523,17z/data=!3m1!4b1!4m5!3m4!1s0x3be7b94f4ae1a487:0x3f2a4ba25c6ceb20!8m2!3d19.2156863!4d72.982641"

    Speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"You Are Now In {state , country} .")

def CoronaVirus(Country):

    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovored = Data

    Speak(f"Cases : {cases}")
    Speak(f"Deaths : {Death}")
    Speak(f"Recovered : {recovored}")
    












