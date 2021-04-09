class A:
    
    def __init__(self, bb):

        self.b = bb


class B:

    def __init__(self):

        self.a = A(self)

    def __del__(self):

        print("die")


def fun():
    b = B()
    


if __name__ == '__main__':
    fun()
