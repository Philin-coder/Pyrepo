import random


def mx_mult_func(n: int, m: int) -> tuple:
    """
    Произведение четных положительных элементов матрицы.
    :param n: размерность матрицы(столбцы).
    :param m: размерность матрицы(строки)
    :return: произведение четных поло.
    Образец вызова
    mx_mult(n=5, m=5)
    """
    if isinstance(n, int) and isinstance(m, int):
        matrix = []
        for _ in range(n):
            m_row = []
            for _ in range(m):
                value = random.randint(1, 18)
                m_row.append(value)
            matrix.append(m_row)
        for m_row in matrix:
            print(*m_row)
        ml = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] > 0 and matrix[i][j] % 2 == 0:
                    ml *= matrix[i][j]
        return "произведение четных элементов - ", ml
    else:
        raise TypeError('передан неверный тип данных')
