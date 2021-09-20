class Employee(object):
    """
    Иллюстрация метода dict
    >>> man = Employee('john', 222, 222.2, 2, 12.2)
    >>> man.__dict__
    {'name': 'john', 'nom': 222, 'zp': 222.2, 'u': 2, 'kom': 12.2}
    >>> man = Employee('john', 222, 222.2, 2, 12.2)
    >>> print(man.__str__())
    ('Employee:john', 'number 222', 'pay222.2', 'restrict2', 'kom12.2')

    """

    def __init__(self, name, nom, zp, u, kom):
        self.name = name
        self.nom = nom
        self.zp = zp
        self.u = u
        self.kom = kom

    def __str__(self):
        return f'Employee:{self.name}', f'number {self.nom}', f'pay{self.zp}', f'restrict{self.u}', f'kom{self.kom}'
