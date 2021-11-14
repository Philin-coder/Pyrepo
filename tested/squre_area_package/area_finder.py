class Rect(object):
    def __init__(self, dl, sh):
        """
        Нахождение площади квадрата и прямоугольника через класс.
        :param dl: длинна фигуры.
        :param sh: ширина фигуры.
        >>> sq = Square(size=2)
        >>> r = Rect(dl=2, sh=3)
        >>> sq.__repr__()
        '2, 2'
        >>> sq.__str__()
        '2, 2'
        >>> sq.__repr__()
        '2, 2'
        >>> sq.area()
        4
        >>> r.repr_dl()
        'длинна фигуры= 2 '
        >>> r.repr_sh()
        'ширина фигуры= 3 '
        >>> r.area()
        6

        """
        self.dl = dl
        self.sh = sh

    def __str__(self):
        return f'{self.dl}, {self.sh}'

    def __repr__(self):
        return f'{self.dl}, {self.sh}'

    def repr_dl(self):
        return f'длинна фигуры= {self.dl} '

    def repr_sh(self):
        return f'ширина фигуры= {self.sh} '

    def area(self):
        if isinstance(self.sh, int) or isinstance(self.dl, int) or isinstance(self.sh, float) or isinstance(self.dl,
                                                                                                            float):
            return self.dl * self.sh
        else:
            raise TypeError('Передан неверный тип данных')


class Square(Rect):

    def __init__(self, size):
        """
        Наследование свойств и методов.
        :param size: размер фигуры.
        """
        super().__init__(size, size)
