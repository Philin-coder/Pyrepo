import math
import numpy as np
#import matplotlib.pyplot as plt


class Function():
    def f(self, x):
        return math.log(abs(x+1)) - 2*math.pow(x, 2) + 1


class NewtonMethod():
    def derrirative(self, x):
        return 1/(x+1) - 4*x

    def newtonsMethod(self, f, a, b, derrirative):
        try:
            x0 = (a+b)/2
            xn = x0
            xn1 = xn - f(xn) / derrirative(xn)
            while abs(xn1-xn) > math.pow(10, -3):
                xn = xn1
                xn1 = xn - f(xn) / derrirative(xn)
            return xn1
        except:
            print("Error!")


func = Function()
#hi = HalfInterval()
nm = NewtonMethod()
variant = input(
    "Enter the name of method:\nHI - Half Interval Method\nNM - Newton`s Method\nSIP - Simple Iterations Method\n")

if variant == "HI":
    x = hi.halfIntervalMethod(func.f, -0.6, -0.4)
    y = hi.halfIntervalMethod(func.f, 0.8, 1.0)
    print("The first solution on such interval [-0.6; -0.4] x1 is: " + str(x))
    print("The second solution on such interval [0.8; 1] x2 is: " + str(y))
    print("F(x1) is: " + str(func.f(x)))
    print("F(x2) is: " + str(func.f(y)))
elif variant == "NM":
    x1 = nm.newtonsMethod(func.f, -0.6, -0.4, nm.derrirative)
    y1 = nm.newtonsMethod(func.f, 0.8, 1., nm.derrirative)
    print(
        "NM The first solution on such interval [-0.6; -0.4] x1 is: " + str(x1))
    print("NM The second solution on such interval [0.8; 1] x2 is: " + str(y1))
    print("F(x1) is: " + str(func.f(x1)))
    print("F(x2) is: " + str(func.f(y1)))
elif variant == "SIP":
    pass
else:
    print("No such method detected. Please, try again")
