import math
lst = [5, 5.16, 20, 32.21, 41.45]  # кто ж числа в кавычках пишет?
for i in lst:
    print(math.modf(i))
