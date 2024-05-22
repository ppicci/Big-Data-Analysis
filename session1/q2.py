def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 50, 60, 80, 90, 100]
    result = linear_search(data, 40)
    print(result)
