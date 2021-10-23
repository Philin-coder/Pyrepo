import random


def random_list_func(start_p: int, end_p: int) -> int:
    """
    Генерация списка сулчайнх чисел
    :param start_p: начало диапазона сулчайнх чисел
    :param end_p: конец диапазона сулчайнх чисел
    :return: случайное число в диапазона от start_p до end_p
    print([random_list_func(start_p=-10, end_p=10) for i in range(12)]) пример вызов
    """
    if isinstance(start_p, int) and isinstance(end_p, int):
        return random.randint(start_p, end_p)
    else:
        raise TypeError('передан неверный тип данных')
