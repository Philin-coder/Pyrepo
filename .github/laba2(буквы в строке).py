#  Даны символы в строке. Выяснить, имеются ли в все буквы,
# входящие в слово «мир»
def finder(mstr: str) -> bool:
    print(mstr)
    if 'м' not in mstr or 'и' not in mstr or 'р' not in mstr:
        res = False
    else:
        res = True
    print(res)
    return res


if __name__ == '__main__':
    mstr = input()
    finder(mstr)
