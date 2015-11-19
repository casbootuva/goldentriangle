# Lonneke Lammers, Cas Boot, Alwin Lijdsman
# Heuristieken
# Kaartkleuren
#
#
# Last update: 2 november 2015 door Alwin Lonneke en Cas
#
# Vraag voor maarten:
#
# Comments Maarten intervisie 1:
# Pygon gebruiken om te visualiseren. Graph visualisatie Python zijn er wel libraries
#
# class: land

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

arrayColor = ["red", "orange", "yellow", "green", "purple", "blue"]

countryDictionary = {}
with open("testcodes.csv", "r") as landcodes:
    lines = landcodes.readlines()
    for line in lines: 
        s = line.split(",")
        countryDictionary[s[0]] = Province(str(s[1]))
#print "this is the CountryDictionary", countryDictionary
# Maarten: als we de dictionary willen orderen, moeten we ze eerst nog sorteren, nu automatisch los door hashing van dictionary.

neighborDictionary = {}
with open("testneighbors.csv", "r") as neighbors:
    rows = neighbors.readlines()
    for row in rows: 
        n = row.split(",")
        neighborDictionary[n[0]] = n[1:-1]
#print "this is the neighborDictionary", neighborDictionary

#p = d["CRA"]
for n in countryDictionary:
    for m in neighborDictionary:
        if m == n:
            #(countryDictionary.get(n)).addNeighbor(neighborDictionary.get(m))
            for i in neighborDictionary.get(m):
                (countryDictionary.get(n)).addNeighbor(countryDictionary.get(i))

for n in countryDictionary:
    (countryDictionary.get(n)).setColor()

# print countryDictionary['cra'].color
# print countryDictionary['eri'].color
# print countryDictionary['war'].color
# print countryDictionary['ven'].color
# print countryDictionary['mer'].color
# print countryDictionary['law'].color
# print countryDictionary['mck'].color














