from math import atan, sqrt
def fun(a):
    return atan(a) + sqrt(a) + 2
 
xo, xn, h = 3, 6, 0.3
while xo <= xn:
    print(f'x = {xo:.1f}  y = {fun(xo):.3f}')
    xo += h