def random_func(p: int, q: int) -> list:
    """
     1) Даны целые числа pq a1 … a67 ( p>q≥0 ) . В последовательности a1 … a67
     заменить нулями члены, модуль которых при делении на p дает в остатке q
     12, 2,[2, 14, 26, 38, 50, 62]
    :param p:
    :param q:
    :return:список подходящих чисел
    >>> random_func(p=12, q=2)
    [2, 14, 26, 38, 50, 62]

    """
    if isinstance(p, int) or isinstance(q, int):
        ints = (i for i in range(1, 68))
        results = list(i for i in ints if i % p == q)
        return results
    else:
        raise TypeError('введите 2 целых числа')
