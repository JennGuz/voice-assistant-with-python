from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os
import uuid 

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_text(text):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role":"user",
                "content": text
            }
        ]
    )
    return completion.choices[0].message.content

def speech_to_text(speech_path):
    audio_file = open(speech_path, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcript.text

def text_to_speech(text):
    speech_file_path = Path(__file__).parent / f"{uuid.uuid4()}.mp3"
    
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )
    
    response.stream_to_file(speech_file_path)
    
    print(f"Audio saved to: {speech_file_path}")
    return speech_file_path 
