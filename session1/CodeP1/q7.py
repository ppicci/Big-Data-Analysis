def sum_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 50, 60, 80, 90, 100]
    print(sum_elements(data))
