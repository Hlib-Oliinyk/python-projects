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


task1()
task2()
task3()