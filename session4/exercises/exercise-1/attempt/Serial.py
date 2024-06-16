import time
from Scripts import *
def serial_runner():

    urls = file_opener("image_urls_small.txt")
    start = time.perf_counter()
    for url in urls:
        photo_downloader(url)
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

if __name__ == '__main__':
    serial_runner()