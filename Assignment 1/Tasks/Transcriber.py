from pathlib import Path
import speech_recognition as sr
import time
import multiprocessing

def transcribe(file):
    input_path = f"Audio/{file.stem}/{file.stem}.wav"
    recognizer = sr.Recognizer()
    with sr.AudioFile(input_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        text = "Transcription failed"
    except sr.UnknownValueError: #Tries again once accounting for ambient noise
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
        except:
            print("Google Speech Recognition could not understand audio")
            text = "Transcription failed"


    name= Path(file).stem
    output_path = f"Transcriptions/{name}/{name}.txt"
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as file:
         file.write(text)
    print(f'Text has been written to {output_path}')

def serial_runner():
    folder = Path("Audio")
    start =time.perf_counter()
    for file in folder.rglob('*.wav'):
        transcribe(file)
    end = time.perf_counter()
    print("\nSerial Transcription:")
    print(f"Finished in {end - start:.2f} seconds\n")

def multiprocess_runner():
    folder = Path("Audio")
    start = time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(transcribe, folder.rglob('*.wav'))
    end = time.perf_counter()
    print("\nMultiprocess Transcription:")
    print(f"Finished in {end - start:.2f} seconds\n")


if __name__ == '__main__':
    #serial_runner()#193.25s
    multiprocess_runner()#60.12

