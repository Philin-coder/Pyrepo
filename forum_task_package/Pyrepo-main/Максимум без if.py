def maximer(a, b):
    c = a // b
    c = ((c + 2) // (c + 1)) % 2
    d = (c + 1) % 2
    res = a * c + b * d
    print(res)
    return res


if __name__ == '__main__':
    assert maximer(a=1, b=2)
