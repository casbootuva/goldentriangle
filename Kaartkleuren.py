# Lonneke Lammers, Cas Boot, Alwin Lijdsman
# Heuristieken
# Kaartkleuren
#
#
# Last update: 2 november 2015 door Alwin Lonneke en Cas
#
# Vraag voor maarten:
# 1. Slaat onze class structuur ergens op? Zo ja, hoe zorgen
#    we dan dat deze ook echt goed is, (want nu slaat het nergens op)
# 2. Kan je lopen over een lijst met classes?
# 3.
#
# Comments Maarten intervisie 1:
# Pygon gebruiken om te visualiseren. Graph visualisatie Python zijn er wel libraries
#
#
#
#
#
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
with open("landcodes.csv", "r") as landcodes:
    lines = landcodes.readlines()
    for line in lines: 
        s = line.split(",")
        countryDictionary[s[0]] = Province(str(s[1]))
print "this is the CountryDictionary", countryDictionary

neighborDictionary = {}
with open("neighbors.csv", "r") as neighbors:
    rows = neighbors.readlines()
    for row in rows: 
        n = row.split(",")
        neighborDictionary[n[0]] = n[1:-1]
print "this is the neighborDictionary", neighborDictionary

#p = d["CRA"]
for n in countryDictionary:
    print n
    for m in neighborDictionary:
        if m == n:
            (countryDictionary.get(n)).addNeighbor(neighborDictionary.get(m))

print countryDictionary{'war'}

    #for m in neighborDictionary:

    #np = d[n]
    #p.addNeighbor(NP)

# dit later zelf uit een ander bestand halen. Dit is de data

# erie = Province("erie")
# crawford = Province("crawford")
# warren = Province("warren")

# erie.addNeighbor(crawford)
# erie.addNeighbor(warren)

# crawford.addNeighbor(erie)
# crawford.addNeighbor(warren)

# erie.setColor()
# crawford.setColor()
# warren.setColor()

# print erie.color, crawford.color, warren.color

# for line in file
#     s = line.split(",")
#     p = d(s[0])
#     for n in s[1:]


# p = d["CRA"]
# for n in [...]
#     np = d[n]
#     P.addNeighbour(NP)






#print arrayProvinces
