import math


def makloren(x, e, s, km):
    s = 1
    k = 0
    t = 1
    while math.fabs(t) > e:
        k += 1
        t = t * x * x / (2 * k * (2 * k - 1))
        s = s + t
        if k > km:
            print('При kmax=', km, ' ряд не сходится!')
            print('достигнутая точность=' + math.fabs(t), 'сумма=', ' ', s)
            print('аналитически=', (math.exp(x) + math.exp(-x)) / 2)
    print('достигнутая точность=', math.fabs(t), ' сумма=', s, ' k=', k)
    print('аналитически=', (math.exp(x) + math.exp(-x)) / 2)


if __name__ == '__main__':
    x = float(input())
    e = float(input())
    s = float(input())
    km = int(input('итерации'))
    makloren(x, e, s, km)
