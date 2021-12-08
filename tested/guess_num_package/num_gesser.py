from random import randint


def guess_number(var2: int) -> str:
    """
    Игра угадай число.
    :param var2:загаданное число.
    :return: Строка, сообщение пользователю о том, какое число за сколько попыток угадали.
    Образец вызова
    guess_number(var2=78)
    """
    if isinstance(var2, int):
        attempts = 1
        var1 = randint(1, 100)
        print("Загадано число от 1 до 99")
        while var1 != var2:
            if var1 > var2:
                print(f"Угадываемое число больше {var2} ")
            elif var1 < var2:
                print(f"Угадываемое число меньше {var2} ")
            attempts += 1
            var2 = int(input("Ваш вариант? - "))
        return f'Вы угадали число {var1} за {attempts} попыток '
    else:
        raise TypeError('передан неверный тип данных')
