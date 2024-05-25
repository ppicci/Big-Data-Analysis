from itertools import permutations


def all_permutations(elements):
    return list(permutations(elements))


if __name__ == "__main__":
    elements = [1, 2, 3]
    print(all_permutations(elements))

# The script outputs:
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
