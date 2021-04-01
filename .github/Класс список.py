import random


class RL(object):
    def __init__(self, mlist):
        self.a = list(reversed(mlist))

    def __str__(self):
        return str(self.a)


if __name__ == '__main__':
    ml1 = [random.randint(1, 10) for i in range(5)]
    print(ml1)
    ml2 = RL = [random.randint(1, 10) for i in range(5)]
    print(ml2)
