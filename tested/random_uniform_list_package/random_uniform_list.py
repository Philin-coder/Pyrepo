import random


def num_gen(start_p: int, end_p: int) -> [float, list]:
    """
    Генерация случайных чисел
    :param start_p:начало диапазона
    :param end_p:  конец диапазона
    :return: список вещественных чисел
    Пример вызова
    ng = num_gen(start_p=1, end_p=10)
    print(ng(n=8))
    """
    if isinstance(start_p, int) and isinstance(end_p, int):
        num = random.uniform(start_p, end_p)

        def num_list_gen(n: int) -> list:
            if isinstance(n, int):
                nums = [num for _ in range(n)]
                work_nums = [i * (len(nums) / sum(nums)) + random.uniform(start_p, end_p) for i in nums]
                return work_nums
            else:
                raise TypeError('Передан неверный тип данных')

        return num_list_gen
    else:
        raise TypeError('Передан неверный тип данных')
