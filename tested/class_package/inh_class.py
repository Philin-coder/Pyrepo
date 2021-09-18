class Employee(object):
    """
    наследывание классов^ клас employee наследуется классом  manager(доп аттрибут rank)
    Методы вывода разыне
    >>> emp = Employee('John', 'Smih', 123)
    >>> emp.__str__()
    ('Employee:John', 'surname:Smih', 'pay123')
    >>> man = Manager('Ivan', 'Jons', 123, 'Alten')
    >>> man.m_output()
    ('Employee:Ivan', 'surname:Jons', 'pay123', 'Alten')

    """

    def __init__(self, naim, surname, pay):
        self.naim = naim
        self.surname = surname
        self.pay = pay

    def __str__(self):
        return f'Employee:{self.naim}', f'surname:{self.surname}', f'pay{self.pay}'


class Manager(Employee):
    def __init__(self, naim, surname, pay, rank):
        super().__init__(naim, surname, pay)
        self.rank = rank

    def m_output(self):
        return f'Employee:{self.naim}', f'surname:{self.surname}', f'pay{int(self.pay)}', f'{self.rank}'
