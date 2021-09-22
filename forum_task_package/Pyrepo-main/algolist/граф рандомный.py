import random
import matplotlib.pyplot
import networkx


def graph(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    g = networkx.DiGraph()
    g.add_nodes_from(mlist)
    g.add_edge(mlist[1], mlist[2])
    g.add_edge(mlist[3], mlist[4])
    g.add_edge(mlist[5], mlist[6])
    g.add_edge(mlist[7], mlist[8])
    g.add_edge(mlist[9], mlist[10])
    networkx.draw(g, with_labels=True)
    matplotlib.pyplot.draw()
    matplotlib.pyplot.show()


if __name__ == '__main__':
    n = int(input())
    graph(n)
