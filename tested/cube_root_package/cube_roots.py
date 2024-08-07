def cube_root_func() -> list:
    """
    Входных параметров нет
    Вывести на экран таблиу кубических корней первых десяти целых положительных чисел.

    :return:список корней кубических  первых 10 чисел
    >>> cube_root_func()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [1.0, 1.2599210498948732, 1.4422495703074083, 1.5874010519681994, 1.7099759466766968, 1.8171205928321397, 1.912931182772389, 2.0, 2.080083823051904, 2.154434690031884]

    """
    ints = [i for i in range(1, 11)]
    print(ints)
    cube_squares = [i ** (1 / 3) for i in ints]
    return cube_squares
