import random
from typing import Callable, List


def alpha_random_nums(start_p: int, end_p: int, n: int) -> Callable[[], List[str]]:
    """
    Генерация аналийских букв случайным образом
    :param start_p: начало диапазона
    :param end_p: конец диапазона
    :param n: количество букв
    :return: список букв
    Пример вызова
    lt = alpha_random_nums(start_p=97, end_p=123, n=14)
    print(lt())
    """
    if isinstance(start_p, int) and isinstance(end_p, int) and isinstance(n, int):
        if start_p <= 97 and end_p <= 123 and n <= 26 and start_p != 0 and end_p != 0 and n != 0:
            try:
                letter_numbers = [random.randint(start_p, end_p) for _ in range(n)]

            except ValueError:
                raise ValueError('введены  неверные значенмя диапазонов в выдаче могут содержаться не только буквы')
        else:
            raise ValueError('проверьте диапазон')

    else:
        raise TypeError('Введите целые числа')

    def random_letter_gen() -> list[str]:
        return [chr(i) for i in letter_numbers]

    return random_letter_gen
