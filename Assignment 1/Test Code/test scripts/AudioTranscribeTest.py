from pathlib import Path
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.AudioFile("../output/test_audio/Me at the zoo.wav") as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.record(source)
text = recognizer.recognize_google(audio)
print(text)

file_path = '../output/test_transcribe/Me at the zoo.txt'
Path(file_path).parent.mkdir(parents=True, exist_ok=True)

with open(file_path, 'w') as file:
     file.write(text)
print(f'Text has been written to {file_path}')
