def count_characters(filename):
    count = 0
    with open(filename, 'r') as file:
        for char in file:
            count += 1

    return count


if __name__ == "__main__":
    filename = 'file1.txt'
    try:
        counts = count_characters(filename)
        print("Letter counts:", counts)
    except FileNotFoundError:
        print("File not found")
