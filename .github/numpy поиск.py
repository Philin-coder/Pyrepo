import numpy 


def masgen():
    a = numpy.random.randint(-10,40,(8,8))
    print(a)
    res=numpy.where(a>0)
    print(res)



    

if __name__ == '__main__':
    masgen()
