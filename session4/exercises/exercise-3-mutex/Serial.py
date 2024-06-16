from Scripts import *


def serial_runner():
    start = time.perf_counter()

    for i in range(4):
        editor(i)

    end = time.perf_counter()

    print(f'Serial runner took {end - start} seconds')

if __name__ == '__main__':
    serial_runner()
