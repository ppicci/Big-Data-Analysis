from Scripts import *


def serial_runner():
    data = file_parser('data_small.txt')
    start = time.perf_counter()
    for i in data:
        conversion_getter(i)
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')


if __name__ == '__main__':
    serial_runner()
