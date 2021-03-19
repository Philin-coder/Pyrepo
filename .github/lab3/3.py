# В последовательности из N целых чисел подсчитать количество чѐтных и нечѐтных чисел.
def countchet(n):
    mlist = [i for i in range(1, 12) if not i % 2]
    print(mlist)
    mlist1 = [i for i in range(1, 12) if i % 2]
    print(mlist1)
    print(len(mlist1))
    print(len(mlist))


if __name__ == '__main__':
    n = int(input())
    countchet(n)
