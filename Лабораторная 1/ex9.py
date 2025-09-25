while True:
    ch = input("Введите один символ: ")
    if len(ch) == 1:   
        print("Цифра?", ch.isdigit())
        print("Буква?", ch.isalpha())
        print("Гласная?", ch.lower() in "аеёиоуыэюяaeiou")
        print("Прописная буква?", ch.isupper())
        break
    else:
        print("Ошибка: нужно ввести ровно один символ!")
