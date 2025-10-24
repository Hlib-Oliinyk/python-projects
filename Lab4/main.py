def task1():
    while True:
        try:
            n = int(input("Введіть кількість елементів: "))
            if n <= 0:
                print("Довжина має бути додатною")
                continue
            break
        except ValueError:
            print("Введіть число")

    arr = []
    for i in range(n):
        while True:
            try:
                arr.append(int(input(f"{i + 1}: ")))
                break
            except ValueError:
                print("Введіть число")

    print("Максимальний:", max(arr))
    print("Зворотній список:", arr[::-1])

def task2():
    while True:
        try:
            n = int(input("Кількість елементів: "))
            if n <= 0:
                print("Довжина має бути додатною")
                continue
            break
        except ValueError:
            print("Введіть число")

    arr = []
    for i in range(n):
        while True:
            try:
                arr.append(int(input(f"{i + 1}: ")))
                break
            except ValueError:
                print("Введіть число")

    pos = [x for x in arr if x > 0]
    other = [x for x in arr if x <= 0]
    print("Позитивні:", pos)
    print("Решта:", other)

def task3():
    arr = []
    for i in range(20):
        while True:
            try:
                arr.append(int(input(f"{i + 1}: ")))
                break
            except ValueError:
                print("Введіть число")

    s = sum(arr[i] for i in range(1, len(arr), 2))
    print("Список:", arr)
    print("Сума непарних індексів:", s)

def task4():
    import random
    arr = [random.randint(-100, 100) for _ in range(30)]
    m = max(arr)
    print("Максимальний:", m, "Індекс:", arr.index(m))
    odd = [x for x in arr if x % 2 != 0]
    print("Непарні:", sorted(odd, reverse=True) if odd else "Немає непарних")

def task5():
    import random
    arr = [random.randint(-100, 100) for _ in range(30)]
    for i in range(len(arr) - 1):
        if arr[i] < 0 and arr[i + 1] < 0:
            print(arr[i], arr[i + 1])

def task6():
    arr = []
    for i in range(10):
        while True:
            try:
                arr.append(int(input(f"{i + 1}: ")))
                break
            except ValueError:
                print("Введіть число")

    m = max(arr)
    new = sorted([x ** 2 for x in arr if x < m], reverse=True)
    print("Максимальний:", m)
    print("Новий список:", new)

def task7():
    import random
    arr = [random.randint(-100, 100) for _ in range(30)]
    min_abs = max(arr, key=lambda x: abs(x))
    print("Мінімальний по модулю:", min_abs)
    print("В порядку зростання:", sorted(arr))

def task8():
    import random
    arr = [random.uniform(-100, 100) for _ in range(30)]
    groups = [arr[i:i + 3] for i in range(0, 30, 3)]
    groups.sort(key=lambda g: sum(abs(x) for x in g))
    for g in groups:
        print(f"{g} -> сума = {sum(abs(x) for x in g):.2f}")


# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
task7()
# task8()