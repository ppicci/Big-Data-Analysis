def reverse1(data):
    reverse = []
    for i in range(len(data) - 1, -1, -1):
        reverse.append(data[i])
    return reverse


def reverse2(data):
    left, right = 0, len(data) - 1
    while left < right:
        # Swap the elements at the left and right indices
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1
    return data


if __name__ == "__main__":
    print(reverse1([1, 2, 3, 4, 5]))
    print(reverse2([1, 2, 3, 4, 5]))
