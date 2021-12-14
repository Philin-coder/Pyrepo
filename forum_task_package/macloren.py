import math


def mck_loren(x: float, e: float, km: int) -> [tuple, float]:
    s = 1
    k = 0
    t = 1
    if isinstance(x, float) and isinstance(km, int) and isinstance(e, float):
        while math.fabs(t) > e:
            k += 1
            t = t * x * x / (2 * k * (2 * k - 1))
            s = s + t
            if k > km:
                print('При kmax=', km, ' ряд не сходится!')
                print('достигнутая точность=' + str(math.fabs(t)), 'сумма=', ' ', s)
                print('аналитически=', (math.exp(x) + math.exp(-x)) / 2)
        print('достигнутая точность=', math.fabs(t), ' сумма=', s, ' k=', k)
        return 'аналитически=', (math.exp(x) + math.exp(-x)) / 2
    else:
        raise TypeError('Передан неверный тип данных')


if __name__ == '__main__':
    print(mck_loren(x=float(input()), e=float(input()), km=int(input('итерации'))))
