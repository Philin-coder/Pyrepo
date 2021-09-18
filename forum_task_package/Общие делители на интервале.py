def devis(a, b, n):
    while a <= b:
        m = 0
        for i in range(1, a + 1):
            if a % i == 0:
                m += 1
        if m >= n:
            print(a, '-', m, end=' - ')
            for i in range(1, a + 1):
                if a % i == 0:
                    print(i, end=' ')
            print()
        a += 1


if __name__ == '__main__':
    # a = int(input("Минимум: "))
    # b = int(input("Максимум: "))
    # n = int(input("Минимальное количество делителей: "))
    devis(a=1, b=14, n=2)
