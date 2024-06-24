import concurrent.futures
import multiprocessing
import threading
import time
import logging
from pathlib import Path
from pytube import YouTube

# Logging set up
Path("Logs").mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename='../Tasks/Logs/Download Log.txt', level=logging.INFO,
                    format='"Timestamp": %(asctime)s, %(message)s', datefmt='%H:%M, %d %B %Y')


download_semaphore = threading.Semaphore(5)
log_mutex = threading.Lock()


def url_loader(filename):
    """
    Load URLs from a file into a list.

    Args:
        filename (str): The path to the file containing video URLs.

    Returns:
        list: A list of video URLs.
    """
    video_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            url = line.strip()
            video_list.append(url)
    return video_list


def logger(url, download):
    """
    Log the download status of a video URL.

    Args:
        url (str): The video URL.
        download (bool): The download status.
    """
    with log_mutex:
        logging.info(f'"URL":"{url}", "Download":{download}')


def yt_downloader(url):
    """
    Download a YouTube video and log the result.

    Args:
        url (str): The URL of the YouTube video to download.
    """
    yt = YouTube(url)

    with download_semaphore:
        try:
            stream = yt.streams.get_highest_resolution()
            print(f"Downloading video: {yt.title}")
            output_dir = Path("Videos")
            output_dir.mkdir(parents=True, exist_ok=True)
            stream.download(output_path=output_dir)
            print(f"Download completed: {yt.title}")
            download = True
        except Exception as e:
            print(f"Download failed: {yt.title}. Error: {e}")
            download = False
        finally:
            logger(url, download)


def serial_runner(filename):
    """
    Download videos serially from URLs in the given file.

    Args:
        filename (str): The path to the file containing video URLs.
    """
    video_list = url_loader(filename)
    start = time.perf_counter()
    for url in video_list:
        yt_downloader(url)
    end = time.perf_counter()
    print("\nSerial download:")
    print(f"Finished in {end - start:.2f} seconds\n")


def parallel_thread_runner(filename):
    """
    Download videos in parallel using threads from URLs in the given file.

    Args:
        filename (str): The path to the file containing video URLs.
    """
    video_list = url_loader(filename)
    start = time.perf_counter()
    threads = []
    for url in video_list:
        t = threading.Thread(target=yt_downloader, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.perf_counter()
    print("\nParallel download with threads:")
    print(f"Finished in {end - start:.2f} seconds\n")


def parallel_threadpool_runner(filename):
    """
    Download videos in parallel using a thread pool from URLs in the given file.

    Args:
        filename (str): The path to the file containing video URLs.
    """
    video_list = url_loader(filename)
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(yt_downloader, video_list)
    end = time.perf_counter()
    print("\nParallel download with thread pool:")
    print(f"Finished in {end - start:.2f} seconds\n")

def parallel_multiprocess_runner(filename):
    """
    Download videos in parallel using multiprocessing from URLs in the given file.

    Args:
        filename (str): The path to the file containing video URLs.
    """
    video_list = url_loader(filename)
    start = time.perf_counter()
    with multiprocessing.Pool(processes=5) as executor:
        executor.map(yt_downloader, video_list)
    end = time.perf_counter()
    print("\nParallel download with multiprocess pool:")
    print(f"Finished in {end - start:.2f} seconds\n")


if __name__ == '__main__':
    filename = "Input/Video Urls.txt"

    serial_runner(filename)#15.90s
    parallel_thread_runner(filename) #7.28s
    parallel_threadpool_runner(filename)#7.57s
    parallel_multiprocess_runner(filename)#fastest -7.03s
