import os


def check_duplicates1(file_path):
    # Provide your solution here
    flag = False

    if not os.path.exists(file_path):
        print('File does not exist')

    try:
        count = 0

        with open(file_path, 'r', encoding='ISO-8859-1') as f:

            records = f.readlines()

            records = list(map(lambda x: x.strip(), records))

            length = len(records)

            for i in range(length):
                if count == 25:
                    break

                for j in range(i + 1, length):
                    if records[i] == records[j]:
                        print("record match at postions " + str(i) + " and " + str(j) + " with values " + str(
                            records[i]) + " and " + str(records[j]))
                        flag = True

                count += 1



    except Exception as e:
        print(f"Error: {e}")
        return False

    if flag:
        return print('There are duplicate records')
    else:
        return print('There are no duplicate records')


if __name__ == "__main__":
    file_path = "rockyou.txt"
    check_duplicates1(file_path)
