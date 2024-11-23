from src.utils import speech_to_text, text_to_speech, generate_text
from src.printer import printer
import pyaudio
import wave
import keyboard
import uuid  
import threading 
from playsound import playsound 

def record_audio():
    file_name = f"{uuid.uuid4()}.wav"

    audio_format = pyaudio.paInt16 
    channels = 1                   
    sample_rate = 44100            
    buffer_size = 1024             

    p = pyaudio.PyAudio()

    stream = p.open(format=audio_format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=buffer_size)

    print("Press Enter to start recording...")
    keyboard.wait('enter')
    print("Recording... Press Enter again to stop.")

    frames = []
    recording = True

    def check_stop_recording():
        nonlocal recording
        keyboard.wait('enter')
        recording = False

    stop_thread = threading.Thread(target=check_stop_recording)
    stop_thread.start()

    while recording:
        data = stream.read(buffer_size)
        frames.append(data)

    stop_thread.join()

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(audio_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print(f"The audio file has been saved as: {file_name}")
    return file_name


recording_path = record_audio()
text = speech_to_text(recording_path)
message = generate_text(text)
    
audio_file = text_to_speech(message)
    
playsound(audio_file)
    
printer.bright_green(text) 
printer.blue(message)       