import numpy as np
a = np.random.randint(1, 6, 10)
print(a)
tmp = a[::2].max()
b = a[1::2]
b[b == b.min()] = tmp
print(a)
