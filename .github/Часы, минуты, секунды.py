def ticker(Sec):
    h = Sec // 3600
    m = (Sec - h * 3600) // 60
    s = Sec % 60
    print(h, 'час', m, 'мин', s, 'сек')


if __name__ == '__main__':
    Sec = int(input())
    ticker(Sec)
