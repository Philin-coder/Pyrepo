def move(n: int, start: int, finish: int) -> tuple:
    """
    Ханойская башня является одной из популярных головоломок XIX века. Даны три стержня, на один из которых нанизаны
    восемь колец, причём кольца отличаются размером и лежат меньшее на большем. Задача состоит в том, чтобы перенести
    пирамиду из восьми колец за наименьшее число ходов на другой стержень. За один раз разрешается переносить только
    одно кольцо, причём нельзя класть большее кольцо на меньшее.
    :param n: количество ходов
    :param start:  стартовый стержень
    :param finish: финишный стержень
    :return: начальный, конечный и 'выиграшный' стержни
    >>> move(n=10, start=1, finish=3)
    Перенести диск 1 со стержня 1 на стержень 2
    Перенести диск 2 со стержня 1 на стержень 3
    Перенести диск 3 со стержня 1 на стержень 2
    Перенести диск 4 со стержня 1 на стержень 3
    Перенести диск 5 со стержня 1 на стержень 2
    Перенести диск 6 со стержня 1 на стержень 3
    Перенести диск 7 со стержня 1 на стержень 2
    Перенести диск 8 со стержня 1 на стержень 3
    Перенести диск 9 со стержня 1 на стержень 2
    Перенести диск 10 со стержня 1 на стержень 3
    (9, 2, 3)
    >>> move(n=8, start=1, finish=4)
    Перенести диск 1 со стержня 1 на стержень 1
    Перенести диск 2 со стержня 1 на стержень 4
    Перенести диск 3 со стержня 1 на стержень 1
    Перенести диск 4 со стержня 1 на стержень 4
    Перенести диск 5 со стержня 1 на стержень 1
    Перенести диск 6 со стержня 1 на стержень 4
    Перенести диск 7 со стержня 1 на стержень 1
    Перенести диск 8 со стержня 1 на стержень 4
    (7, 1, 4)

    """
    if isinstance(n, int) and isinstance(start, int) and isinstance(finish, int) and n > 0 and start > 0 and finish > 0:
        if n == 1:
            print("Перенести диск 1 со стержня", start, "на стержень", finish)
        else:
            temp = (6 - start) - finish
            move(n - 1, start, temp)
            print("Перенести диск", n, "со стержня", start, "на стержень", finish)
            return n - 1, temp, finish

    else:
        raise TypeError('введите целые, положительные  числа')
