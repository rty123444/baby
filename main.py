from vosk import Model, KaldiRecognizer
import os
from voice_to_text import voice_to_text
from gpt_response import gpt_response
from text_to_voice import text_to_voice

def initialize_model(model_path):
    if not os.path.exists(model_path):
        print("Model not found at", model_path)
        exit(1)
    return Model(model_path)

def main():
    model_path = "./model/vosk-model-cn-0.22"
    model = initialize_model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    while True:
        # Step 1: Convert voice to text
        user_text = voice_to_text(recognizer)
        print(f"user > {user_text}")
        
        # Step 2: Get response from GPT-3
        #ai_response = gpt_response(user_text)
        #print(f"ai > {ai_response}")
        
        # Step 3: Convert text to voice
        #text_to_voice(ai_response)

if __name__ == "__main__":
    main()
