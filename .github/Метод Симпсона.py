import sympy
 
x = sympy.Symbol('x')
 
f_x = x / (x**4 + 4)
 
 
def sympson(left, right, n, function):
    h = (right - left) / (2 * n)
 
    tmp_sum = float(function.subs({x: left})) +\
        float(function.subs({x: right}))
 
    for step in range(1, 2 * n):
        if step % 2 != 0:
            tmp_sum += 4 * float(function.subs({x: left + step * h}))
        else:
            tmp_sum += 2 * float(function.subs({x: left + step * h}))
 
    return tmp_sum * h / 3
 
 
print(sympson(0, 5, 5, f_x))