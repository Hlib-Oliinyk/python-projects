import random
import math

def task1():
    l = []
    l2 = []
    for i in range(100):
        x = random.randint(0,100)
        l.append(x)
    l.sort()
    print(f"Початковий масив чисел - {l}")
    l2 = [nums for nums in l if nums <= 50]
    print(f"Масив чисел першого інтервалу - {l2}")

def task2(num):
    if num > 1000:
        num = num - (num * 0.05)
    elif num > 500:
        num = num - (num * 0.03)
    print(f"Сума покупки пілся знижки - {num}")

def task3(a, b):
    h = math.sqrt((a ** 2) - ((b / 2) ** 2))
    res = round((0.5 * b * h), 0)
    print(f"Площа {res}")
    if int(res) % 2 == 0:
        print(f"Площа {res} є парною. Після ділення на 2 {res / 2}")
    else:
        print("Не можу ділити на 2!")

def task4(A, B):
    res = 0
    for i in range(A, B + 1):
        res += i
    print(f"Сума всіх чисел від {A} до {B} = {res}")

print("Завдання 1")
task1()

print("Завдання 2")
while True:
    try:
        num = float(input("Введіть вартість покупки "))
        if num < 0:
            print("Вартість не може бути менше 0")
            continue
        if num < 1:
            print("Вартість не може бути наслільки малою")
            continue
        task2(num)
        break
    except ValueError:
        print("Помилка введення")

print("Завдання 3")
while True:
    try:
        a = float(input("Введіть довжину бічної сторони "))
        b = float(input("Введіть довжину основи "))
        if a < 0 or b < 0:
            print("Число не може бути менше 0")
            continue
        if 2 * a <= b:
            print("Такий трикутник не існує (сума двох сторін має бути більшою за третю)")
            continue
        task3(a, b)
        break
    except ValueError:
        print("Помилка введення")

print("Завдання 4")
while True:
    try:
        A = int(input("Введіть число A: "))
        B = int(input("Введіть число B: "))
        if A > B:
            print("Число A не може бути меншим за число B")
            continue
        task4(A, B)
        break
    except ValueError:
        print("Помилка введення")

