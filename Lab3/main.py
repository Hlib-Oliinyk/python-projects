import re

def task1():
    while True:
        text = input("Введіть український текст (до 1000 слів): ").strip()
        if not re.fullmatch(r"[А-Яа-яЇїІіЄєҐґ]", text):
            print("Текст має містити лише українські літери")
            continue

        search = input("Введіть слово або початок слова для пошуку українською ").strip()
        if not re.fullmatch(r"[А-Яа-яЇїІіЄєҐґ'-]+", search):
            print("Слово має бути українське")
            continue

        words = re.findall(r"[А-Яа-яЇїІіЄєҐґ'-]+", text.lower())
        if len(words) > 1000:
            print(f"У тексті більше 1000 слів")
            continue

        search = search.lower()
        count = sum(1 for w in words if w.startswith(search))
        print(f"Кількість слів, що починаються з '{search}': {count}")
        break


def task2():
    while True:
        text = input("Введіть текст: ").strip()
        if not any(l.isalpha() for l in text):
            print("Введіть хоча б одну літеру")
            continue

        replaced_text = text.replace('a', 'A').replace('а', 'А')
        print(f"Текст після заміни - {replaced_text}")

        letters = [l for l in text if l.isalpha()]
        print(f"Кількість символів - {len(text)}")
        print(f"Кількість літер - {len(letters)}")
        break


def task3():
    while True:
        text = input("Введіть текст: ").strip()
        if not any(l.isalpha() for l in text):
            print("Введіть хоча б одну літеру")
            continue

        search = input("Введіть слово для пошуку: ").strip()
        if not any(l.isalpha() for l in search):
            print("Введіть хоча б одну літеру у слові для пошуку")
            continue

        words = re.findall(r"[А-Яа-яA-Za-zЇїІіЄєҐґ'-]+", text.lower())
        count = sum(1 for w in words if w == search.lower())
        print(f"Слово '{search}' зустрічається {count} раз(ів)")
        break

def task4():
    allowed = re.compile(r"^[А-Яа-яЇїІіЄєҐґ\s.,!?:;\"'()\[\]{}«»„“”’\-—–…]+$")
    ua = re.compile(r"[А-Яа-яЇїІіЄєҐґ]+(?:[-'’][А-Яа-яЇїІіЄєҐґ]+)*")

    while True:
        text = input("Введіть український текст (до 1000 слів): ").strip()
        if not text:
            print("Рядок порожній")
            continue
        if not allowed.fullmatch(text):
            print("Текст має містити лише українські літери")
            continue

        words = list(ua.finditer(text))
        n = len(words)
        if n == 0:
            print(" | "); break
        if n > 1000:
            print("Кількість слів більше 1000")
            continue

        mid, out, pos = n // 2, [], 0
        for i, m in enumerate(words, 1):
            s, e = m.span()
            if s > pos:
                out.append(text[pos:s])
            w = m.group()
            if i <= mid:
                out.append(w.capitalize())
                if i == mid:
                    out.append(" |")
            else:
                out.append(w.lower() + "*")
            pos = e
        out.append(text[pos:])
        print("".join(out))
        break

def task5():
    while True:
        text = input("Введіть англійський текст (до 1000 слів): ").strip()
        if not re.fullmatch(r"[A-Za-z]", text):
            print("Текст має бути англійською")
            continue

        words = re.findall(r"[A-Za-z'-]+", text)
        if len(words) > 1000:
            print("Текст не має бути більше 1000 слів")
            continue

        n = input("Введіть літеру N: ").strip()
        p = input("Введіть літеру P: ").strip()
        if not (len(n) == 1 and len(p) == 1 and n.isascii() and p.isascii() and n.isalpha() and p.isalpha()):
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
        text = input("Введіть англійський текст (до 100 слів): ").strip()
        if not re.search(r"[A-Za-z]", text):
            print("Текст має бути англійською")
            continue

        words = re.findall(r"[A-Za-z'-]+", text)
        if len(words) > 100:
            print("Текст не має бути більше 100 слів")
            continue

        count = sum(1 for ch in text.lower() if ch in vowels)
        print(f"Кількість голосних: {count}")
        break


def task7():
    while True:
        text = input("Введіть англійський текст (до 1000 слів): ").strip()
        if not re.search(r"[A-Za-z]", text):
            print("Текст має бути англійською")
            continue

        words = re.findall(r"[A-Za-z'-]+", text)
        if len(words) > 1000:
            print("Текст не має бути більше 1000 слів")
            continue

        proper = [w for w in words if w[0].isupper()]
        print(f"Слова з великої літери (імена, власні назви): {proper}")
        break

# task1()
# task2()
# task3()
task4()
# task5()
# task6()
# task7()
