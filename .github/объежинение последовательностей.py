n = (10**6)**2
a = [i**2 for i in range(1, int(n**(1/2)))]
b = [i**3 for i in range(1, int(n**(1/3)))]
c = sorted(set(a+b))
print(c[int(input())-1])
