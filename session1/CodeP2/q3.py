if __name__ == "__main__":
    with open('rockyou.txt', 'r', encoding='ISO-8859-1') as file:
        for line in file:
            # Strip newline and whitespace from the line
            current_password = line.strip()
            print(current_password)
            break
