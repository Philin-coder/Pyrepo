# TODO: one
def func():
    a = int(input("первое число"))
    b = int(input("второе число"))
    x = a + b

    return x


def func2(arg):
    print(arg)


if __name__ == '__main__':
    func2(func())
