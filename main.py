from voice_to_text import voice_to_text
from gpt_response import gpt_response
from text_to_voice import text_to_voice

def main():
    while True:
        # Step 1: Convert voice to text
        user_text = voice_to_text()
        
        # Step 2: Get response from GPT-3
        ai_response = gpt_response(user_text)
        print(f"ai > {ai_response}")
        
        # Step 3: Convert text to voice
        text_to_voice(ai_response)
        
if __name__ == "__main__":
    main()
