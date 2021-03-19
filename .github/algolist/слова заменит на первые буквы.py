def changer(inp):
    res = ''.join([i[0] for i in inp.split()])
    print(res)
    return res


if __name__ == '__main__':
    inp = input()
    changer(inp)
