import random

def is_number(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def is_valid_year(year):
    return isinstance(year, int) and year >= 0

def is_valid_string(value):
    return isinstance(value, str) and value.strip() != ""

class Bank:
    def __init__(self, initial_balance=0):
        if not is_number(initial_balance) or float(initial_balance) < 0:
            print("Помилка: початковий баланс має бути числом не менше за 0")
            self.__balance = 0
            self.valid = False
        else:
            self.__balance = float(initial_balance)
            self.valid = True

    def deposit(self, amount):
        if not self.valid:
            print("Операції не виконуються через недійсний початковий баланс")
            return
        if not is_number(amount) or float(amount) <= 0:
            print("Помилка: сума поповнення має бути позитивним числом")
            return
        self.__balance += float(amount)
        print(f"Поповнено {amount} Поточний баланс: {self.__balance}")

    def withdraw(self, amount):
        if not self.valid:
            print("Операції не виконуються через недійсний початковий баланс")
            return
        if not is_number(amount) or float(amount) <= 0:
            print("Помилка: сума зняття має бути позитивним числом")
            return
        amount = float(amount)
        if amount > self.__balance:
            print("Недостатньо коштів на рахунку")
            return
        self.__balance -= amount
        print(f"Знято {amount}. Поточний баланс: {self.__balance}")

    def check_balance(self):
        if not self.valid:
            print("Баланс недоступний через недійсний початковий стан рахунку")
            return None
        print(f"Поточний баланс: {self.__balance}")
        return self.__balance


class Coin:
    def __init__(self, sideup='heads'):
        if sideup.lower() not in ('heads', 'tails'):
            print("Некоректне значення для SideUp, встановлено 'heads' за замовчуванням")
            self.__sideup = 'heads'
        else:
            self.__sideup = sideup.lower()

    def toss(self):
        self.__sideup = random.choice(['heads', 'tails'])

    def get_sideup(self):
        return self.__sideup


class Car:
    def __init__(self, make, model, year):
        self.speed = 0
        self.valid = True

        if not is_valid_string(make):
            print("Помилка: Марка має бути непорожнім рядком")
            self.valid = False
            self.make = None
        else:
            self.make = make

        if not is_valid_string(model):
            print("Помилка: Модель має бути непорожнім рядком")
            self.valid = False
            self.model = None
        else:
            self.model = model

        if not is_valid_year(year):
            print("Помилка: Рік має бути цілим числом >= 0")
            self.valid = False
            self.year = None
        else:
            self.year = year

    def accelerate(self):
        if not self.valid:
            print("Дія заборонена: об'єкт створено з некоректними даними")
            return
        self.speed += 5

    def brake(self):
        if not self.valid:
            print("Дія заборонена: об'єкт створено з некоректними даними")
            return
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        if not self.valid:
            print("Дія заборонена: об'єкт створено з некоректними даними")
            return None
        return self.speed

class Dog:
    mammal = True
    nature = "вироджений друг людини"
    breed = "невідома порода"

    def __init__(self, name, age):
        self.valid = True

        if not isinstance(name, str) or not name.strip():
            print("Помилка: ім'я має бути непорожнім рядком")
            self.valid = False
            self.name = None
        else:
            self.name = name.strip()

        if not isinstance(age, int) or age < 0:
            print("Помилка: вік має бути цілим невід’ємним числом")
            self.valid = False
            self.age = None
        else:
            self.age = age

    def speak(self):
        if not self.valid:
            print("Дія заборонена: некоректні дані екземпляра")
            return
        return "Гав-гав!"

    def info(self):
        if not self.valid:
            print("Дія заборонена: некоректні дані екземпляра")
            return
        return f"Ім'я: {self.name}, Вік: {self.age} років"


class Bulldog(Dog):
    nature = "спокійний та впертий"
    breed = "Бульдог"

    def play_behavior(self):
        if not self.valid:
            print("Дія заборонена: некоректні дані екземпляра")
            return
        return f"{self.name} повільно грається, але з великим задоволенням"


class Beagle(Dog):
    nature = "активний та допитливий"
    breed = "Бігль"

    def play_behavior(self):
        if not self.valid:
            print("Дія заборонена: некоректні дані екземпляра")
            return
        return f"{self.name} завжди шукає пригоди під час прогулянок"


class Poodle(Dog):
    nature = "інтелігентний та слухняний"
    breed = "Пудель"

    def play_behavior(self):
        if not self.valid:
            print("Дія заборонена: некоректні дані екземпляра")
            return
        return f"{self.name} із задоволенням виконує команди та фокуси"


class Pets:
    def __init__(self):
        self.pets_list = []

    def add_pet(self, pet):
        self.pets_list.append(pet)

    def show_pets_info(self):
        for pet in self.pets_list:
            if not getattr(pet, 'valid', True):
                print(f"Інформація про {getattr(pet, 'name', 'Невідома тварина')} недоступна через некоректні дані")
                continue

            print(f"Порода: {pet.breed}, Характер: {pet.nature}")
            print(pet.info())
            print(pet.speak())
            if hasattr(pet, 'play_behavior'):
                print(pet.play_behavior())

class Buffer:
    def __init__(self):
        self._buffer = []

    def add(self, *a):
        for x in a:
            if not isinstance(x, int):
                print(f"Пропущено некоректне значення: {x} (повинно бути цілим числом)")
                continue
            self._buffer.append(x)

        while len(self._buffer) >= 5:
            current_five = self._buffer[:5]
            total = sum(current_five)
            print(f"Сума п’ятірки: {total}")
            self._buffer = self._buffer[5:]

    def get_current_part(self):
        return self._buffer.copy()

class NameLengthError(ValueError):
    pass

def check_name(name):
    if not isinstance(name, str):
        print(f"Помилка: ім'я має бути рядком, а не {type(name).__name__}")
        return
    clean_name = name.strip()
    if len(clean_name) < 10:
        raise NameLengthError(f"Довжина менша за 10 символів")

class DecimalToRoman:
    def __init__(self):
        self.roman_map = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]

    def convert(self, number):
        if not isinstance(number, int):
            print("Помилка: число має бути цілим")
            return None
        if number <= 0 or number >= 4000:
            print("Помилка: число має бути від 1 до 3999")
            return None

        result = ""
        for roman, value in self.roman_map:
            while number >= value:
                result += roman
                number -= value
        return result

class RomanToDecimal:
    def __init__(self):
        self.roman_values = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

    def convert(self, roman):
        if not isinstance(roman, str):
            print("Помилка: вхідне значення має бути рядком")
            return None

        roman = roman.upper().strip()
        if not roman:
            print("Помилка: рядок не може бути порожнім")
            return None

        for ch in roman:
            if ch not in self.roman_values:
                print(f"Помилка: недопустимий символ '{ch}' у римському числі")
                return None

        total = 0
        prev_value = 0
        for ch in reversed(roman):
            value = self.roman_values[ch]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        decimal_to_roman = DecimalToRoman()
        if decimal_to_roman.convert(total) != roman:
            print("Помилка: некоректний формат римського числа")
            return None

        return total

def task1():
    account = Bank(1000)
    account.check_balance()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)

def task2():
    coin = Coin()
    n = 10
    for _ in range(n):
        coin.toss()
        print(coin.get_sideup())

def task3():
    car = Car("Toyota", "Corolla", 2002)

    if not car.valid:
        print("Некоректний дані")
        return

    for i in range(5):
        car.accelerate()
        print(f"Швидкість після прискорення {i + 1}: {car.get_speed()} км/год")

    for i in range(5):
        car.brake()
        print(f"Швидкість після гальмування {i + 1}: {car.get_speed()} км/год")

def task4():
    dog1 = Bulldog("Рокі", 5)
    dog2 = Beagle("Белла", 3)
    dog3 = Poodle("Леді", 2)

    my_pets = Pets()
    my_pets.add_pet(dog1)
    my_pets.add_pet(dog2)
    my_pets.add_pet(dog3)

    my_pets.show_pets_info()

def task5():
    buf = Buffer()
    buf.add(1, 2, 3)
    print("Поточний буфер:", buf.get_current_part())

    buf.add(4, 5, 6, 7, 8)
    print("Поточний буфер:", buf.get_current_part())

    buf.add(9, 10)
    print("Поточний буфер:", buf.get_current_part())

def task6():
    try:
        check_name("Олександр")
    except NameLengthError as e:
        print(f"Виняток: {e}")

    try:
        check_name("Олександрович")
    except NameLengthError as e:
        print(f"Виняток: {e}")

def task7():
    d2r = DecimalToRoman()
    print(d2r.convert(1994))

    r2d = RomanToDecimal()
    print(r2d.convert("MCMXCIV"))

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