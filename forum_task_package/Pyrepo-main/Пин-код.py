# В банке "Литровый" хотят установить сейф. Программистами этого банка уже написан генератор случайных пин-кодов для сейфа. Пин-код имеет вид a-b-c, где a, b, c – натуральные числа. Но директор хочет, чтобы его сейф был защищен пин-кодом специального вида: число a должно быть простым, число b должно быть палиндромом, число c должно быть степенью двойки. Напишите функцию checkPin(pinCode), которая проверяет, является ли пин-код корректным.

# Формат ввода
# Строка a-b-c
#
# Формат вывода
# 'Корректен', 'Некорректен'
#
# Пример 1
# Ввод Вывод
# 7-101-4 Корректен
# Пример 2
# Ввод Вывод
# 12-22-16 Некорректен
def is_valid_pin(pin):
    def is_prime(a):
        a = int(a)
        if a % 2 == 0:
            return False
        for i in range(3, int(a ** 0.5) + 1, 2):
            if a % i == 0:
                return False
        return True

    def is_palindrome(b):
        for i in range(0, len(b) // 2):
            if b[i] != b[len(b) - i - 1]:
                return False
        return True

    def is_degree_2(c):
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


pin = '3-101-2'
if is_valid_pin(pin):
    print('Корректен')
else:
    print('Некорректен')
