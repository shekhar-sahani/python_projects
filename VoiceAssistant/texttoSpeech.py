from gtts import gTTS
import playsound
import speech_recognition as sr




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

speak('Hello everybody and welcome back')
get_audio()
