import math


def box(a, S):
    a = math.sqrt(S / 3.0)
    h = 0.5 * a
    V = a * a * h
    print(V)
    return V


if __name__ == '__main__':
    assert box(a=2, S=4)
