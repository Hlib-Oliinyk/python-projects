from dataclasses import replace
import re

def task1():
    while True:
        text = input("Введіть текст ").strip()
        if not text or not any(l.isalpha() for l in text):
            print("Введіть хоча б одну літеру")
            continue

        search = input("Введіть слово або початок слова для пошуку ").strip()

        if not search or not any(l.isalpha() for l in search):
            print("Введіть хоча б одну літеру для пошуку")
            continue

        words = re.findall(r"[А-Яа-яЇїІіЄєҐґA-Za-z'-]+", text.lower())
        if len(words) > 1000:
            print(f"У тексті більше 1000 слів")
            continue

        search = search.lower()

        count = sum(1 for w in words if w.startswith(search))
        print(f"Кількість слів, що починаються з '{search}': {count}")
        break

def task2():
    while True:
        text = input("Введіть текст: ")
        if not any(l.isalpha() for l in text):
            print("Введіть хоча б одну літеру")
            continue

        replaced_text = text.replace('a', 'A').replace('а', 'А')
        print(f"Текст пілся заміни - {replaced_text}")

        letters = [l for l in text if l.isalpha()]
        print(f"Кількість символів - {len(text)}")
        print(f"Кількість літер - {len(letters)}")
        break

def task3():
    while True:
        text = input("Введіть текст ").strip()
        if not text or not any(l.isalpha() for l in text):
            print("Введіть хоча б одну літеру для пошуку")
            continue

        search = input("Введіть слово для пошуку ").strip()
        if not search or not any(l.isalpha() for l in search):
            print("Введіть слово для пошуку")
            continue

        words = re.findall(r"[А-Яа-яЇїІіЄєҐґ'-]+", text.lower())
        count = sum(1 for w in words if w == search.lower())

        print(f"Кількість, скільки зустрічається слово '{search}' - {count}")
        break

task1()
task2()
task3()
