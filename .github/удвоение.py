#  Даны натуральное число n, символы s1, …, sn. Преобразовать
# последовательность, удалив каждый символ «–» и повторив каждый символ,
# отличный от «-».


def repeatear(mstr: str) -> str:
    print(mstr)
    n = len(mstr)
    for i in mstr:
        if i == '-':
            mstr = mstr.replace('-', '')
        else:
            print(i * 2)

    print(mstr)
    return mstr


if __name__ == '__main__':
    mstr = input()
    repeatear(mstr)
