import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = ["0", "1", "2", "3", "4"]
G.add_nodes_from(nodes)

G.add_edge("0", "1", weight=1.0)
G.add_edge("0", "2", weight=2.0)
G.add_edge("1", "0", weight=3.0)
G.add_edge("1", "4", weight=4.0)
G.add_edge("2", "0", weight=5.0)
G.add_edge("2", "3", weight=6.0)
G.add_edge("3", "2", weight=7.0)
G.add_edge("3", "4", weight=8.0)
G.add_edge("4", "1", weight=9.0)
G.add_edge("4", "3", weight=1.0)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
