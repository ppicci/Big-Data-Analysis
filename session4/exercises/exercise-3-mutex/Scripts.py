from faker import Faker
import os, time, threading

# Create a Faker object to generate random phrases
faker = Faker()

file_lock = threading.Lock()

# Specify the folder and file name
folder_name = "output"
file_name = "phrases.txt"
file_path = os.path.join(folder_name, file_name)

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)


def editor(thread_id):
    # Generate a random sentence using Faker
    phrase = faker.sentence()

    time.sleep(1)

    file_lock.acquire()
    try:
        # Open the file in append mode
        with open(file_path, "a") as file:
            # Create a log entry with the generated phrase
            log_entry = f"Thread{thread_id}: {phrase}\n"

            # Write the log entry to the file
            file.write(log_entry)
            print(f"Thread {thread_id} Saved: {phrase}\n")
    finally:
        file_lock.release()
