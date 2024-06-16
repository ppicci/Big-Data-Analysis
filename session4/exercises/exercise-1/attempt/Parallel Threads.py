import threading
import time

from Scripts import *
def parallel_thread_runner():

    urls = file_opener("image_urls_small.txt")
    start = time.perf_counter()

    threads = []
    for url in urls:
        t = threading.Thread(target=photo_downloader, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f'Parallel(Threads): {end - start} second(s)')

if __name__ == '__main__':
    parallel_thread_runner()