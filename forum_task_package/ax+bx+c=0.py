def solver(a: float, b: float, c: float) -> [str, float]:
    discriminant = b ** 2 - 4 * a * c
    print('Дискриминант = ' + str(discriminant))
    if discriminant < 0:
        return 'Корней нет'
    elif discriminant == 0:
        x = -b / (2 * a)
        return 'x = ' + str(x)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return 'x₁ = ' + str(x1), ' ', 'x₂ = ' + str(x2)


if __name__ == '__main__':
    print('Решаем уравнение a•x²+b•x+c=0')
    solver(a=float(input('Введите значение a: ')), b=float(input('Введите значение b: ')),
           c=float(input('Введите значение c: ')))
