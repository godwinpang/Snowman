import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from io import BytesIO

from pydub import AudioSegment
from pydub.playback import play
 
from subprocess import Popen
pause_apple_script = "osascript -e 'tell application "+'"iTunes"'+" to pause'"
play_apple_script = "osascript -e 'tell application "+'"iTunes"'+" to play'"
increase_vol_apple_script = 'osascript -e "set volume output volume(output volume of (get volume settings) + 1) --100%"'
decrease_vol_apple_script= 'osascript -e "set volume output volume(output volume of (get volume settings) - 1) --100%"'

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')

    mp3_fp= BytesIO()
    tts.write_to_fp(mp3_fp)

    # text = AudioSegment.from_file(mp3_fp, format='mp3')
    # play(text)
    
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
    # Uses the default API key
    # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return data
    
def jarvis(data):
    if "pause" in data:
        Popen(pause_apple_script, shell=True) # must add shell=True when adding raw string
    
    if "play" in data:
        Popen(play_apple_script, shell=True) # must add shell=True when adding raw string

    if "increase" in data:
        Popen(increase_vol_apple_script, shell=True) # must add shell=True when adding raw string
    
    if "decrease" in data:
        Popen(decrease_vol_apple_script, shell=True) # must add shell=True when adding raw string

# initialization
time.sleep(2)
speak("Hi Godwin, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)