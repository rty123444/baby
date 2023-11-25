import pyttsx3

def text_to_voice(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# 使用方法：
#text_to_voice("您想要轉換的文字")
