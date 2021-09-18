def namer(mstring: str) -> str:
    print('hello' + ',' + mstring)
    print('But global name is' + ',' + name)


def globalnamer() -> str:
    print("my global name=" + name)


if __name__ == '__main__':
    global name
    name = "BOB"
    namer(mstring=input())
    globalnamer()
