import datetime
import os
import re

def current_work_path():
    return os.getcwd()

def dictionary_path():
    return os.path.join(current_work_path(), "file for task 2")

def file_path():
    return os.path.join(dictionary_path(), "people.txt")

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

def task1():
    person1 = Person("Олійник", "Гліб", "2007-07-07")

    if person1.valid:
        print(person1.get_fullname())
        print(person1.get_age())


def main():
    task1()

if __name__ == "__main__":
    main()