from Scripts import *

def parallel_threads_runner():
    thread_ids = [0, 1, 2, 3]

    threads = []

    start = time.perf_counter()

    for thread_id in thread_ids:
        thread = threading.Thread(target=editor, args=(thread_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.perf_counter()
    print(f'Parallel(Threads): {end - start} second(s)')


if __name__ == "__main__":
    parallel_threads_runner()
