def anagr(mstr, mstr1):
    print([False, True][sum([ord(x) for x in mstr])
          == sum([ord(x) for x in mstr1])])


if __name__ == '__main__':

    anagr(mstr='apple', mstr1='pleap')
