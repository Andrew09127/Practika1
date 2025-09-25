print("Сумма чисел от 1 до 10 =", sum(range(1, 11)))

N = int(input("Введите N: "))
print(f"Сумма чисел от 1 до {N} =", sum(range(1, N)))


even_sum = 0
for i in range(1, N):
    if i % 2 == 0:
        even_sum += i
print(f"Сумма чётных чисел от 1 до {N} =", even_sum)


odd_sum = 0
for i in range(1, N):
    if i % 2 != 0:
        odd_sum += i
print(f"Сумма нечётных чисел от 1 до {N}, ", odd_sum)