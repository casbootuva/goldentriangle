import networkx as nx
import matplotlib.pyplot as plt
from random import random

g = nx.Graph()
nodes = ['lon', 'cas', 'ali', 'hoi',3,4,5,6]
edges = [('lon','cas'),('cas','ali'),('ali','lon'),(3,4)]

#g.add_edge(1, [3, 2, 4])
#g.add_edge([1, 4], [1, 3], [2, 5])
#g.add_edge('cra', 'law', 'mer')

g.add_nodes_from(nodes)
g.add_edges_from(edges)

colors = [('#2AD093'), ('#1E9167') ,('#0F4C36'), ('red')]

# show nrs on circles
position = nx.circular_layout(g)
nx.draw_networkx_labels(g,position)

#draw graph
nx.draw_circular(g, node_color=colors)
plt.show()

# website maarten: http://stackoverflow.com/questions/8082420/networkx-change-node-color-in-draw-circular