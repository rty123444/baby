import speech_recognition as sr

def voice_to_text():
    # 初始化語音識別器
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("請開始說話...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # 使用Google的語音識別服務
            response = recognizer.recognize_google(audio, language="zh-TW", show_all=True)
            
            # 這裡我假設 response 就是您的 result2
            result2 = response
            
            # 提取所有可能的結果
            alternatives = result2['alternative']

            # 根據信心分數排序
            sorted_alternatives = sorted(alternatives, key=lambda x: x.get('confidence', 0), reverse=True)

            # 選取信心分數最高的結果
            best_result = sorted_alternatives[0]['transcript']
            print(f'{best_result}')
            return best_result
            
        except sr.UnknownValueError:
            return "無法識別語音"
        except sr.RequestError:
            return "API 請求出錯"

#print(speech_to_text())
