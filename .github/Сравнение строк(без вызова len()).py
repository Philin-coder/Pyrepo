def comper(mystr: str, mystr1: str) -> str:
    a, b = len(mystr), len(mystr1)
    if a == b:
        return "equally"
    return [mystr, mystr1][b > a]


if __name__ == '__main__':
    print(comper(mystr=input(), mystr1=input()))
