from itertools import product


def margo(a, b, c, d):
    for a, b, c, d in product(range(25), repeat=4):
        if a*9+b*6+c*3+d == 121:
            print(f'Бегемот: {a}')
            print(f'Коровьев: {b}')
            print(f'Гелла: {c}')
            print(f'Азазелло: {d}')
            print('-----')


if __name__ == '__main__':
    a, b, с, d = int(input())
    margo(a, b, c, d)
