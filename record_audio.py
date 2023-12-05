import sounddevice as sd
import wave
import numpy as np

def record_audio(duration=5, fs=44100, filename="output.wav"):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()  # 等待录音完成
    print("Recording finished.")

    # 将 numpy 数组转换为 PCM 字节数据
    audio_bytes = (np.iinfo(np.int16).max * audio).astype(np.int16).tobytes()

    # 保存为 WAV 文件
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(audio_bytes)


