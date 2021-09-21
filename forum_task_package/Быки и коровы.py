from random import randint

_bulls_cow = {}
user_number = 1522
count = 0


def random_number():
    number = randint(1000, 9999)
    global res
    res = [int(x) for x in str(number)]
    return res


number = random_number()
print(number)


def number_check(user_number):
    count_cows = 0
    count_bulls = 0
    list_user_number = [int(i) for i in str(user_number)]
    for item, i in enumerate(set(number)):
        if i in list_user_number:
            count_cows += 1
            _bulls_cow['cows'] = count_cows
        else:
            count_cows += 0
            _bulls_cow['cows'] = count_cows

    for x in enumerate(number):
        for k in enumerate(list_user_number):
            if k == x:
                count_bulls += 1
                _bulls_cow['bulls'] = count_bulls
            else:
                count_bulls += 0
                _bulls_cow['bulls'] = count_bulls

    return _bulls_cow


if __name__ == '__main__':
    print(number_check(user_number))
