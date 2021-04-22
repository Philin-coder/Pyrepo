def dash(func):
    def inner(*args, **kwargs):
        print("==" * 30)
        func(*args, **kwargs)
        print("==" * 30)
    return inner


@dash
def printer(msg):
    print(msg)


if __name__ == '__main__':
    printer("Hello")