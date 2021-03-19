def slovgen():
    slov = {k: i + 1 for i, k in enumerate(['раз', 'два', 'три'])}
    print(slov)


if __name__ == '__main__':
    slovgen()
