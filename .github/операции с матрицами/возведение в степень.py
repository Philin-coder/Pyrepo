import numpy
n=int(input())
a = numpy.arange(0, 9).reshape(3, 3)
a=numpy.matrix(a)
print(a)
print(a**n)