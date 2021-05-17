def delit(a):
    res = 1
    i = 2
    dmax = dmin = False
    d = int(a**0.5) + 2
    while i < d:
        if a % i == 0:
            if not dmin:
                dmin = i
                dmax = a//i
            tmp = 1
            a //= i
            while a % i == 0:
                tmp += 1
                a //= i
            res *= (tmp+1)
            d = int(a**0.5) + 2
        i += 1
    res *= 2 - (a == 1)
    return dmin, dmax, res - 2


t = delit(int(input()))
print('наименьший делитель =', t[0])
print('наибольший делитель =', t[1])
print('всего делителей =', t[2])
