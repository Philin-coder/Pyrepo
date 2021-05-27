import math


def test(x: float) -> float:
    if x > 0:
        y = ((math.fabs(2*x)-4)/(2*x+2))-1+(x**2)-math.fabs(x)
        return y
    else:
        return 0


if __name__ == '__main__':
    print(test(x=float(input())))
