import numpy


def np_mass_create(n: int, m: int) -> numpy.ndarray:
    """
    Вектор numpy в виде матрицы.
    :param n: размерность матрицы
    :param m: размерность матрицы
    :return: вектор в виде матрицы
    """
    if isinstance(n, int) and n > 0 and n != 0 and m > 0 and isinstance(m, int) and m != 0:
        return numpy.random.randint(100, size=(n, m)) * 0.1
    else:
        raise TypeError('Введите целые числа')
