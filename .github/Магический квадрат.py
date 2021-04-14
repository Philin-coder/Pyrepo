import numpy


def magicsq(a):
    if numpy.array_equal(numpy.unique(a.sum(axis=1)), numpy.unique(a.sum(axis=0))):
        return True
    else:
        return False
