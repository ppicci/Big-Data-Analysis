import moviepy.editor as mp
from pathlib import Path
import time
import multiprocessing
import threading
import concurrent.futures

def audio_extractor(file):
    output_folder = Path("Audio")/file.stem
    output_folder.mkdir(parents=True, exist_ok=True)
    video = mp.VideoFileClip(f"{file}")
    video.audio.write_audiofile(f"{output_folder}/{file.stem}.wav")

def serial_runner():
    folder = Path("Videos")
    start = time.perf_counter()
    for file in folder.glob('*.mp4'):
        audio_extractor(file)
    end = time.perf_counter()
    print("\nSerial Extraction:")
    print(f"Finished in {end - start:.2f} seconds\n")

def multiprocess_runner():
    folder = Path("Videos")
    start = time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(audio_extractor, folder.glob('*.mp4'))
    end = time.perf_counter()
    print("\nMultiprocess Extraction:")
    print(f"Finished in {end - start:.2f} seconds\n")

def thread_runner():
    folder = Path("Videos")
    threads = []
    start = time.perf_counter()
    for file in folder.glob('*.mp4'):
        t= threading.Thread(target=audio_extractor, args=(file,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.perf_counter()
    print("\nThread Extraction:")
    print(f"Finished in {end - start:.2f} seconds\n")

def concurrent_runner():
    folder = Path("Videos")
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(audio_extractor, folder.glob('*.mp4'))
    end = time.perf_counter()
    print("\nConcurrent Extraction:")
    print(f"Finished in {end - start:.2f} seconds\n")

def threadpool_runner():
    folder = Path("Videos")
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(audio_extractor, folder.glob('*.mp4'))
    end = time.perf_counter()
    print("\nThread Extraction:")
    print(f"Finished in {end - start:.2f} seconds\n")


if __name__ == "__main__":
    #serial_runner() #23.17s
    multiprocess_runner() #Fastest - 8.09s
    #thread_runner() #19.40s
    #concurrent_runner() #8.25s
    #threadpool_runner() #18.92s


