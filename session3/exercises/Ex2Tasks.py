import os
import requests
import re
import multiprocessing
import time

urls = [
        'http://www.gutenberg.org/files/1342/1342-0.txt',  # Pride and Prejudice by Jane Austen
        'http://www.gutenberg.org/cache/epub/11/pg11.txt',  # Alice’s Adventures in Wonderland by Lewis Carroll
        'http://www.gutenberg.org/files/84/84-0.txt',  # Frankenstein by Mary Shelley
        'http://www.gutenberg.org/files/1080/1080-0.txt',  # A Modest Proposal by Jonathan Swift
        'http://www.gutenberg.org/files/98/98-0.txt',  # A Tale of Two Cities by Charles Dickens
        'http://www.gutenberg.org/files/2701/2701-0.txt',  # Moby Dick by Herman Melville
        'http://www.gutenberg.org/files/2600/2600-0.txt',  # War and Peace by Leo Tolstoy
        'http://www.gutenberg.org/files/174/174-0.txt',  # The Picture of Dorian Gray by Oscar Wilde
        'http://www.gutenberg.org/files/43/43-0.txt',  # The Strange Case of Dr. Jekyll and Mr. Hyde by Robert Louis Stevenson
        'http://www.gutenberg.org/files/1661/1661-0.txt'  # The Adventures of Sherlock Holmes by Arthur Conan Doyle
    ]

os.makedirs('Saved Books', exist_ok=True)
def save_text_to_file(text_list, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for text in text_list:
            file.write(text + '\n')

def download_book(url):
    response = requests.get(url)
    book = response.text
    pattern = r'[^/]+$'
    match = (re.search(pattern, url))
    title = match.group(0)
    directory= os.path.join('Saved Books', title)
    save_text_to_file(book, directory)
    return book

def serial_runner():
    start = time.perf_counter()
    for url in urls:
        download_book(url)
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

def parallel_runner():
    start = time.perf_counter()
    processes = []
    for url in urls:
        p = multiprocessing.Process(target= download_book, args=[url])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end = time.perf_counter()
    print(f'Parallel: {end - start} second(s)')


if __name__ == '__main__':
    serial_runner()
    parallel_runner()