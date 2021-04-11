import numpy
a = numpy.arange(0, 9).reshape(3, 3)
b = numpy.arange(0, 9).reshape(3, 3)
c = numpy.dot(a, b)
print(c)