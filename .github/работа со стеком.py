class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


myStack = Stack()
num = float(input())
max_ = num
while True:
    myStack.push(num)
    num = float(input())
    if num > max_:
        max_ = num
print(max_)
