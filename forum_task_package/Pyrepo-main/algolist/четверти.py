import random


def chetv(x, y):
    if ((x > 0) and (y > 0)):
        res = "первая четврть"
        print(res)
    if ((x < 0) and (y > 0)):
        res = "вторая четврть"
        print(res)
    if ((x < 0) and (y <= 0)):
        res = "третья четврть"
        print(res)
    if ((x > 0) and (y < 0)):
        res = "четвертая четврть"
        print(res)
    return res


if __name__ == '__main__':
    x = float(input())
    y = float(input())
    # chetv(x,y)
    for i in range(3):
        chetv(x=random.randint(-10, 10), y=random.randint(-10, 10))
