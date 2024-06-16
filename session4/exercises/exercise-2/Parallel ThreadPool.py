from Scripts import *
import time
import concurrent.futures
def parallel_threadpool_runner():
    data =file_parser('data_small.txt')

    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(conversion_getter,data)

    end = time.perf_counter()
    print(f'Parallel(Threadpool): {end - start} second(s)')

if __name__ == '__main__':
    parallel_threadpool_runner()