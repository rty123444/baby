from gtts import gTTS
from playsound import playsound

def text_to_voice(text):
    tts = gTTS(text=text, lang='zh-tw')
    tts.save("output.mp3")
    playsound("output.mp3")

