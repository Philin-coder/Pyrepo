def nabor(k: int) -> [float, str]:
    """
    Дано K наборов ненулевых целых чисел.
    Признаком завершения каждого набора является число 0.
    Вычислить среднее арифметическое всех элементов во всех наборах.
    :param k: количество наборов
    :return: среднее всех элементов во всех наборах
    nabor(k=2)
    2
    nabor 0
    1
    2
    0
    nabor 1
    1
    2
    3
    0
    2.0


    """

    print(k)
    if isinstance(k, int):
        for i in range(k):
            print("nabor", i)
            s = 0
            n = 0
            a = int(input())
            while a != 0:
                s += a
                n = n + 1
                a = int(input())

        if (n != 0):
            return (s / n)
        else:
            return "нельзя делить на 0"

    else:
        raise TypeError('Введите целое чисдл для количества наборов и набор  из целых  числе')
