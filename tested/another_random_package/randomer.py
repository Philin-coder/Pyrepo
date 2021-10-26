import random


def my_rand(start_p: int, end_p: int, ) -> int:
    if isinstance(start_p, int) and isinstance(end_p, int):
        return random.randint(start_p, end_p)
    raise TypeError('Введите  целые числа')
