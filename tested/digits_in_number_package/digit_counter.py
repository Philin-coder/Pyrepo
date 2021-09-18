def digits_in_number(n: int) -> int:
    """
    :param n: число
    :return: возвращается количество цифр в числе
    >>> digits_in_number(n=12)
    2
    >>> digits_in_number(n=123)
    3
    >>> digits_in_number(n=4234343)
    7
    """
    if not isinstance(n, int):
        raise TypeError('Должно быть введено целое число')
    else:
        n = abs(n)

        count = 1
        n //= 10

        while n > 0:
            n //= 10
            count += 1
        return count
