# 
# Lonnekke Lammers, Cas Boot en Alwin Lijdsman
# Golden Triangle
# 
# Vak: Heuristieken
# Periode 2 semester 1 2015-2016
# Begeleider: Maarten 
# Werkcollegedocent: Tim
# Inleverdatum: 18 december 2015
#

import networkx as nx
import matplotlib.pyplot as plt
from random import shuffle

# THE AMOUNT OF TIMES THAT THE ALGORITHM IS PERFORMED TO CALCULATED THE STATISTICS
orderedDictionary = {}
colorAmountList = []
fourColorResultList = []

for i in range (0, 500):
    
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

    arrayColor = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    countryDictionary = {}
    with open("NWcodes.csv", "r") as landcodes:
        lines = landcodes.readlines()
        for line in lines: 
            s = line.split(",")
            countryDictionary[s[0]] = Province(str(s[1]))

    neighborDictionary = {}
    with open("NWneighbors.csv", "r") as neighbors:
        rows = neighbors.readlines()
        for row in rows: 
            n = row.split(",")
            neighborDictionary[n[0]] = n[1:-1]
     
    for n in countryDictionary:
        for m in neighborDictionary:
            if m == n:
                for i in neighborDictionary.get(m):
                    (countryDictionary.get(n)).addNeighbor(countryDictionary.get(i))


    # Searching algorithms are applied
    colorList = []
    orderedCountryList = []
    for i in countryDictionary.keys():
        orderedCountryList.append(i)

    # ''' 
    # ==============This part is used for random sampling Comment out when using depth first ==============
    # '''
    # shuffle(orderedCountryList)
    # ''' 
    # ===============This part is used for random sampling==============
    # '''


    ''' 
    =============This part is used for depth first searching - Comment out when using random =====================
    '''

    # Instantion dictionary with key values ranging up to max neighbor count
    NeighborCountDict = {}
    for i in orderedCountryList:
        for j in countryDictionary:
            if i == j:
                country = countryDictionary.get(j)
                NeighborCountDict[len(country.neighbors)] = []


    # Append instantiation of country to proper key depending on neighbor count
    for i in orderedCountryList:
        for j in countryDictionary:
            if i == j:
                country = countryDictionary.get(j)
                NeighborCountDict[len(country.neighbors)].append(country)

    depthFirstList = []
    # print NeighborCountDict
    for i in range (len(NeighborCountDict), 1, -1):
        
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

    # THIS IS WHERE COLORS ARE SET
    for j in orderedCountryList:
        (countryDictionary.get(j)).setColor()

        # IS VOOR PRINTEN VAN KLEUREN
        colorList.append(countryDictionary.get(j).color)
        #print countryDictionary.get(j).color
    colorAmount = max(colorList)

    # prints the minmal amount of numbers
    colorAmountList.append(colorAmount)

    # Finds value of last map with solution of 4 colours used

    # prints te values and colors when the lowest coloramount has been found (in this case three)
    colorOverviewList = []
    if colorAmount == "4": 
        for county in orderedCountryList:
            for j in countryDictionary:
                if county == j:
                    fourColorResultList.append(countryDictionary.get(j))
                    colorOverviewList.append((countryDictionary.get(j)).color)

        # PRINTS ANSWERS FOR COLOURING, DONT DELETE
        # This is the answer dictionary
        # print orderedDictionary
        # for values in orderedDictionary.get("3"):
        #     instance = countryDictionary.get(values)
        #     print instance.name + " " + instance.color


# Calculates and prints statistics
intColorAmountList = []
for i in colorAmountList:
    intColorAmountList.append(float(i))

average = sum(intColorAmountList) / len(intColorAmountList)
print "The average 1000 iterations on this module is", (average + 1)
print "The minimal amount of colors is", (int(min(colorAmountList)) + 1)

# This is used for the visualistation
visualisationDict = {"0":('black'), "1":('purple'), "2":('yellow'), "3":('red'), "4":('blue'), "5":('green'), "6":('grey')}
for country in fourColorResultList:
    country.color = visualisationDict[country.color]
    country.visualize()

g.add_nodes_from(nodes)
g.add_edges_from(edges)

position = nx.random_layout(g)
#nx.draw_networkx_labels(g,position)

nx.draw_random(g, node_color=colors)

plt.show()