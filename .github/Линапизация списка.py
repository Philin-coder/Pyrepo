lst = [[1, 2], 4, [[2, 4, 8, [-4, "er", [0], [{2: "primer"}], []]]]]


def linear(lst):
    out = []

    def recursion(lst):
        if type(lst) is list:
            for a in lst:
                if type(a) is list:
                    recursion(a)
                else:
                    out.append(a)
        else:
            out.append(lst)

    recursion(lst)

    return out


print(*linear(lst))