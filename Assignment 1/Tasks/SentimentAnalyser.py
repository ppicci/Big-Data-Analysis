import threading
from pathlib import Path
from textblob import TextBlob
import time
import multiprocessing

def sentiment_analyser(file):

    with open(file, 'r') as f:
        text = f.read()

    #print(text)

    blob = TextBlob(text)
    #print(blob.sentiment)
    sentiment = blob.sentiment
    name=Path(file).stem
    #print(name)
    output_path = f"Sentiments/{name}/{name}.txt"
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as file:
         file.write(str(sentiment))
    print(f'Text has been written to {output_path}')


def serial_runner():
    folder = Path("Transcriptions")
    start = time.perf_counter()
    for file in folder.rglob("*.txt"):

        #print(file)
        sentiment_analyser(file)
    end = time.perf_counter()
    print("\nSerial Sentiment Analysis:")
    print(f"Finished in {end - start:.2f} seconds\n")

def multiprocessing_runner():
    folder = Path("Transcriptions")
    start = time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(sentiment_analyser, folder.rglob("*.txt"))
    end = time.perf_counter()
    print("\nMultiprocessing Sentiment Analysis:")
    print(f"Finished in {end - start:.2f} seconds\n")

def thread_runner():
    folder = Path("Transcriptions")
    threads= []
    start = time.perf_counter()
    for file in folder.rglob("*.txt"):
        t = threading.Thread(target=sentiment_analyser, args=(file,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.perf_counter()
    print("\nThreads Sentiment Analysis:")
    print(f"Finished in {end - start:.2f} seconds\n")


if __name__ == "__main__":
    serial_runner()#0.03s
    multiprocessing_runner()#2.27s
    thread_runner() #Fastest - 0.02s