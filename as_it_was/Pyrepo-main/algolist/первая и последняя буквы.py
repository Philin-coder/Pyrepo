def play(nazv):
    print(nazv)
    l = (len(nazv))
    last = (nazv[l - 1:])
    first = (nazv[0])
    if first == last:
        res = "первая и последняя буквы совпадают"
        print(res)

    else:
        res = "первая и последняя буквы не  совпадают"
        print(res)
    return res


if __name__ == '__main__':
    nazv = input("введите слово")
    play(nazv)
