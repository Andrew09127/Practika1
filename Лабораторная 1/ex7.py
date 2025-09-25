import math
print("Факториал 3 =", math.factorial(3))
print("Факториал 5 =", math.factorial(5))

N = int(input("Введите число для факториала: "))
print(f"Факториал {N} =", math.factorial(N))


print("Факториал (ввод 0 означает остановку программы):")
while True:
    n = int(input("Введите число для которого нужно посчитать факториал: "))
    if n == 0:
        break
    print(f"{n}! =", math.factorial(n))
    
    
    
    
    
    
    
    
    
    
    
    
    
# f = 1
# for i in range(1,4):
#     f *= i
     
    
    
    
    
    