# 1. Типы данных в Python. Встроенные типы данных. Пользовательские типы. Использование словарей, списков и множеств.
# Цель лабораторной работы — описать некоторую предметную область (например, командировки работников отдела) при помощи
# встроенных и пользовательских типов данных языка, а также обеспечить к ним пользовательский доступ.
class employee(object):
    def __init__(self, name, nom, zp, u, kom):
        self.name = name
        self.nom = nom
        self.zp = zp
        self.u = u
        self.kom = kom

    def printer(self):
        print(self.name)
        print(self.nom)
        print(self.zp)
        print(self.u)
        print(self.kom)


if __name__ == '__main__':
    man = employee('john', 222, 222.2, 2, 12.2)
    print(man.__dict__)
