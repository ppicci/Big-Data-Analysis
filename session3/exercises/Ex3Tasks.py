import multiprocessing
import time
import concurrent

def sum_square(number):
    total = 0
    for i in range(1,number):
        total= total+i**2
    return total

def serial_runner():
    start = time.perf_counter()
    for i in range(20000):
        sum = sum_square(i)
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

def parallel_runner():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(sum_square, range(20000))
    end = time.perf_counter()
    print(f'Parallel: {end - start} second(s)')

if __name__ == '__main__':
    serial_runner()
    parallel_runner()