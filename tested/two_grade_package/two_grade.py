def check2rec(num: int) -> bool:
    """
    Является ли число степенью 2
    :param num: число, которое проверяется на то, является ли оно сиепенью 2
    :return: результат типа bool(True, если является, иначе False)
    >>> check2rec(num=2)
    True
    >>> check2rec(num=32)
    True
    >>> check2rec(num=122)
    False


    """
    if isinstance(num, int):
        if num == 1:
            return True
        if num & 1:
            return False
        return check2rec(num >> 1)
    else:
        raise TypeError('Введите целое число')


