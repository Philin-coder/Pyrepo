n = int(input('N = '))
last = 1
i = 1
count = 1
while count != n:
    i += 1
    for j in range(i):
        if j == 0:
            next = last + 1
            while True:
                if next % i == 0:
                    last = next
                    count += 1
                    break
                next += 1
        else:
            last = last + i
            count += 1

        if count == n:
            break

print(last)