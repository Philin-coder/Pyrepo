import math


def foo():
    list = set()
    for i in range(300):
        flag = True
        for j in range(2, 1 + int(math.sqrt(i))):
            if not i % j:
                flag = False
                break
        if flag:
            list.add(i)
    print(list)
    print(flag)
    return flag


if __name__ == '__main__':
    foo()
