class Stud(object):
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname

    @classmethod
    def nametripler(cls, name):
        # print('print three times %s'%cls)
        return name * 3

    @property
    def nicknamer(self):
        return "%s" % (self.name + 'nick')


if __name__ == '__main__':
    # Stud.name=input('Введи имя')
    st = Stud(name=None, nickname=None)
    st.name = input()
    print(Stud.nametripler(st.name))
    print(st.nicknamer)
