def delindex(mstr):
    print(''.join(letter for index, letter in enumerate(mstr) if index % 3 != 0))


if __name__ == "__main__":
    mstr = input()
    delindex(mstr)
