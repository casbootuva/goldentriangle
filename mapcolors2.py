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
import sys
import csv
from random import shuffle

# Used for input handling and instructions
print "for the codes", sys.argv[1], sys.argv[2]

if (bool(sys.argv[1] != "random") & bool(sys.argv[1] != "targeted")):
    print "Error in first argument: As a first argument give either: 'random' - for random sampling or highest or; 'targeted' for targeted count first"
    print "For example:" 
    print "python matplotlib2.py random india"
    sys.exit(0)

if (bool(sys.argv[2] != "india") & bool(sys.argv[2] != "pennsylvania") & bool(sys.argv[2] != "socialnetwork")):
    print "Error in second argument: As a second argument give either: 'india', 'pennsylvania' or 'socialnetwork'"
    print "For example:" 
    print "python matplotlib2.py random india"
    sys.exit(0)

if sys.argv[2] == "india":
    codeFile = "INcodes.csv"
    neighborFile = "INneighbors.csv"
if sys.argv[2] == "pennsylvania":
    codeFile = "PNcodes.csv"
    neighborFile = "PNneighbors.csv"
if sys.argv[2] == "socialnetwork":
    codeFile = "NWcodes.csv"
    neighborFile = "NWneighbors.csv"

# Variables used to store results of 1000 iterations of map coloring in
orderedDictionary = {}
colorAmountList = []
fourColorResultList = []
colorAmountListForHistogram = []
for i in range (0, 1000):
    
    # Class definition
    class Province():
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

    # Variables set for visualisation
    g = nx.Graph()

    edges = []
    colors = []
    nodes = []

    # Used for setting the colors
    arrayColor = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    # Opens CSV files and puts content into dictionaries
    countryDictionary = {}
    with open(codeFile, "r") as landcodes:
        lines = landcodes.readlines()
        for line in lines: 
            s = line.split(",")
            countryDictionary[s[0]] = Province(str(s[1]))

    neighborDictionary = {}
    with open(neighborFile, "r") as neighbors:
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

    if sys.argv[1] == "random":
        shuffle(orderedCountryList)

    elif sys.argv[1] == "targeted":

        # Instantion dictionary with key values ranging up to max neighbor count
        orderedNeighborDict = {}
        for i in orderedCountryList:
            for j in countryDictionary:
                if i == j:
                    country = countryDictionary.get(j)
                    orderedNeighborDict[len(country.neighbors)] = []


        # Append instantiation of country to proper key depending on neighbor count
        for i in orderedCountryList:
            for j in countryDictionary:
                if i == j:
                    country = countryDictionary.get(j)
                    orderedNeighborDict[len(country.neighbors)].append(country)

        depthFirstList = []
        for i in range (len(orderedNeighborDict), 1, -1):
            
            shuffle(orderedNeighborDict[i])
            for j in orderedNeighborDict[i]:
                depthFirstList.append(j)

        orderedCountryList = []
        for i in depthFirstList:
            for j in countryDictionary:
                if i == countryDictionary.get(j):
                    orderedCountryList.append(j)

    # Colors are set here
    for j in orderedCountryList:
        (countryDictionary.get(j)).setColor()
        colorList.append(countryDictionary.get(j).color)
    colorAmount = max(colorList)
    colorAmountList.append(colorAmount)

    # Sets values and colors when the lowest coloramount has been found
    colorOverviewList = []
    if colorAmount == "4": 
        for county in orderedCountryList:
            for j in countryDictionary:
                if county == j:
                    fourColorResultList.append(countryDictionary.get(j))
                    colorOverviewList.append((countryDictionary.get(j)).color)


# Calculates and prints statistics
intColorAmountList = []
for i in colorAmountList:
    intColorAmountList.append(float(i))
    i = int(i) + 1
    colorAmountListForHistogram.append(str(i))

with open('coloramount.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(colorAmountListForHistogram)

average = sum(intColorAmountList) / len(intColorAmountList)
print "The average 1000 iterations on this module is", (average + 1)
print "The minimal amount of colors is", (int(min(colorAmountList)) + 1)

# Code used for visualisation
visualisationDict = {"0":('black'), "1":('purple'), "2":('yellow'), "3":('red'), "4":('blue'), "5":('green'), "6":('grey')}
for country in fourColorResultList:
    country.color = visualisationDict[country.color]
    country.visualize()

g.add_nodes_from(nodes)
g.add_edges_from(edges)

position = nx.random_layout(g)
nx.draw_networkx_labels(g,position)

nx.draw_random(g, node_color=colors)

plt.show()