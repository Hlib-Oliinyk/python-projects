import re
from string import ascii_uppercase


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