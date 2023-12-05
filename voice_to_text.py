import sounddevice as sd
import numpy as np
import speech_recognition as sr
import wave
import io

def record_audio(duration=5, sample_rate=44100):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    return recording

def save_audio_to_wav(recording, sample_rate=44100):
    wav_io = io.BytesIO()
    with wave.open(wav_io, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(recording.tobytes())
    wav_io.seek(0)
    return wav_io

def voice_to_text(duration=5):
    recognizer = sr.Recognizer()
    audio_data = record_audio(duration)
    wav_audio = save_audio_to_wav(audio_data)

    with sr.AudioFile(wav_audio) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="zh-TW")
        return text
    except sr.UnknownValueError:
        return "无法识别语音"
    except sr.RequestError as e:
        return f"无法从 Google Web Speech API 获取结果; {e}"

if __name__ == "__main__":
    text = voice_to_text(duration=5)
    print("您说的话是： " + text)
