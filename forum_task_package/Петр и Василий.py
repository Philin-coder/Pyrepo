def get_lucky(n):
    if n < 5:
        return 2 ** n, 0

    tmp = 0
    itog = 1
    for i in range(6, n + 1):
        itog *= 2
        tmp = (tmp + 1) % 3
        if not tmp:
            itog += 1

    return 2 ** n, itog


print(*get_lucky(int(input())))
