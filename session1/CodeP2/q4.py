def count_pass(file_path):
    # Provide your Python script here
    try:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:

            passNo = len(file.readlines())
            return passNo
    except Exception as e:
        print(f"Error: {e}")
        return -1


## Use the following main
if __name__ == "__main__":
    print(count_pass('rockyou.txt'))
