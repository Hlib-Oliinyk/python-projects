import os

curr_dic = os.getcwd()

def task1():
    sum = 0
    dic_task1 = os.path.join(curr_dic, 'file for task 1')
    file_path = os.path.join(dic_task1, 'numbers.txt')
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            try:
                num = int(line)
                sum += num
            except ValueError:
                continue
    file_sum_path = os.path.join(dic_task1, 'sum_numbers.txt')
    with open(file_sum_path, "w") as f:
        f.write(str(sum))
    print(sum)


def task2():
    dic_task2 = os.path.join(curr_dic, 'file for task 2')
    file_path = os.path.join(dic_task2, 'num.txt')

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding='utf-8') as f:
            f.write('')

    def add_numbers():
        numbers_input = input("Введіть цілі числа через пробіл: ").strip()
        numbers = numbers_input.split()
        valid_numbers = []

        for num in numbers:
            try:
                valid_numbers.append(int(num))
            except ValueError:
                continue

        with open(file_path, "w", encoding='utf-8') as f:
            for num in valid_numbers:
                f.write(f"{num}\n")

    def paired():
        result_path = os.path.join(dic_task2, 'parity.txt')

        with open(file_path, "r", encoding='utf-8') as f:
            numbers = f.readlines()

        with open(result_path, "w", encoding='utf-8') as f:
            for line in numbers:
                try:
                    num = int(line.strip())
                    if num % 2 == 0:
                        f.write(f"{num} - парне\n")
                    else:
                        f.write(f"{num} - непарне\n")
                except ValueError:
                    continue
    add_numbers()
    paired()


def task3():
    dic_task3 = os.path.join(curr_dic, 'file for task 3')
    file_path = os.path.join(dic_task3, 'learning_python.txt')

    python_opportunities = []
    prefix = "Python можна використати для"

    with open(file_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith(prefix):
                python_opportunities.append(line)
                print(f"{line}")
            else:
                print(f"Помилка введення")

    python_opportunities.sort(key=len, reverse=True)

    print("Відсортовані рядки:")
    for line in python_opportunities:
        print(line)


def task4():
    dic_task3 = os.path.join(curr_dic, 'file for task 3')
    file_path = os.path.join(dic_task3, 'learning_python.txt')

    dic_task4 = os.path.join(curr_dic, 'file for task 4')
    if not os.path.exists(dic_task4):
        os.makedirs(dic_task4)

    true_path = os.path.join(dic_task4, 'true_statements.txt')
    false_path = os.path.join(dic_task4, 'false_statements.txt')

    language = input("Введіть мову програмування замість Python: ").strip()

    with open(true_path, "w", encoding='utf-8') as f:
        f.write('')
    with open(false_path, "w", encoding='utf-8') as f:
        f.write('')

    true_statements = []
    false_statements = []

    with open(file_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line.startswith("Python можна використати для"):
                modified_line = line.replace("Python", language)

                print(f"\nОригінал: {line}")
                print(f"Змінено: {modified_line}")

                while True:
                    answer = input(f"Це актуально для {language}? (так/ні): ").strip().lower()
                    if answer in ['так', 'ні', 'y', 'n']:
                        break
                    print("Введіть 'так' або 'ні'")

                if answer in ['так', 'y']:
                    true_statements.append(modified_line)
                else:
                    false_statements.append(modified_line)

    with open(true_path, "w", encoding='utf-8') as f:
        for line in true_statements:
            f.write(f"{line}\n")

    with open(false_path, "w", encoding='utf-8') as f:
        for line in false_statements:
            f.write(f"{line}\n")

    print("Істинні твердження")
    with open(true_path, "r", encoding='utf-8') as f:
        print(f.read())
    print("Хибні твердження")
    with open(false_path, "r", encoding='utf-8') as f:
        print(f.read())

def main():
    while True:
        try:
            choice = int(input("Виберіть номер функції (0 - вихід): "))
            match choice:
                case 0:
                    break
                case 1:
                    task1()
                case 2:
                    task2()
                case 3:
                    task3()
                case 4:
                    task4()
                case _:
                    print("Функції з таким номером не має")
        except ValueError:
            print("Ви ввели не число")

if __name__ == "__main__":
    main()