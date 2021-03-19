def roman(): __(one, two)


def __(a: int, b: int):
    print(f'{_(a)} + {_(b)} = {_(a + b)}')


def _(one: int) -> str:
    if one <= 3: return 'I' * one
    if one == 4: return 'IV'
    if one <= 8: return 'V' + _(one % 5)
    if one == 9: return 'IX'
    if one <= 18: return 'X' + _(one % 10)


assert _(5) == 'V'

one = 9
two = 4
roman()