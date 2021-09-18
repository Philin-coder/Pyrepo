"""
Иллюстрация работы lambda-функции
>>> func(1, 4)
17
>>> func(1, 6)
37
"""


def func(x: int, y: int) -> int:
    return x ** 2 + y ** 2
