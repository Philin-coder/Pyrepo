def p(x):
    a = 2 if x >= 0 else .5
    x = abs(x)
    result = 1
    while x > 0:
        if x % 2 == 0:
            a *= a
            x //= 2
        else:
            x -= 1
            result *= a
    return result
    
assert p(0) == 1
assert p(1) == 2
assert p(-1) == .5
assert p(2) == 4
assert p(-2) == .25
assert p(3) == 8
assert p(-3) == .125
assert p(10) == 1024
assert p(16) == 65536