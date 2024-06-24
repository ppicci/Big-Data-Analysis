from pathlib import Path
import spacy, nltk
from nrclex import NRCLex
import time
import multiprocessing
import threading

nlp = spacy.load('en_core_web_sm')
nltk.download('punkt')
def emotion_analyser(file):


    with open(file, 'r') as f:
        text = f.read()

    # print(text)

    doc = nlp(text)

    full_text = ' '.join([sent.text for sent in doc.sents])

    emotion = NRCLex(text)
    # print(translation.text)
    name = Path(file).stem
    # print(name)
    output_path = f"Emotions/{name}/{name}.txt"
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as file:
        file.write(str(emotion.affect_frequencies))
    print(f'Text has been written to {output_path}')


def serial_runner():
    folder = Path("Transcriptions")
    start = time.perf_counter()
    for file in folder.rglob("*.txt"):
        # print(file)
        emotion_analyser(file)
    end = time.perf_counter()
    print("\nSerial Emotion Analysis:")
    print(f"Finished in {end - start:.2f} seconds\n")


def multiprocess_runner():
    folder = Path("Transcriptions")
    start = time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(emotion_analyser, folder.rglob("*.txt"))
    end = time.perf_counter()
    print("\nMultiprocess Emotion Analysis:")
    print(f"Finished in {end - start:.2f} seconds\n")


def thread_runner():
    folder = Path("Transcriptions")
    threads = []
    start = time.perf_counter()
    for file in folder.rglob("*.txt"):
        t = threading.Thread(target=emotion_analyser, args=(file,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.perf_counter()
    print("\nThread Emotion Analysis:")
    print(f"Finished in {end - start:.2f} seconds\n")


if __name__ == '__main__':
    serial_runner()#-Fastest - 0.07s
    multiprocess_runner()#4.51s
    thread_runner()#0.10s
