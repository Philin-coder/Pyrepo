from builtins import float


def sloovf(a, b):
    mdict = {
        'add': lambda a, b: a + b,
        'sub': lambda a, b: a - b,
        'mul': lambda a, b: a * b,
        'div': lambda a, b: a / b

    }
    print(mdict['add'](1, 2))
    print(mdict['sub'](1, 2))
    print(mdict['mul'](1, 2))
    print(mdict['div'](1, 2))


if __name__ == '__main__':
    a = float(input())
    b = float(input())
    sloovf(a, b)
