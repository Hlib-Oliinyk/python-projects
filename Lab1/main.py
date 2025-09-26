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

# Завдання 1
numbers1 = task1()
# Завдання 2
numbers2 = task2(numbers1)
#Завдання 3
task3(numbers2)
