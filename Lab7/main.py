import datetime
import os
import re

def current_work_path():
    return os.getcwd()

def dictionary_path():
    return os.path.join(current_work_path(), "file for task 2")

def file_path():
    return os.path.join(dictionary_path(), "people.csv")

class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.valid = True

        pattern = re.compile(r"^[a-zA-Zа-яА-ЯґҐєЄіІїЇʼ']+$")

        if not surname or not isinstance(surname, str) or not pattern.match(surname):
            print("Неправильно заповнене поле з прізвищем")
            self.valid = False
            return
        if not first_name or not isinstance(first_name, str) or not pattern.match(first_name):
            print("Неправильно заповнене поле з ім'ям")
            self.valid = False
            return
        try:
            year, month, day = map(int, birth_date.split('-'))
            birth_date = datetime.date(year, month, day)
        except Exception:
            print("Неправильно заповнене поле з днем народження")
            self.valid = False
            return

        self.surname = surname
        self.firstname = first_name
        self.nickname = nickname
        self.birth_date = birth_date

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return str(age)

    def get_fullname(self):
        return f"{self.firstname} {self.surname}"


def modifier(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Файл не знайдено")
        return
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return
    if not lines:
        print("Файл порожній")
        return

    headers = lines[0].strip().split(",")
    required_columns = ["surname", "name", "birth_date"]

    for col in required_columns:
        if col not in headers:
            print(f"Відсутня необхідна колонка '{col}' у файлі")
            return

    name_index = headers.index("name")
    surname_index = headers.index("surname")
    birth_date_index = headers.index("birth_date")
    nickname_index = headers.index("nickname") if "nickname" in headers else None

    output_filename = filename.replace(".csv", "_modified.csv")
    new_headers = headers[:name_index + 1] + ["fullname"] + headers[name_index + 1:] + ["age"]
    new_lines = [",".join(new_headers) + "\n"]

    valid_rows = 0
    invalid_rows = 0


    for line_num, line in enumerate(lines[1:], 2):
        data = line.strip().split(",")

        if len(data) < len(headers):
            invalid_rows += 1
            continue

        surname = data[surname_index]
        first_name = data[name_index]
        birth_date = data[birth_date_index]
        nickname = data[nickname_index] if nickname_index is not None else None

        person = Person(surname, first_name, birth_date, nickname)

        if not person.valid:
            invalid_rows += 1
            continue

        fullname = person.get_fullname()
        age = person.get_age()
        new_data = data[:name_index + 1] + [fullname] + data[name_index + 1:] + [age]
        new_lines.append(",".join(new_data) + "\n")
        valid_rows += 1


    with open(output_filename, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def task1():
    person1 = Person("Олійник", "Гліб", "2007-07-07")

    if person1.valid:
        print(person1.get_fullname())
        print(person1.get_age())

def task2():
    modifier(file_path())

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
                case _:
                    print("Функції з таким номером не має")
        except ValueError:
            print("Ви ввели не число")

if __name__ == "__main__":
    main()