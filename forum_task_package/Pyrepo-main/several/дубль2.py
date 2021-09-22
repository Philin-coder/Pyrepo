import inspect


def func(arg1, arg2):
    res = arg1 + arg2
    print(res)
    return res


if __name__ == '__main__':
    lines = inspect.getsource(func)
    print(lines)
    arg1 = int(input())
    arg2 = int(input())
