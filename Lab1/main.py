def task1():
    n = []
    while len(n) < 4:
        try:
            num = float(input("Введіть число: "))
            n.append(num)
        except ValueError:
            print("Ви ввели не число")
    for i in n:
        print(i, end=" ")

# Завдання 1
task1()