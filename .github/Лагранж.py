for i in range(n):
    p = np.poly1d(1)
    for j in range(n):
        if j != i:
            p *= np.poly1d([x[j]], True) / (x[i] - x[j])

    base_functions.append(p)

for i in range(n):
    polynomial += y[i] * base_functions[i]

return polynomial, base_functions
