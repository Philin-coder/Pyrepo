class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class MyMegaGurrenLagenList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        """Добавить элемент в конец списка"""
        node = Node(value)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node


ls = MyMegaGurrenLagenList()
ls.add(42)

print(ls.tail)
