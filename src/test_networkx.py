import networkx as nx
G = nx.Graph()

# easy way to add a node
G.add_node(1)

# More sophisticated
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

# You can merge two graph together
H = nx.path_graph(10)
G.add_node(H)

import matplotlib.pyplot as plt
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')

plt.show()