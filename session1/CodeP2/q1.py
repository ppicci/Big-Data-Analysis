import time
from itertools import permutations


def all_permutations(elements):
    return list(permutations(elements))


if __name__ == "__main__":
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # Start the timer
    start = time.time()
    result = all_permutations(elements)
    # End the timer
    end = time.time()

    print(f'Total time to run (seconds):', round(end - start, 4))
