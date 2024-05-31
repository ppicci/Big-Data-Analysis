import os


def check_duplicates2(file_path):
    # Provide your solution here
    flag = False

    if not os.path.exists(file_path):
        print('File does not exist')

    try:
        count = 0
        recordSet = set()

        with open(file_path, 'r', encoding='ISO-8859-1') as f:

            records = f.readlines()

            records = list(map(lambda x: x.strip(), records))

            length = len(records)

            for i in range(length):
                if count == 25:
                    break

                for j in range(i + 1, length):
                    if records[i] == records[j]:
                        recordSet.add(records[i])
                        flag = True

                count += 1



    except Exception as e:
        print(f"Error: {e}")
        return False

    if flag:
        return print('There are duplicate records of:' + str(recordSet))
    else:
        return print('There are no duplicate records')


if __name__ == "__main__":
    file_path = "rockyou.txt"
    check_duplicates2(file_path)
