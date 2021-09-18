def is_valid_pin(pin: str) -> bool:
    """
    В банке "Литровый" хотят установить сейф. Программистами этого банка
уже написан генератор случайных пин-кодов для сейфа. Пин
-код имеет вид a-b-c, где a, b, c – натуральные числа.
Но директор хочет, чтобы его сейф был защищен пин-кодом специального
вида: число a должно быть простым, число b должно быть палиндромом,
число c должно быть степенью двойки. Напишите функцию checkPin(pinCode),
которая проверяет, является ли пин-код корректным.

Формат ввода
Строка a-b-c

Формат вывода
'Корректен', 'Некорректен'

Пример 1
Ввод Вывод
7-101-4 Корректен
Пример 2
Ввод Вывод
12-22-16 Некорректен

    :param pin: пин-код(в виде строки)
    :return: булевое значениек, которое должно быть True, если функцию срабоатла

    >>> is_valid_pin(pin='7-101-4')
    True
    >>> validator(is_valid_pin)
    'Корректен'




    """

    def is_prime(a: str) -> bool:
        a = int(a)
        if a % 2 == 0:
            return False
        for i in range(3, int(a ** 0.5) + 1, 2):
            if a % i == 0:
                return False
        return True

    def is_palindrome(b: str) -> bool:
        for i in range(0, len(b) // 2):
            if b[i] != b[len(b) - i - 1]:
                return False
        return True

    def is_degree_2(c: str) -> bool:
        c = int(c)
        if c % 2 != 0:
            return False
        i = 2
        while True:
            if i == c:
                return True
            if i > c:
                return False
            i *= 2

    pin = pin.split('-')
    return is_prime(pin[0]) and is_palindrome(pin[1]) and is_degree_2((pin[2]))


def validator(is_valid_pin) -> str:
    if is_valid_pin(pin='7-101-4'):
        return 'Корректен'
    else:
        return 'Некорректен'


