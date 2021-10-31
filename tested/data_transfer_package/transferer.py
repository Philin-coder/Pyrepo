import random


def create_matrix(n: int) -> list:
    """
    Генерация матрицы случайных чисел.
    :param n:Диапазон.
    :return: список чисел в диапазоне
    """
    if isinstance(n, int) and n > 0 and n != 0:
        return [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    else:
        raise TypeError('Введите число')


def show_matrix(matrix: list):
    """
    Вывод списка случайных чисел в виде матрицы.
    :param matrix:
    :return: Матрица случайных чисел.
    """
    if matrix is not None:
        for i in matrix:
            for j in i:
                print(j, end=' ')
            print()
    else:
        raise TypeError('Для вывода передан не список')
