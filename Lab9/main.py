import re
from string import ascii_uppercase
import csv
import os
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List
import sys

class Alphabet:
    default_lang = "UA"
    default_letters = [
        "А", "Б", "В", "Г", "Ґ", "Д", "Е", "Є", "Ж", "З",
        "И", "І", "Ї", "Й", "К", "Л", "М", "Н", "О",
        "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч",
        "Ш", "Щ", "Ь", "Ю", "Я",
    ]

    UA_PATTERN = re.compile(r'^[А-ЯҐЄІЇЇЙ\' ]+$', re.IGNORECASE)

    def __init__(self, lang: str = None, letters=None):
        self.lang = lang if lang is not None else self.default_lang
        self.letters = letters if letters is not None else self.default_letters

    def print_alphabet(self):
        print(" ".join(self.letters))

    def letters_num(self) -> int:
        return len(self.letters)

    def is_ua_lang(self, text: str) -> bool:
        if not isinstance(text, str) or not text.strip():
            return False
        cleaned = re.sub(r'[^\w\s\']', '', text)
        return bool(self.UA_PATTERN.match(cleaned))


class EngAlphabet(Alphabet):
    __en_letters_num = 26

    EN_PATTERN = re.compile(r'^[A-Za-z\' ]+$')

    def __init__(self):
        super().__init__(lang="EN", letters=list(ascii_uppercase))

    def is_en_letter(self, s: str) -> bool:
        if not isinstance(s, str) or not s.strip():
            return False
        cleaned = re.sub(r'[^\w\s\']', '', s)
        return bool(self.EN_PATTERN.match(cleaned))

    def letters_num(self) -> int:
        return self.__en_letters_num

    @staticmethod
    def example() -> str:
        return "Hello World"


class Human:
    default_name = "Ім'я за замовчуванням"
    default_age = 30

    NAME_PATTERN = re.compile(r"^[A-Za-zА-Яа-яІіЇїЄєҐґ'\- ]+$")

    def __init__(self, name, age, money=0, house=None):
        self._errors = []

        if not isinstance(name, str) or not name.strip():
            self._errors.append("Ім'я має бути непорожнім рядком")
        elif not self.NAME_PATTERN.fullmatch(name.strip()):
            self._errors.append("Ім'я містить недопустимі символи")
        else:
            self.name = name.strip()

        if not isinstance(age, int):
            self._errors.append("Вік має бути цілим числом")
        elif age <= 0 or age > 120:
            self._errors.append("Вік має бути в діапазоні 1–120 років")
        else:
            self.age = age

        if not isinstance(money, (int, float)):
            self._errors.append("Гроші мають бути числом")
        elif money < 0:
            self._errors.append("Гроші не можуть бути від'ємними")
        else:
            self._money = float(money)

        if house is not None and not isinstance(house, House):
            self._errors.append("house має бути об'єктом класу House")
        else:
            self._house = house

        if self._errors:
            print("Помилки при створенні Human:")
            for error in self._errors:
                print(f"{error}")
            raise SystemExit(1)

        print("Human створено")

    def info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Гроші: {self._money:.2f}")
        print(f"Будинок: {self._house._area if self._house else 'немає'} м^2")

    @staticmethod
    def default_info():
        print(f"Значення за замовчуванням - Ім'я: {Human.default_name}, Вік: {Human.default_age}")

    def _make_deal(self, house, price):
        self._money -= price
        self._house = house

    def earn_money(self, amount):
        if not isinstance(amount, (int, float)):
            print("Сума має бути числом")
            raise SystemExit(1)
        if amount <= 0:
            print("Сума не може бути від'ємною або нулем")
            raise SystemExit(1)
        self._money += amount
        print(f"Зароблено {amount}!")

    def buy_house(self, house, discount=10):
        if not isinstance(house, House):
            print("house має бути об'єктом класу House")
            raise SystemExit(1)
        if not (0 <= discount <= 100):
            print("Знижка має бути в діапазоні 0-100%")
            raise SystemExit(1)

        final_cost = house.final_price(discount)
        if self._money < final_cost:
            print(f"Недостатньо грошей. Потрібно {final_cost:.2f}, маємо {self._money:.2f}")
            return False

        print(f"Купуємо будинок за {final_cost:.2f} (знижка {discount}%)")
        self._make_deal(house, final_cost)
        return True


class House:
    def __init__(self, _area=50, _price=50000):
        self._errors = []

        if not isinstance(_area, (int, float)):
            self._errors.append("Площа має бути числом")
        elif _area <= 0:
            self._errors.append("Площа не може бути від'ємною або нулем")
        else:
            self._area = float(_area)

        if not isinstance(_price, (int, float)):
            self._errors.append("Ціна має бути числом")
        elif _price <= 0:
            self._errors.append("Ціна не може бути від'ємною або нулем")
        else:
            self._price = float(_price)

        if self._errors:
            print("Помилки при створенні House:")
            for error in self._errors:
                print(f"{error}")
            raise SystemExit(1)

    def final_price(self, discount):
        if not isinstance(discount, (int, float)):
            print("Знижка має бути числом")
            raise SystemExit(1)
        if discount < 0 or discount > 100:
            print("Знижка має бути в діапазоні 0-100%")
            raise SystemExit(1)
        return self._price * (1 - discount / 100)


class SmallHouse(House):
    def __init__(self):
        super().__init__(_area=40, _price=40000)



class Apple:
    states = ["Відсутнє", "Цвітіння", "Зелене", "Червоне"]

    def __init__(self, _index):
        self._errors = []

        if not isinstance(_index, int):
            self._errors.append("Індекс яблука має бути цілим числом")
        elif _index < 0:
            self._errors.append("Індекс яблука не може бути від'ємним")
        else:
            self._index = _index
            self._state = self.states[0]

        if self._errors:
            print("Помилки при створенні Apple:")
            for error in self._errors:
                print(f"{error}")
            raise SystemExit(1)

        print(f"Яблуко #{self._index} створено: {self._state}")

    def grow(self):
        current_idx = self.states.index(self._state)
        if current_idx < len(self.states) - 1:
            self._state = self.states[current_idx + 1]
            print(f"Яблуко №{self._index}: {self._state}")
        else:
            print(f"Яблуко №{self._index} вже стигле")

    def is_ripe(self):
        return self._state == self.states[-1]


class AppleTree:
    def __init__(self, apples_count):
        self._errors = []

        if not isinstance(apples_count, int):
            self._errors.append("Кількість яблук має бути цілим числом")
        elif apples_count <= 0:
            self._errors.append("Кількість яблук має бути > 0")
        else:
            self.apples = [Apple(i) for i in range(apples_count)]

        if self._errors:
            print("Помилки при створенні AppleTree:")
            for error in self._errors:
                print(f"{error}")
            raise SystemExit(1)

        print(f"Дерево з {len(self.apples)} яблуками створено")

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):
        self.apples.clear()
        print("Урожай зібрано. Список порожній.")


class Gardener:
    def __init__(self, name, _tree):
        self._errors = []

        NAME_PATTERN = re.compile(r"^[A-Za-zА-Яа-яІіЇїЄєҐґ'\- ]+$")
        if not isinstance(name, str) or not name.strip():
            self._errors.append("Ім'я садівника має бути непорожнім рядком")
        elif not NAME_PATTERN.fullmatch(name.strip()):
            self._errors.append("Ім'я садівника містить недопустимі символи")
        else:
            self.name = name.strip()

        if not isinstance(_tree, AppleTree):
            self._errors.append("_tree має бути об'єктом AppleTree")
        else:
            self._tree = _tree

        if self._errors:
            print("Помилкі при створенні Gardener:")
            for error in self._errors:
                print(f"{error}")
            raise SystemExit(1)

        print(f"Садівник {self.name} готовий до роботи")

    def work(self):
        print(f"{self.name} працює")
        self._tree.grow_all()

    def harvest(self):
        if self._tree.all_are_ripe():
            print(f"{self.name} збирає урожай")
            self._tree.give_away_all()
            return True
        else:
            print(f"{self.name}: Яблука ще не стиглі")
            return False

    @staticmethod
    def apple_base():
        print("Стадії дозрівання яблука:")
        for i, state in enumerate(Apple.states):
            print(f"{i}: {state}")



plt.rcParams['font.family'] = 'DejaVu Sans'
class KmrCsv:
    ref = None
    num = None

    def __init__(self, ref: str = None, num: int = None):
        self._errors = []

        if ref is not None:
            if not isinstance(ref, str):
                self._errors.append("ref має бути рядком")
            elif not os.path.exists(ref):
                self._errors.append(f"Файл '{ref}' не існує")
            else:
                self.ref = ref

        if num is not None:
            if not isinstance(num, int):
                self._errors.append("num має бути цілим числом")
            elif num <= 0:
                self._errors.append("num має бути додатнім числом")
            else:
                self.num = num

        if self._errors:
            print("Помилки KmrCsv:")
            for error in self._errors:
                print(f"{error}")
            raise SystemExit(1)

    def set_ref(self, ref: str):
        if not isinstance(ref, str):
            print("ref має бути рядком")
            raise SystemExit(1)
        if not os.path.exists(ref):
            print(f"Файл '{ref}' не існує")
            raise SystemExit(1)
        self.ref = ref

    def set_num(self, num: int):
        if not isinstance(num, int):
            print("num має бути цілим числом")
            raise SystemExit(1)
        if num <= 0:
            print("num має бути додатнім")
            raise SystemExit(1)
        self.num = num

    def read_csv(self) -> List[Dict]:
        if not self.ref:
            print("ref не встановлено")
            raise SystemExit(1)

        try:
            students = []
            with open(self.ref, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    students.append(row)
            return students
        except Exception as e:
            print(f"Помилка читання CSV: {e}")
            raise SystemExit(1)

    def file_info(self):
        students = self.read_csv()
        print(f"КМР #{self.num}: {len(students)} студентів")


class Statistic:

    def avg_stat(self, students: List[Dict]) -> Tuple[float, ...]:
        if not students:
            return tuple()

        cols = list(students[0].keys())
        question_cols = cols[-3:]

        total_correct = [0] * len(question_cols)

        for student in students:
            for i, col in enumerate(question_cols):
                try:
                    value = float(student[col].replace(',', '.'))
                    if value > 0:
                        total_correct[i] += 1
                except:
                    pass

        percentages = tuple((correct / len(students)) * 100 for correct in total_correct)
        return percentages

    def marks_stat(self, students: List[Dict]) -> Dict[float, int]:
        marks = {}
        cols = list(students[0].keys())
        question_cols = cols[-3:]

        for student in students:
            total = 0
            for col in question_cols:
                try:
                    value = float(student[col].replace(',', '.'))
                    total += value
                except:
                    pass

            marks[round(total, 2)] = marks.get(round(total, 2), 0) + 1

        return marks

    def marks_per_time(self, students: List[Dict]) -> Dict[str, float]:
        result = {}
        cols = list(students[0].keys())

        id_col = cols[0]
        duration_col = cols[3]
        question_cols = cols[-3:]

        for student in students:
            student_id = student[id_col]

            total_mark = 0
            for col in question_cols:
                try:
                    value = float(student[col].replace(',', '.'))
                    total_mark += value
                except:
                    pass

            try:
                duration_str = student[duration_col]
                time_match = re.search(r'(\d+)\s*хв\s*(\d+)\s*сек', duration_str)
                if time_match:
                    minutes = int(time_match.group(1))
                    seconds = int(time_match.group(2))
                    total_seconds = minutes * 60 + seconds
                    total_minutes = total_seconds / 60

                    if total_minutes > 0:
                        result[student_id] = total_mark / total_minutes
            except:
                pass

        return result

    def best_marks_per_time(self, students: List[Dict], bottom_margin: float, top_margin: float) -> Tuple:
        if not isinstance(bottom_margin, (int, float)) or not isinstance(top_margin, (int, float)):
            print("Межі мають бути числами")
            return tuple()

        if bottom_margin < 0 or top_margin < bottom_margin:
            print("Неправильний діапазон")
            return tuple()

        marks_per_time = self.marks_per_time(students)
        cols = list(students[0].keys())
        question_cols = cols[-3:]

        filtered = []

        for student in students:
            student_id = student[cols[0]]

            total_mark = 0
            for col in question_cols:
                try:
                    value = float(student[col].replace(',', '.'))
                    total_mark += value
                except:
                    pass

            if student_id in marks_per_time and bottom_margin <= total_mark <= top_margin:
                filtered.append((student_id, total_mark, marks_per_time[student_id]))

        filtered.sort(key=lambda x: x[2], reverse=True)

        return tuple(filtered[:5])


class Plots:

    def __init__(self):
        self.cat = "results"
        os.makedirs(self.cat, exist_ok=True)

    def set_cat(self, cat: str):
        if not isinstance(cat, str):
            print("Каталог має бути рядком")
            raise SystemExit(1)

        self.cat = cat
        os.makedirs(self.cat, exist_ok=True)

    def avg_plot(self, percentages: Tuple[float, ...]):
        if not percentages:
            print("Немає даних для графіка")
            return

        try:
            plt.figure(figsize=(10, 6))
            questions = [f"Q{i + 1}" for i in range(len(percentages))]
            plt.bar(questions, percentages, color='steelblue')
            plt.xlabel('Питання')
            plt.ylabel('% студентів з балом > 0')
            plt.title('Активність за питаннями')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(f"{self.cat}/avg_plot.png", dpi=100)
            plt.close()
            print(f"Збережено: {self.cat}/avg_plot.png")
        except Exception as e:
            print(f"Помилка графіка: {e}")

    def marks_plot(self, marks: Dict[float, int]):
        if not marks:
            print("Немає даних для графіка")
            return

        try:
            plt.figure(figsize=(10, 6))
            mark_values = sorted(marks.keys())
            counts = [marks[m] for m in mark_values]
            mark_labels = [f"{m:.1f}" for m in mark_values]
            plt.bar(mark_labels, counts, color='green')
            plt.xlabel('Загальна оцінка')
            plt.ylabel('Кількість студентів')
            plt.title('Розподіл оцінок')
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(f"{self.cat}/marks_plot.png", dpi=100)
            plt.close()
            print(f"Збережено: {self.cat}/marks_plot.png")
        except Exception as e:
            print(f"Помилка графіка: {e}")

    def best_marks_plot(self, top5: Tuple):
        if not top5:
            print("Немає даних для графіка")
            return

        try:
            plt.figure(figsize=(10, 6))
            ids = [item[0][:8] for item in top5]
            scores = [item[2] for item in top5]
            plt.bar(range(len(top5)), scores, color='orange')
            plt.xlabel('Студент')
            plt.ylabel('Бал/хв')
            plt.title('Топ-5: найкращі результати за хвилину')
            plt.xticks(range(len(top5)), ids, rotation=45)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig(f"{self.cat}/best_marks_plot.png", dpi=100)
            plt.close()
            print(f"Збережено: {self.cat}/best_marks_plot.png")
        except Exception as e:
            print(f"Помилка графіка: {e}")


class KmrWork(KmrCsv, Statistic, Plots):
    kmrs = {}
    cat = "results"

    def __init__(self, ref: str, num: int):
        KmrCsv.__init__(self, ref, num)
        Plots.__init__(self)

        KmrWork.kmrs[num] = ref
        self.set_cat(KmrWork.cat)
        print(f"KmrWork №{num} готова")

    def compare_csv(self, other_num: int):
        if self.num not in KmrWork.kmrs or other_num not in KmrWork.kmrs:
            print("Один з КМР не зареєстрована")
            return

        students1 = self.read_csv()
        other_kmr = KmrCsv(ref=KmrWork.kmrs[other_num])
        students2 = other_kmr.read_csv()

        cols1 = list(students1[0].keys())
        cols2 = list(students2[0].keys())
        question_cols1 = cols1[-3:]
        question_cols2 = cols2[-3:]
        duration_col1 = cols1[3]
        duration_col2 = cols2[3]

        def calc_avg_mark(stds, q_cols):
            total = 0
            for s in stds:
                for col in q_cols:
                    try:
                        total += float(s[col].replace(',', '.'))
                    except:
                        pass
            return total / len(stds) if stds else 0

        def calc_avg_time(stds, d_col):
            total_seconds = 0
            count = 0
            for s in stds:
                try:
                    duration_str = s[d_col]
                    time_match = re.search(r'(\d+)\s*хв\s*(\d+)\s*сек', duration_str)
                    if time_match:
                        minutes = int(time_match.group(1))
                        seconds = int(time_match.group(2))
                        total_seconds += minutes * 60 + seconds
                        count += 1
                except:
                    pass
            return total_seconds / count / 60 if count > 0 else 0

        avg_mark1 = calc_avg_mark(students1, question_cols1)
        avg_mark2 = calc_avg_mark(students2, question_cols2)
        avg_time1 = calc_avg_time(students1, duration_col1)
        avg_time2 = calc_avg_time(students2, duration_col2)

        report = f"""Порівняння КМР №{self.num} vs №{other_num}
Кількість студентів:  {len(students1)} vs {len(students2)}
Середній бал:         {avg_mark1:.2f} vs {avg_mark2:.2f}
Середній час (хв):    {avg_time1:.2f} vs {avg_time2:.2f}
"""
        print(report)

        os.makedirs(self.cat, exist_ok=True)
        with open(f"{self.cat}/compare_{self.num}_{other_num}.txt", 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Збережено: {self.cat}/compare_{self.num}_{other_num}.txt")

    def compare_avg_plots(self, other_num: int):
        if self.num not in KmrWork.kmrs or other_num not in KmrWork.kmrs:
            print("Один з КМР не зареєстрована")
            return

        students1 = self.read_csv()
        other_kmr = KmrCsv(ref=KmrWork.kmrs[other_num])
        students2 = other_kmr.read_csv()

        avg1 = self.avg_stat(students1)
        avg2 = Statistic().avg_stat(students2)

        self.avg_plot(avg1)
        self.set_cat(f"{self.cat}_kmr{other_num}")
        self.avg_plot(avg2)



def task1():
    eng_alphabet = EngAlphabet()

    print("Літери англійського алфавіту:")
    eng_alphabet.print_alphabet()

    print(f"Кількість букв в алфавіті: {eng_alphabet.letters_num()}")

    print(f"Чи буква J належить англійському алфавіту: {eng_alphabet.is_en_letter('J')}")

    ua_alphabet = Alphabet()
    print(f"Чи буква Щ належить українському алфавіту: {ua_alphabet.is_ua_lang('Щ')}")

    print(f"Приклад тексту англійською: {EngAlphabet.example()}")


def task2():
    print("Довідкова інформація")
    Human.default_info()

    print("Створення Human")
    person = Human("Олег", 25, money=30000)
    person.info()

    print("SmallHouse")
    small_house = SmallHouse()
    print(f"Будинок: {small_house._area}м^2, {small_house._price}")

    print("Невдала покупка")
    person.buy_house(small_house)

    print("earn_money")
    person.earn_money(15000)

    print("Успішна покупка")
    person.buy_house(small_house, discount=10)

    print("Фінальний стан")
    person.info()


def task3():
    print("Створення яблук")
    apple1 = Apple(1)
    apple2 = Apple(2)

    print("Довідка")
    Gardener.apple_base()

    print("AppleTree + Gardener")
    tree = AppleTree(3)
    gardener = Gardener("Іван", tree)

    print("Робота садівника")
    gardener.work()

    print("Спроба зібрати урожай")
    gardener.harvest()

    print("Продовжуємо догляд")
    while not gardener._tree.all_are_ripe():
        gardener.work()
        if gardener.harvest():
            break

    print("Фінальна перевірка")
    print(f"Яблук залишилось: {len(gardener._tree.apples)}")

def task4():

    print("Створення об'єктів kmr1 і kmr2")
    kmr1 = KmrWork("marks2.lab11.csv", 1)
    kmr2 = KmrWork("marks2.lab11.csv", 2)

    print("Інформація про файли")
    kmr1.file_info()
    kmr2.file_info()

    print("avg_plot() для kmr2")
    students2 = kmr2.read_csv()
    avg_stats = kmr2.avg_stat(students2)
    print(f"Питань: {len(avg_stats)}")
    print(f"Активність: {[f'{p:.1f}%' for p in avg_stats]}")
    kmr2.avg_plot(avg_stats)

    print("marks_plot() для kmr2")
    marks_stats = kmr2.marks_stat(students2)
    print(f"Розподіл оцінок: {marks_stats}")
    kmr2.marks_plot(marks_stats)

    print("best_marks_per_time()")
    top5 = kmr2.best_marks_per_time(students2, 0, 30)
    print(f"Топ-5 студентів: {len(top5)}")
    for item in top5:
        print(f"  ID: {item[0][:8]}..., Оцінка: {item[1]:.2f}, Бал/хв: {item[2]:.2f}")
    kmr2.best_marks_plot(top5)

    print("compare_csv()")
    kmr1.compare_csv(2)

    print("compare_avg_plots()")
    kmr1.compare_avg_plots(2)


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