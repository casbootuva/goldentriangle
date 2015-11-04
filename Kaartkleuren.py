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
 #       self.neighbours = []

# append etc. hier toevoegen
    def addNeighbour(self, neighbours):
        self.neighbours.append = []
        
    def colour(self):
        self.kleur = 0

# dit later zelf uit een ander bestand halen. Dit is de data

erie = Province("errie")
crawford = Province("crawford")
warren = Province("warren")

# Hier wordt alles gekoppeld
warren.addNeighbour(erie)
warren.addNeighbour(crawford)
    
# aray van landen (classes)
arrayProvinces = [erie, warren, crawford]

# algoritme om te bepalen hoeveel kleuren er minimaal nodig zijn

"""
for provincie in range (0, arrayLanden):
        i = 0
	if arrayLanden[j] raakt provincie waar colour != rood(0)
		arrayLanden[j].kleur = i
		i++
		return to begin
	    
	else if provincie raakt 5landen waar colour != geel
		land.colour = i
		i = i + 2
	else if i raakt landen waar colour != groen
		colour = groen
		return begin
	else if i raakt landen waar colour != oranje
		colour = oranje
		return begin

# print visualisatie
"""

print arrayProvinces

