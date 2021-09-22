def multiplier(n):
    "multiplier(n) возвращает функцию, умножающую на n"

    def mul(k):
        return n * k

    return mul
    # того же эффекта можно добиться выражением
    # multiplier = lambda n: lambda k: n*k


mul2 = multiplier(2)  # mul2 - функция, умножающая на 2, например,
mul2(5) == 10
