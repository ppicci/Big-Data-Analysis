import time
import multiprocessing
import random

def foo():
    time.sleep(1)

def generate_and_sort_numbers():
    rand_list = []
    for i in range(10000):
        rand_list.append(random.uniform(0, 100))
    bubble_sort(rand_list)
    return rand_list


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Serial runner
def serial_runner():
    start = time.perf_counter()
    for i in range(3):
        #foo()
        generate_and_sort_numbers()
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

# Parallel runner
def parallel_runner():
    start = time.perf_counter()
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=generate_and_sort_numbers) #foo
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end = time.perf_counter()
    print(f'Parallel: {end - start} second(s)')


if __name__ == '__main__':
    serial_runner()
    parallel_runner()