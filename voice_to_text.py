import sounddevice as sd
import numpy as np
import speech_recognition as sr

def record_from_mic(duration=5, sample_rate=44100):
    print(f"錄製 {duration} 秒的音頻...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # 等待錄製完成
    return np.array(recording).flatten()

def voice_to_text(duration=5):
    recognizer = sr.Recognizer()
    audio_data = record_from_mic(duration)  # 錄製指定秒數的音頻

    # 將 numpy 數組音頻轉換為音頻數據
    audio = sr.AudioData(np.array(audio_data).tobytes(), 44100, 2)

    try:
        # 使用 Google 的 Web Speech API 進行識別
        text = recognizer.recognize_google(audio, language="zh-TW")
        return text
    except sr.UnknownValueError:
        return "無法識別語音"
    except sr.RequestError as e:
        return f"無法從 Google Web Speech API 獲取結果; {e}"

if __name__ == "__main__":
    text = voice_to_text(duration=5)
    print("您說的話是： " + text)
