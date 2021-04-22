from random import randint


def fun():
    a = [randint(2, 10000) for _ in range(10000)]
    k = int(input())
    max_num = 0
    for num in a:
        i = 1
        cnt = 0
        while i*i <= num:
            if num % i == 0:
                cnt += 1 + int(i*i != num)
            if cnt > k:
                break
            i += 1
        if cnt == k and num > max_num:
            max_num = num
    return max_num


print(fun())
