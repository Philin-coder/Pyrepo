def chetv(x, y):
    if ((x > 0) and (y > 0)):
        res = True
        print(res)
    if ((x < 0) and (y > 0)):
        res = True
        print(res)

    return res


if __name__ == '__main__':
    assert chetv(3, 4) == True
    assert chetv(-3.5, 8) == True
