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


arrayColor = ["red", "orange", "yellow", "green", "purple", "blue"]

countryDictionary = {}
with open("Landcodes.csv", "r") as landcodes:
    lines = landcodes.readlines()
    for line in lines: 
        s = line.split(",")
        countryDictionary[s[0]] = s[1]
print countryDictionary

# class: land
class Province():
    """
    Een leeg vak op een kaart
    """
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.color = "?"



# p = d["CRA"]
# for n in [...]
#     np = d[n]
#     P.addNeighbour(NP)

# append etc. hier toevoegen
    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def checkColor(self, colorCountry):
        colorChecker = True
        for neighbour in self.neighbours:
            if colorCountry == neighbour.color:
                colorChecker = False
                return False
        return True

    def setColor(self):
        for color in arrayColor:
            if self.checkColor(color) == True:
                self.color = color
                break



# dit later zelf uit een ander bestand halen. Dit is de data

erie = Province("erie")
crawford = Province("crawford")
warren = Province("warren")

erie.addNeighbour(crawford)
erie.addNeighbour(warren)

crawford.addNeighbour(erie)
crawford.addNeighbour(warren)

erie.setColor()
crawford.setColor()
warren.setColor()

print erie.color, crawford.color, warren.color

# for line in file
#     s = line.split(",")
#     p = d(s[0])
#     for n in s[1:]


# p = d["CRA"]
# for n in [...]
#     np = d[n]
#     P.addNeighbour(NP)






#print arrayProvinces
