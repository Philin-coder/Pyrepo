import random


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def prt(self):
        print(self.x, self.y, self.z)


if __name__ == '__main__':
    p = Point(random.randint(1, 10), random.randint(
        1, 20), random.randint(1, 50))
    p.prt()
    print(str(p.__dir__))
    del p.__dict__["z"]
    print(str(p.__dict__))
