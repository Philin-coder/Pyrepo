# Python 3.Надо создать программу которая генерирует пароли первая степень генерации-цифры,
# вторая-цифры и буквы третья-цифры,букву спец символы.
# Ещё она должна проверять пароль который
# ты вводишь на сложность.Код должен быть один.Не отдельно.
import random
import string


def passgen(n, nums):
    numeric = ([random.randint(-10, 10) for i in range(n)])
    numeric = str(numeric)
    numeric = numeric.replace('[', ' ')
    numeric = numeric.replace(']', ' ')
    numeric = numeric.replace(',', '')
    l = ''.join(random.choice(string.ascii_letters) for i in range(n))
    p = ''.join(random.choice(string.punctuation) for i in range(n))
    prom = numeric + l + p
    res = ''.join(random.sample(prom, len(prom)))
    # print(res)
    if nums == 1:
        res = numeric
        print(res)
        print('первая степень')
        return res

    elif nums == 2:
        prom = l + numeric
        res = ''.join(random.sample(prom, len(prom)))
        print(res)
        print('втораая степень')
        return res
    elif nums == 3:
        prom = numeric + l + p
        res = ''.join(random.sample(prom, len(prom)))
        print('третья  степень')
        print(res)

    else:
        print('wrong number')


if __name__ == '__main__':
    n = int(input())
    nums = int(input())
    passgen(n, nums)
