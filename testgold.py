import networkx as nx
import matplotlib.pyplot as plt

class Province():
    """
    Een leeg vak op een kaart
    """
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.color = "?"

# append etc. hier toevoegen
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def checkColor(self, colorCountry):
        colorChecker = True
        for neighbor in self.neighbors:
            if colorCountry == neighbor.color:
                colorChecker = False
                return False
        return True

    def setColor(self):
        for color in arrayColor:
            if self.checkColor(color) == True:
                self.color = color
                break
    
    def visualize(self):
    	nodes.append(self.name)
    	colors.append(self.color)
    	for neighbor in self.neighbors:
    		edges.append((self.name, neighbor.name)) 


g = nx.Graph()

edges = []
colors = []
nodes = []

arrayColor = ["red", "orange", "white", "yellow", "green", "purple", "blue"]
countryDictionary = {}
with open("codes.csv", "r") as landcodes:
    lines = landcodes.readlines()
    for line in lines: 
        s = line.split(",")
        countryDictionary[s[0]] = Province(str(s[1]))
#print "this is the CountryDictionary", countryDictionary
# Maarten: als we de dictionary willen orderen, moeten we ze eerst nog sorteren, nu automatisch los door hashing van dictionary.

neighborDictionary = {}
with open("neighbors.csv", "r") as neighbors:
    rows = neighbors.readlines()
    for row in rows: 
        n = row.split(",")
        neighborDictionary[n[0]] = n[1:-1]
#print "this is the neighborDictionary", neighborDictionary
 
for n in countryDictionary:
    for m in neighborDictionary:
        if m == n:
            for i in neighborDictionary.get(m):
                (countryDictionary.get(n)).addNeighbor(countryDictionary.get(i))

#emergency test for typo's
#counter = 0
for j in countryDictionary:
    #print j
    #print countryDictionary[j]
    #print countryDictionary[j].neighbors
    #counter += 1
    #print counter
    (countryDictionary.get(j)).setColor()
    print countryDictionary.get(j).color

for country in countryDictionary.values():
	country.visualize()

g.add_nodes_from(nodes)
g.add_edges_from(edges)

position = nx.random_layout(g)
nx.draw_networkx_labels(g,position)

nx.draw_random(g, node_color=colors)

plt.show()






# G=nx.Graph()

# G.add_edge(1, 3)
# G[1][3]['color'] = 'blue'


# nx.draw(G)
# plt.show()