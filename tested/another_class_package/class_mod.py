class Employee(object):
    """
    Иллюстрация простого классам
    >>> man = Employee('John', 222, 222.2, 2)
    >>> man.printer().__str__()
    "('Employee:John', 'nom:222', 'pay222.2', '2')"

    """

    def __init__(self, name, nom, zp, u_der):
        self.name = name
        self.nom = nom
        self.zp = zp
        self.u_der = u_der

    def printer(self):
        return f'Employee:{self.name}', f'nom:{self.nom}', f'pay{self.zp}',f'{self.u_der}'


