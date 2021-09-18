def ticker(Sec):
    h = Sec // 3600
    m = (Sec - h * 3600) // 60
    s = Sec % 60
    return h, 'час', m, 'мин', s, 'сек'


if __name__ == '__main__':
    print(ticker(Sec=int(input())))
