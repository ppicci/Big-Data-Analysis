import concurrent.futures
import time

from Scripts import *
def parallel_threadpool_runner():

    urls = file_opener("image_urls_small.txt")

    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(photo_downloader,urls)

    end = time.perf_counter()
    print(f'Parallel(Threadpool): {end - start} second(s)')

if __name__ == '__main__':
    parallel_threadpool_runner()