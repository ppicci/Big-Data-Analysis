from pathlib import Path
from googletrans import Translator
import time
import multiprocessing
import threading


def translate(file):
    with open(file, 'r') as f:
        text = f.read()

    # print(text)

    translator = Translator()

    translation = translator.translate(text, src='en', dest='it')
    # print(translation.text)
    name = Path(file).stem
    # print(name)
    output_path = f"Translations/{name}/{name}.txt"
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as file:
        file.write("Text in Italian: "+str(translation.text))
    print(f'Text has been written to {output_path}')


def serial_runner():
    folder = Path("Transcriptions")
    start = time.perf_counter()
    for file in folder.rglob("*.txt"):
        # print(file)
        translate(file)
    end = time.perf_counter()
    print("\nSerial Translation:")
    print(f"Finished in {end - start:.2f} seconds\n")


def multiprocess_runner():
    folder = Path("Transcriptions")
    start = time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(translate, folder.rglob("*.txt"))
    end = time.perf_counter()
    print("\nMultiprocess Translation:")
    print(f"Finished in {end - start:.2f} seconds\n")


def thread_runner():
    folder = Path("Transcriptions")
    threads = []
    start = time.perf_counter()
    for file in folder.rglob("*.txt"):
        t = threading.Thread(target=translate, args=(file,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.perf_counter()
    print("\nThreads Translation:")
    print(f"Finished in {end - start:.2f} seconds\n")


if __name__ == "__main__":
    serial_runner()#1.71s
    multiprocess_runner()#1.06s
    thread_runner()#Fastest - 0.25s
