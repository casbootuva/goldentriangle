# Changes made to adjust to alwins computer, changes to code, only number pulled out
#
#
#
#
#
#

# VOOR VISUALISATIE
import networkx as nx
import matplotlib.pyplot as plt


orderedDictionary = {}
colorAmountList = []

for i in range (0, 1000):
    
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

        # THIS PART IS NEVERU USED        
        def visualize(self):
        	nodes.append(self.name)
        	colors.append(self.color)
        	for neighbor in self.neighbors:
        		edges.append((self.name, neighbor.name)) 

    # DIT IS OOK VOOR VISUALISATIE
    g = nx.Graph()

    edges = []
    colors = []
    nodes = []

    arrayColor = [('#2AD093'), ('#1E9167') ,('#0F4C36'), ('red'),('blue'),('green'),('purple')]
    countryDictionary = {}
    with open("PNcodes.csv", "r") as landcodes:
        lines = landcodes.readlines()
        for line in lines: 
            s = line.split(",")
            countryDictionary[s[0]] = Province(str(s[1]))


    neighborDictionary = {}
    with open("PNneighbors.csv", "r") as neighbors:
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


    colorList = []
    #emergency test for typo's
    #counter = 0


    # order the country dictionary
    from random import shuffle

    orderedCountryList = []
    for i in countryDictionary.keys():
        orderedCountryList.append(i)

    # shuffle(orderedCountryList)
    #print orderedCountryList

    # setcolor
    for j in orderedCountryList:
        #print j
        #print countryDictionary[j]
        #print countryDictionary[j].neighbors
        #counter += 1
        #print counter
        (countryDictionary.get(j)).setColor()
        # IS VOOR PRINTEN VAN KLEUREN
        colorList.append(countryDictionary.get(j).color)
        #print countryDictionary.get(j).color
    colorAmount = max(colorList)

    # prints the minmal amount of numbers
    colorAmountList.append(colorAmount)

    for country in countryDictionary.values():
        country.visualize()


    # prints te values and colors when the lowest coloramount has been found (in this case three)
    if colorAmount == "3": 
        orderedDictionary[colorAmount] = orderedCountryList
        print orderedDictionary
        for values in orderedDictionary.get("3"):
            instance = countryDictionary.get(values)
            print instance.name + " " + instance.color

# THIS LINE DOES NOT WORK IF YOU ENTER RED BLUE GREEN ETC
# print "The minimal amount of colors is", (int(min(colorAmountList)) + 1)

#   DIT IS DE VISUALISATIE : only works when printing one
g.add_nodes_from(nodes)
g.add_edges_from(edges)

position = nx.random_layout(g)
nx.draw_networkx_labels(g,position)

nx.draw_random(g, node_color=colors)

plt.show()


#planaire graaf

#HIER WERD SOWIESO NIETS MEE GEDAAN
# G=nx.Graph()

# G.add_edge(1, 3)
# G[1][3]['color'] = 'blue'


# nx.draw(G)
# plt.show()