from Scripts import *
import concurrent.futures

def parallel_threadpool_runner():
    data = conversion_requests

    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(thread_printer,data)

    end = time.perf_counter()
    print(f'Parallel(Threadpool): {end - start} second(s)')

if __name__ == '__main__':
    parallel_threadpool_runner()