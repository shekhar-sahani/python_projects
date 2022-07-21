import wolframalpha
import wikipedia
import pyttsx3
from gtts import gTTS
import playsound
import speech_recognition as sr


client = wolframalpha.Client('PLHV99-9H9764Y5VX')
engine = pyttsx3.init()

import PySimpleGUI as sg


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    print('enter')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Exception: ' + str(e))
    return said



sg.theme('LightGreen')   # Add a touch of color
# All the stuff inside your window.
layout = [ [sg.Text('Enter a command'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Gamora', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        sg.PopupNonBlocking("Wolfram Results: " + wolfram_res , "Wikipedia Results: " + wiki_res )
        speak(wolfram_res)
        get_audio()
        print("enterd in both")
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        # engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
        speak(wolfram_res)
        get_audio()
        print('entered in error 1')
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        # engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
        speak(wolfram_res)
        get_audio()
        print('entered in error 2')
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        # engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)
        speak(wiki_res)
        get_audio()
        print('entered in wikipedia')

    print('values', values[0])
    
window.close()
