while True:
    num = int(input("Введите двузначное число: "))
    if 10 <= num <= 99:
        a = num // 10   
        b = num % 10    
        print("Сумма цифр =", a + b)
        print("Произведение цифр =", a * b)
        break
    else:
        print("Ошибка: нужно ввести двузначное число!")



while True:
    num = int(input("Введите трёхзначное число: "))
    if 100 <= num <= 999:
        c = num // 100      
        d = (num // 10) % 10 
        b = num % 10         
        print("Сумма цифр =", c + d + b)
        print("Первая и последняя цифры =", c, b)
        break
    else:
        print("Ошибка: нужно ввести трёхзначное число!")
