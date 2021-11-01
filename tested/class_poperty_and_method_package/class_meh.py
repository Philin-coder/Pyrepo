class Stud(object):
    """
    Иллюстрация работы с методами и свойствами класса.
    >>> st = Stud(name='Петр ', nickname='Ger Petter')
    >>> Stud.name_mul_three(st.name)
    'Петр Петр Петр '
    >>> st.nick_name_generator
    'Петр  Ger Petter'
    """

    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname

    @classmethod
    def name_mul_three(cls, name):
        if isinstance(name, str) and not any(i.isdigit() for i in name):
            return f'{name * 3}'
        else:
            raise TypeError('Передан неверный тип данных')

    @property
    def nick_name_generator(self):
        if isinstance(self.name, str) and isinstance(self.nickname, str):
            return "%s" % (self.name + ' ' + self.nickname)
        else:
            raise TypeError('Передан неверный тип данных')


if __name__ == '__main__':
    st = Stud(name=1, nickname='Ger Petter')
    print(Stud.name_mul_three(st.name))
    print(st.nick_name_generator)

    st = Stud(name=1, nickname='Ger Petter')
    # st = Stud(name='1', nickname='Ger Petter')
    sl = Stud(name='Павел ', nickname='Apostol')
    print(Stud.name_mul_three(sl.name))
    print(sl.nick_name_generator)
