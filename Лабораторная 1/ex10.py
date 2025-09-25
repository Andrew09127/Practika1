s = 0
while True:
    print("Введите число для сложения (ввод 0 означает остановку программы)")
    x = int(input())
    if x == 0:
        break
    s += x
print("Сумма =", s)


count = 0
while True:
    print("Ввод число для подсчета кол-ва чисел (ввод отрицательного числа означает остановку программы):")
    x = int(input())
    if x < 0:
        break
    count += 1
print("Количество =", count)


s = 0
while True:
    print("Введите нечетное число для подсчета суммы (ввод четного числа означает остановку программы):")
    x = int(input())
    if x % 2 == 0:
        break
    s += x
print("Сумма нечётных =", s)


nums = []
while True:
    print("Ввод чисел (ввод числа больше 100 означает остановку программы):")
    x = int(input())
    if x > 100:
        break
    nums.append(x)
print("Среднее арифметическое =", sum(nums)/len(nums))
