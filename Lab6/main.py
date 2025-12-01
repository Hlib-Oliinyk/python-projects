import os
from datetime import datetime
import time
import re
import csv
from collections import Counter, defaultdict

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

    while not language:
        print("Поле не може бути порожнім")
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


def task5():
    dic_task5 = os.path.join(curr_dic, 'file for task 5')
    if not os.path.exists(dic_task5):
        os.makedirs(dic_task5)

    file_path = os.path.join(dic_task5, 'guest_book.txt')

    file_exists = os.path.exists(file_path)
    creation_time = datetime.fromtimestamp(os.path.getctime(file_path)) if file_exists else datetime.now()

    if not file_exists:
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(f"Гостьова книга створена: {creation_time.strftime('%d.%m.%Y %H:%M:%S')}\n")

    def is_valid_name(name):
        for char in name:
            if not (char.isalpha() or char in [' ', '-', "'"]):
                return False
        return True

    print("Введіть 'вихід' для завершення\n")

    while True:
        name = input("Введіть ваше ім'я: ").strip()

        if name.lower() == 'вихід':
            break

        if not name:
            print("Ім'я не може бути порожнім\n")
            continue

        if not is_valid_name(name):
            print("Помилка в введенні імені\n")
            continue

        current_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        greeting = f"Вітаємо, {name}! Дякуємо за візит [{current_time}]"

        print(f"\n{greeting}\n")

        with open(file_path, "a", encoding='utf-8') as f:
            f.write(f"{greeting}\n")

    last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%d.%m.%Y %H:%M:%S')

    with open(file_path, "a", encoding='utf-8') as f:
        f.write(f"Останні внесені зміни: {last_modified}\n")


def task6():
    dic_task6 = os.path.join(curr_dic, 'file for task 6')
    if not os.path.exists(dic_task6):
        os.makedirs(dic_task6)

    file_path = os.path.join(dic_task6, 'python_article.txt')
    result_path = os.path.join(dic_task6, 'analysis_result.txt')

    start_time = time.time()
    start_datetime = datetime.now().strftime('%d.%m.%Y %H:%M:%S')

    with open(file_path, "r", encoding='utf-8') as f:
        text = f.read()

    word_count = len(text.split())
    if word_count > 3000:
        print("Текст не може бути більше 3000 слів")
        return

    letter_count = sum(1 for char in text if char.isalpha())
    if letter_count == 0:
        print("Текст не містить букв")
        return

    english_letter_count = sum(1 for char in text if char.isalpha() and ord(char) < 128)
    if english_letter_count == 0:
        print("Текст не містить англійських букв")
        return

    text_lower = text.lower()

    choice = None
    while choice not in ["1", "2", "3"]:
        print("Виберіть режим аналізу:")
        print("1 - Частота літер")
        print("2 - Частота слів (всі)")
        print("3 - Частота слів (повторилось 2+ рази)")
        choice = input("Введіть 1, 2 або 3: ").strip()

        if choice not in ["1", "2", "3"]:
            print("Невірний вибір\n")

    if choice == "1":
        letter_freq = {}
        for char in text_lower:
            if char.isalpha():
                letter_freq[char] = letter_freq.get(char, 0) + 1

        sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
        title = "Частота літер у тексті"
        result_data = sorted_freq

    elif choice == "2":
        words = text_lower.split()
        word_freq = {}
        for word in words:
            word = re.sub(r'[^a-z]', '', word)
            if len(word) >= 2:
                word_freq[word] = word_freq.get(word, 0) + 1
        sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        title = "Частота всіх англійських слів у тексті (мін. 2 символи)"
        result_data = sorted_freq

    elif choice == "3":
        words = text_lower.split()
        word_freq = {}
        for word in words:
            word = re.sub(r'[^a-z]', '', word)
            if len(word) >= 2:
                word_freq[word] = word_freq.get(word, 0) + 1

        sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        sorted_freq = [item for item in sorted_freq if item[1] >= 2]
        title = "Частота англійських слів у тексті (повторилось 2+ рази)"
        result_data = sorted_freq

    end_time = time.time()
    execution_time = round(end_time - start_time, 3)
    last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%d.%m.%Y %H:%M:%S')

    print(f"\n{title}")

    for item, count in result_data:
        print(f"{item} - {count} разів")

    with open(result_path, "w", encoding='utf-8') as f:
        f.write(f"Аналіз тексту\n")
        f.write(f"Час створення результату: {start_datetime}\n")
        f.write(f"Час останніх змін вихідного файлу: {last_modified}\n")
        f.write(f"Час виконання аналізу: {execution_time} сек\n")
        f.write(f"{title}\n")

        for item, count in result_data:
            f.write(f"{item} - {count} разів\n")

    print(f"\nЧас виконання: {execution_time} сек")


def task7():
    dic_task7 = os.path.join(curr_dic, 'file for task 7')
    if not os.path.exists(dic_task7):
        os.makedirs(dic_task7)

    file_path = os.path.join(dic_task7, 'marks2.lab11.csv')
    result_path = os.path.join(dic_task7, 'statistics.txt')

    students_data = []
    all_marks = []
    question_stats = defaultdict(lambda: {'correct': 0, 'total': 0})
    time_marks = []

    try:
        with open(file_path, "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            for row_num, row in enumerate(reader, 1):
                if len(row) < 5:
                    continue

                try:
                    student_id = row[0]
                    time_str = row[3]
                    mark_str = row[4].replace(',', '.')

                    if mark_str.strip() == '-' or mark_str.strip() == '':
                        continue

                    mark = float(mark_str)

                    answers = []
                    for x in row[5:]:
                        x_cleaned = x.strip().replace(',', '.')
                        if x_cleaned == '-' or x_cleaned == '':
                            answers.append(0.0)
                        else:
                            answers.append(float(x_cleaned))

                    minutes = int(time_str.split()[0])

                    students_data.append({
                        'id': student_id,
                        'time': minutes,
                        'mark': mark,
                        'answers': answers
                    })

                    all_marks.append(mark)
                    time_marks.append((mark, minutes))

                    for i, answer in enumerate(answers):
                        question_stats[i]['total'] += 1
                        if answer > 0:
                            question_stats[i]['correct'] += 1

                except ValueError as e:
                    print(f"Помилка в рядку {row_num}: {e}")
                    continue

        if not students_data:
            print("Не знайдено валідних даних студентів")
            return

        student_count = len(students_data)
        mark_distribution = Counter(all_marks)

        print(f"Кількість студентів: {student_count}")
        print("\nРозподіл оцінок:")
        for mark in sorted(mark_distribution.keys()):
            count = mark_distribution[mark]
            print(f"  {mark:.2f}: {count} студентів")

        print("\nСередня оцінка за 1 хвилину:")
        if time_marks:
            min_time = min(t[1] for t in time_marks)
            max_time = max(t[1] for t in time_marks)
            for minute in range(min_time, max_time + 1):
                minute_marks = [m[0] for m in time_marks if m[1] == minute]
                if minute_marks:
                    avg_mark = sum(minute_marks) / len(minute_marks)
                    print(f"  {minute} хв: {avg_mark:.2f}")

        time_marks.sort(key=lambda x: x[0] / x[1], reverse=True)
        top_5 = time_marks[:5]

        with open(result_path, "w", encoding='utf-8') as f:
            f.write("Статистика тестування\n")

            f.write(f"Кількість студентів: {student_count}\n\n")

            f.write("Розподіл оцінок:\n")
            for mark in sorted(mark_distribution.keys()):
                count = mark_distribution[mark]
                f.write(f"  {mark:.2f}: {count} студентів\n")

            f.write("\nСтатистика по питанням\n")

            for q_num in sorted(question_stats.keys()):
                stats = question_stats[q_num]
                correct = stats['correct']
                total = stats['total']
                correct_percent = (correct / total * 100) if total > 0 else 0
                incorrect_percent = ((total - correct) / total * 100) if total > 0 else 0

                f.write(f"Питання {q_num + 1}:\n")
                f.write(f"Правильних: {correct} ({correct_percent:.1f}%)\n")
                f.write(f"Неправильних: {total - correct} ({incorrect_percent:.1f}%)\n\n")

            f.write("5 найкращих оцінок\n")

            for i, (mark, time_spent) in enumerate(top_5, 1):
                ratio = mark / time_spent
                f.write(f"{i}. Оцінка {mark:.2f} за {time_spent} хв (коефіцієнт: {ratio:.3f})\n")

    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")


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
                case 5:
                    task5()
                case 6:
                    task6()
                case 7:
                    task7()
                case _:
                    print("Функції з таким номером не має")
        except ValueError:
            print("Ви ввели не число")

if __name__ == "__main__":
    main()