import random

win = 0

lose = 0

while True:

    tip = input("Камень, Ножницы или Бумага? - ")

    res = 0

    if tip.lower() == "камень":
        res = 1

    elif tip.lower() == "ножницы":
        res = 2

    elif tip.lower() == "бумага":
        res = 3

    else:

        print("Нет такого варианта!")

        continue

    rr = random.randrange(1, 3)

    if res == rr:

        win += 1

        print("Вы выиграли!")

    else:

        lose += 1

        print("Вы проиграли ;c")

    print("Счет - ", win, "/", lose, " (Выигрыши/Проигрыши)")
