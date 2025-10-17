def task1():
    n = []
    while True:
        try:
            num1 = float(input("Введіть число "))
            break
        except ValueError:
            print("Ви ввели не число")
    while True:
        try:
            num2 = float(input("Введіть число "))
            break
        except ValueError:
            print("Ви ввели не число")
    while True:
        try:
            num3 = float(input("Введіть число "))
            break
        except ValueError:
            print("Ви ввели не число")
    while True:
        try:
            num4 = float(input("Введіть число "))
            break
        except ValueError:
            print("Ви ввели не число")
    print(f"Введені числа - {num1}, {num2}, {num3}, {num4}")
    return num1, num2, num3, num4

def task2(n):
    result = []
    i = 0
    while i < len(n) - 1:
        result.append(n[i] + n[i + 1])
        result.append(n[i] - n[i + 1])
        result.append(n[i] * n[i + 1])
        try:
            result.append(n[i] / n[i + 1])
        except ZeroDivisionError:
            print("Ділення на 0")
            result.append(0)
        result.append(n[i] ** n[i + 1])
        try:
            result.append(n[i] // n[i + 1])
        except ZeroDivisionError:
            print("Ділення на 0")
            result.append(0)
        try:
            result.append(n[i] % n[i + 1])
        except ZeroDivisionError:
            print("Ділення на 0")
            result.append(0)
        i += 1
    print(f"Список елементів пілся математичних дій - {result}")
    return result

def task3(n):
    pare = []
    for i in n:
        if  i == int(i) and int(i) % 2 == 0:
            pare.append(i)
    print(f"Кількість елементів у списку - {len(n)}", f"\nПарні елементи списку - {pare}")

def task4(n):
    saved = []
    saved.append(n[1]), saved.append(n[4])
    n[1] = saved[1]
    n[4] = saved[0]
    print(f"Масив після перестановки 2 і 5 елемту - {n}")

def task5():
    while True:
        name = str(input(""))
        if name.replace(" ", "").isalpha():
            print(f"Лабораторну виконав {name}\nВисковки:\n"
            f"1. В ході виконання лабораторної роботи я ознайомився з алгоритмами послідовної (лінійної) структури, з процедурами запуску програм, які реалізують ці алгоритми на мові Python."
            f"\n2. Познайомився з інтегрованим середовищем розробки – integrated development environment (IDLE).")
            break
        else:
            print("Ви ввели не текст")


# Завдання 1
numbers1 = task1()
# Завдання 2
numbers2 = task2(numbers1)
#Завдання 3
task3(numbers2)
#Завдання 4
task4(numbers2)
#Завдання 5
task5()
