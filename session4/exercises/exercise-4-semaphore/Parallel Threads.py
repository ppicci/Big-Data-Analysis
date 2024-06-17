from Scripts import *

def parallel_thread_runner():
    data = conversion_requests
    start = time.perf_counter()
    threads=[]
    for i in data:
        t = threading.Thread(target=thread_printer, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.perf_counter()
    print(f'Parallel(Threads & Semaphore): {end - start} second(s)')


if __name__ == '__main__':
    parallel_thread_runner()