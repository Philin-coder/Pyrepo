

class Stack(object):
    def __init__(self, size, smax=3):
        self.max = smax
        if size < 1:
            raise Exception('стек пуст')
        if size > smax:
            raise Exception('неправильные данные')
        self.slist = []

    def is_emp(self):
        return self.slist == []

    def push(self, item):
        self.slist.append(item)
        if self.size() > self.max:
            raise Exception('стек переполнен')

    def pop(self):
        return self.slist.pop()
        if self.size() < 1:
            raise Exception('стек пуст ')

    def peak(self):
        return self.slist[len(self.slist)-1]

    def size(self):
        return len(self.slist)

    def show_elem(self):
        return self.slist


if __name__ == '__main__':
    n = int(input())
    st = Stack(n)
    for i in range(n):
        elem = int(input())
        st.push(elem)
        print('В стеке', st.show_elem())
