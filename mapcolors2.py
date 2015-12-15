# Lonnekke Lammers, Cas Boot en Alwin Lijdsman
# Golden Triangle
#
#
#
#
#

# VOOR VISUALISATIE
import networkx as nx
import matplotlib.pyplot as plt
from random import shuffle

# THE AMOUNT OF TIMES THAT THE ALGORITHM IS PERFORMED TO CALCULATED THE STATISTICS
orderedDictionary = {}
colorAmountList = []

for i in range (0, 1000):
    
    # CLASS DEFINITION
    class Province():
        """
        Een leeg vak op een kaart
        """
        def __init__(self, name):
            self.name = name
            self.neighbors = []
            self.color = "?"

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

    # DIT IS OOK VOOR VISUALISATIE
    g = nx.Graph()

    edges = []
    colors = []
    nodes = []

    arrayColor = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
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
     
    for n in countryDictionary:
        for m in neighborDictionary:
            if m == n:
                for i in neighborDictionary.get(m):
                    (countryDictionary.get(n)).addNeighbor(countryDictionary.get(i))


    # THIS IS WHERE THE RANDOM/DEPTH FIRST ALGORITHM IS USED
    colorList = []
    orderedCountryList = []
    for i in countryDictionary.keys():
        orderedCountryList.append(i)

    # ''' 
    # ==============This part is used for random sampling==============
    # '''
    # shuffle(orderedCountryList)
    # ''' 
    # ===============This part is used for random sampling==============
    # '''


    ''' 
    =============This part is used for depth first searching =====================
    '''

    # instantiate dictionary with key values ranging up to max neighbor count
    NeighborCountDict = {}
    for i in orderedCountryList:
        for j in countryDictionary:
            if i == j:
                country = countryDictionary.get(j)
                NeighborCountDict[len(country.neighbors)] = []

    # append instantiation of country to proper key depending on neighbor count
    for i in orderedCountryList:
        for j in countryDictionary:
            if i == j:
                country = countryDictionary.get(j)
                NeighborCountDict[len(country.neighbors)].append(country)

    depthFirstList = []
    for i in range (len(NeighborCountDict) + 1, 1, -1):

        shuffle(NeighborCountDict[i])
        for j in NeighborCountDict[i]:
            depthFirstList.append(j)

    orderedCountryList = []
    for i in depthFirstList:
        for j in countryDictionary:
            if i == countryDictionary.get(j):
                orderedCountryList.append(j)

    ''' 
    =============This part is used for depth first searching =====================
    '''
    # FOR FINDING CSV ERRORS
    counter = 0

    # THIS IS WHERE COLORS ARE SET
    for j in orderedCountryList:
        CSV ERRORS FINDER
        print j
        print countryDictionary[j]
        print countryDictionary[j].neighbors
        counter += 1
        print counter

        (countryDictionary.get(j)).setColor()

        # IS VOOR PRINTEN VAN KLEUREN
        colorList.append(countryDictionary.get(j).color)
        #print countryDictionary.get(j).color
    colorAmount = max(colorList)

    # prints the minmal amount of numbers
    colorAmountList.append(colorAmount)

    # THIS PART IS FOR PRINTING A COLORED MAP WHEN NECESSARY - hardcoded in only finding a solution 3 now
    # prints te values and colors when the lowest coloramount has been found (in this case three)
    if colorAmount == "3": 
        orderedDictionary[colorAmount] = orderedCountryList
        # This is the answer dictionary
        #print orderedDictionary
        for values in orderedDictionary.get("3"):
            instance = countryDictionary.get(values)
            # PRINTS ANSWERS FOR COLOURING, DONT DELETE
            #print instance.name + " " + instance.color


# THIS PART CALUCULATES STATISTICS OF MULTIPLE ITERATIONS
intColorAmountList = []
for i in colorAmountList:
    intColorAmountList.append(float(i))

average = sum(intColorAmountList) / len(intColorAmountList)
print "The average 1000 iterations on this module is", (average + 1)
print "The minimal amount of colors is", (int(min(colorAmountList)) + 1)


# DIT IS DE VISUALISATIE
# g.add_nodes_from(nodes)
# g.add_edges_from(edges)

# position = nx.random_layout(g)
# nx.draw_networkx_labels(g,position)

# nx.draw_random(g, node_color=colors)

# plt.show()