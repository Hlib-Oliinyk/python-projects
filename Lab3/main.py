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
        text = input("Введіть текст українською: ").strip()
        if not re.search(r"[А-Яа-яЇїІіЄєҐґ]", text):
            print("Текст має містити лише українські літери")
            continue

        search = input("Введіть слово для пошуку: ").strip()
        if not re.fullmatch(r"[А-Яа-яЇїІіЄєҐґ'-]+", search):
            print("Слово має бути українське")
            continue

        words = re.findall(r"[А-Яа-яЇїІіЄєҐґ'-]+", text.lower())
        print(f"Слово '{search}' зустрічається {sum(1 for w in words if w == search.lower())}")
        break

def task4():
    while True:
        text = input("Введіть український текст (до 1000 слів): ").strip()
        if not re.search(r"[А-Яа-яЇїІіЄєҐґ]", text):
            print("Текст має містити лише українські літери")
            continue

        words = re.findall(r"[А-Яа-яЇїІіЄєҐґ'-]+", text)
        if len(words) > 1000:
            print("Кількість слів більше 1000")
            continue

        mid = len(words) // 2
        first_half = [w.capitalize() for w in words[:mid]]
        second_half = [w.lower() + "*" for w in words[mid:]]
        print(" ".join(first_half) + " | " + " ".join(second_half))
        break

def task5():
    while True:
        text = input("Введіть текст англійською: ").strip()
        if not re.search(r"[A-Za-z]", text):
            print("Текст має бути англійською")
            continue

        words = re.findall(r"[A-Za-z'-]+", text)
        if len(words) > 1000:
            print("Текст не має бути більше 100 слів")
            continue

        n = input("Введіть літеру N: ").strip()
        p = input("Введіть літеру P: ").strip()
        if not (len(n) == 1 and len(p) == 1 and n.isalpha() and p.isascii()):
            print("Літери мають бути англійськими")
            continue

        n, p = n.lower(), p.lower()
        start_n = [w for w in words if w.lower().startswith(n)]
        end_p = [w for w in words if w.lower().endswith(p)]

        print(f"Починаються з '{n}': {start_n}")
        print(f"Закінчуються на '{p}': {end_p}")
        break

def task6():
    vowels = "aeiou"
    while True:
        text = input("Введіть англійський текст: ").strip()
        if not re.search(r"[A-Za-z]", text):
            print("Текст має бути англійською")
            continue

        words = re.findall(r"[A-Za-z'-]+", text)
        if len(words) > 100:
            print("Текст не має бути більше 100 слів")
            continue

        count = sum(1 for ch in text.lower() if ch in vowels)
        print(f"Голосні: {count}")
        break

def task7():
    while True:
        text = input("Введіть текст англійською: ").strip()
        if not re.search(r"[A-Za-z]", text):
            print("Текст має бути англійською")
            continue

        words = re.findall(r"[A-Za-z'-]+", text)
        if len(words) > 1000:
            print("Текст не має бути більше 1000 слів")
            continue

        proper = [w for w in words if w[0].isupper()]
        print(f"З великої літери: {proper}")
        break

# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
task7()