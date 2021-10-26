import random
import string


def pass_gradient(star_p: int, end_p: int, grade: int, n: int) -> str:
    """
    Программа которая генерирует пароли первая степень генерации-цифры,
    вторая-цифры и буквы третья-цифры,букву спец символы.
    Ещё она должна проверять пароль который
    ты вводишь на сложность.Код должен быть один.Не отдельно.
    :param star_p:начала диапазона случайных чисел
    :param end_p: конец диапазона случайных чисел
    :param grade: степень сложности пароля
    :param n: колмчество символов в нем
    :return:пароль
    образец вызова
    print(pass_gradient(star_p=1, end_p=10, grade=1, n=3))
    print(pass_gradient(star_p=1, end_p=10, grade=2, n=3))
    print(pass_gradient(star_p=1, end_p=10, grade=3, n=3))
    print(pass_gradient(star_p=1, end_p=10, grade=4, n=3))


    """
    if isinstance(star_p, int) and isinstance(end_p, int) and isinstance(grade, int) and isinstance(n, int):
        grades = [1, 2, 3]
        if grade in grades and grade == 1:
            print('Первая степень')
            return f'{str([random.randint(star_p, end_p) for _ in range(n)])}'.removeprefix('[').removesuffix(
                ']').strip()
        if grade in grades and grade == 2:
            print('вторая степень')
            sep = ''
            res = sep.join([
                f'{str([random.randint(star_p, end_p) for _ in range(n)])}'.removeprefix('[').removesuffix(']').strip(),
                f'{sep.join(random.choice(string.ascii_letters) for _ in range(n))}'])
            return sep.join(random.sample(res, len(res)))
        if grade in grades and grade == 3:
            print('третья степень')
            sep = ''
            res = sep.join([
                f'{str([random.randint(star_p, end_p) for _ in range(n)])}'.removeprefix('[').removesuffix(']').strip(),
                f'{sep.join(random.choice(string.ascii_letters) for _ in range(n))}'
                f'{sep.join(random.choice(string.punctuation) for _ in range(n))}'
            ])
            return sep.join(random.sample(res, len(res)))
        if grade not in grades:
            return 'wrong grade'
    else:
        raise TypeError('Введите целые числа')
