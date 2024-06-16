from Scripts import *
import concurrent.futures

def parallel_threadpool_runner():
    thread_ids = [0, 1, 2, 3]

    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(editor, thread_ids)

    end = time.perf_counter()
    print(f'Parallel(Threads): {end - start} second(s)')


if __name__ == "__main__":
    parallel_threadpool_runner()