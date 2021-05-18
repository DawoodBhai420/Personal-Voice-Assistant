import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser as wb

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

greeting = 'Heyyyyyy guys. its Alina. What can I do for you'
talk(greeting)

def take_command():
    try:
        with sr.Microphone() as source:
            print('I am listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alina' in command:
                command = command.replace('alina',' ')
                print(command)
    except:
        pass
    return command


def run_alina():
    command = take_command()
    if 'play' in command:
        song = command.replace('play',' ')
        print('playing' + song)
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('current time is '+time)
    elif 'tell me about' in command:
        thing = command.replace('tell me about',' ')
        info = wikipedia.summary(thing,1)
        print(info)
        talk(info)
    elif '.com' in command:
        site = command.replace('open',' ')
        print('opening' + site)
        talk('opening' + site)
        wb.open(site)


while True:
    run_alina()


