from vosk import Model, KaldiRecognizer
import os
import pyaudio

def initialize_model(model_path):
    # 检查模型路径
    if not os.path.exists(model_path):
        print("Model not found at", model_path)
        exit(1)

    # 加载模型
    return Model(model_path)

def voice_to_text(recognizer):
    # 使用 PyAudio 开始录音
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    print("请开始说话...")

    # 进行录音并识别
    while True:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    return result

if __name__ == "__main__":
    model_path = "./model/vosk-model-cn-0.22"
    model = initialize_model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    # 示例：连续进行两次语音识别
    for _ in range(2):  
        result = voice_to_text(recognizer)
        print("识别结果:", result)
