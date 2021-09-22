class Node:
    __slots__ = 'name', 'ls'

    def __init__(self, name, ls=None):
        self.name = name
        self.ls = ls or []


data = Node('public class Program', [
    Node('int', [Node('23'), Node('45')]),
    Node('float')
])


def render(node, prefix=''):
    print(prefix, node.name)
    if len(node.ls) == 0:
        return
    for i in node.ls[:-1]:
        render(i, prefix + '  +')
    render(node.ls[-1], prefix + '  =')


render(data)