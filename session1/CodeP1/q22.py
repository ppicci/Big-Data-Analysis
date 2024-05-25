def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # // means integer division (5//2)=2 :)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    data = [10, 19, 28, 32, 45, 55, 66]
    target = 28
    print(binary_search(data, target))
