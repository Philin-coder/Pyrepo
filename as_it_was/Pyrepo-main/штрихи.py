def shtrih(x, y):
    if x >= 0 and x >= x - 6 and x * x + y * y <= 36:
        return 'Да'
    return 'Нет'


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    shtrih(x, y)
