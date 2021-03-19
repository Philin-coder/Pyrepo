def digkiller(vvod):
    res = ''.join([i for i in vvod if not i.isdigit()])
    print(res)


if __name__ == '__main__':
    vvod = str(input())
    digkiller(vvod)
