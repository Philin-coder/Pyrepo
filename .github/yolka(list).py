n = 3
mx = n * 2 - 1
res = [('*' * i * 2)[:-1].center(mx) for i in range(1, n + 1)]
print(*res, sep='\n')
