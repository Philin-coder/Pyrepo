class Employe(object):

    def __init__(self, name, nom, zp, uder):
        self.name = name
        self.nom = nom
        self.zp = zp
        self.uder = uder

    def printer(self):
        print(self.name)
        print(self.nom)
        print(self.zp)
        print(self.uder)


if __name__ == '__main__':
    man = employe('111', 222, 222.2, 2)
    man.printer()
