def devs(a: int, b: int, n: int) -> list:
    """
    Отыскание общих делителей на интервале.
    :param a: Начало интервала.
    :param b: Конец интервала.
    :param n: количество чисел.
    :return: итоговый список чисел.
    Образец вызова: devs(a=1, b=14, n=2)

        """
    ints = list()
    if isinstance(a, int) and isinstance(b, int) and isinstance(n, int):
        while a <= b:
            m = 0
            for i in range(1, a + 1):
                if a % i == 0:
                    m += 1
            if m >= n:
                print(a, '-', m, end=' - ')
                for i in range(1, a + 1):
                    if a % i == 0:
                        print(i, end=' ')
                        ints.append(i)
                print()
            a += 1
        return ints
    else:
        raise TypeError('Передан неверный тип данных')
