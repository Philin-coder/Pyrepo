# -*- coding: utf-8 -*-

def example(t1: int, t2: int, p: int, v: int, a: int) -> str:
    if p / v % (t1 + t2) - t1 < 0:
        return "Pass"

    s = v ** 2 / (2 * a)
    t = t2 - (p - s) / v % (t1 + t2) + v / a
    return f"{s:.3f} {t:.3f}"


assert example(30, 20, 145, 5, 3) == "Pass"
assert example(10, 70, 200, 20, 4) == "50.000 67.500"
