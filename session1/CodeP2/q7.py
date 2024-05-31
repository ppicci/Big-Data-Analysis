import os
import time


def search_password(file_path, target_password):
    # Provide your solution here
    if not os.path.exists(file_path):
        print('File does not exist')
        return False

    try:
        with open(file_path, 'r', encoding= 'ISO-8859-1') as f:
            if target_password in f.read():
                return True

    except Exception as e:
        print(f"Error: {e}")
        return False

    return False


if __name__ == "__main__":
    file_path = input("Enter the path to the password file: ")
    target_password = input("Enter the password to search for: ")

    start_time = time.time()

    found = search_password(file_path, target_password)
    if found:
        print("Password found.")
    else:
        print("Password not found.")

    print("Time Taken: %s seconds " % (time.time() - start_time))