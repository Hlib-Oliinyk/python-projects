import random
import math

def task1():
    l = []
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

def task5(A, B):
    res = 0
    for i in range(A, B + 1):
        res += (i ** 2)
    print(f"Сума квадратів всіх чисел від {A} до {B} = {res}")

def task6(a, b):
    res = 0
    i = a
    while i <= b:
        res += i
        i += 1
    print(f"Сума квадратів всіх чисел від {a} до {b} = {res}")

def task7(a):
    res = 0
    for i in range(a, 51):
        res += (i ** 2)
    print(f"Сума квадратів всіх чисел від {a} до 50 = {res}")

def task8(N):
    K = 0
    while (5 ** K) <= N:
        K += 1
    print(f"Найменше ціле цисло при якому виконується нерівність (5^K > {N}) - {K}")

def task9(n):
    k = 1
    for i in range(k, n + 2):
        if (k ** 2) > n:
            print(f"Перше число яке більше за {n} це {k**2}")
            break
        k += 1

def task10(n):
    k = 0
    num = (k ** 2) + 1
    while num <= n:
        k += 1
        num = (k ** 2) + 1
    print(f"Перше число яке більше за {n}, це {num}.")

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

print("Завдання 5")
while True:
    try:
        A = int(input("Введіть число A: "))
        B = int(input("Введіть число B: "))
        if A > B:
            print("Число A не може бути більшим за число B")
            continue
        task5(A, B)
        break
    except ValueError:
        print("Помилка введення")

print("Завдання 6")
while True:
    try:
        a = int(input("Введіть число a: "))
        b = int(input("Введіть число b: "))
        if b <= a:
            print("Число а не може бути більшим за число b")
            continue
        task6(a, b)
        break
    except ValueError:
        print("Помилка введення")

print("Завдання 7")
while True:
    try:
        a = int(input("Введіть число a: "))
        if a <= 0 or a >= 50:
            print("Число a не може бути більшим за 50 або менше 0")
            continue
        task7(a)
        break
    except ValueError:
        print("Помилка введення")

print("Завдання 8")
while True:
    try:
        N = int(input("Введіть число N: "))
        if N < 1:
            print("Число N не може бути меншим за 1")
            continue
        task8(N)
        break
    except ValueError:
        print("Помилка введення")

print("Завдання 9")
while True:
    try:
        n = int(input("Введіть число n: "))
        if n <= 0:
            print("Число n не може бути меншим за 0")
            continue
        task9(n)
        break
    except ValueError:
        print("Помилка введення")

print("Завдання 10")
while True:
    try:
        n = int(input("Введіть число n: "))
        if n <= 0:
            print("Число n не може бути меншим за 0")
            continue
        task10(n)
        break
    except ValueError:
        print("Помилка введення")
