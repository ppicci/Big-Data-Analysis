import threading
import logging
from pytube import YouTube

log_mutex = threading.Lock()
def basic_downloader():
    url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print(f"Downloading video: {yt.title}")
    stream.download(output_path="../output/test_video")
    print(f"Download completed: {yt.title}")
    download = True
    basic_logger(url, download)


def basic_logger(url,download):
    log_mutex.acquire()
    try:
        logging.basicConfig(filename='../output/test_video/test_log.txt', level=logging.INFO, format='"Timestamp":, %(asctime)s, %(message)s', datefmt='%H:%M, %d %B %Y')
        logging.info(f'"URL":"{url}", "Download":{download}')
    finally:
        log_mutex.release()


if __name__ == '__main__':
    basic_downloader()