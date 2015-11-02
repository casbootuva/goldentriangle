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
# class: land
class provincie():
    """
    Een leeg vak op een kaart
    """
    def __init__(self, name):
        self.name = name

    def aangrenzendeLanden(self):
        self.aangrenzendeLanden = []
        
    def kleur(self):
        self.kleur = 0
  
#erie = provincie("erie"):
#    self.aangrenzendeLanden.append("crawford", "warren")

warren = provincie("warren")
warren.aangrenzendeLanden("erie", "crawford")

    
# aray van landen (classes)
arrayLanden = [erie, warren, crawford]

# algoritme om te bepalen hoeveel kleuren er minimaal nodig zijn


for provincie in range (0, arrayLanden):
        i = 0
	if arrayLanden[j] raakt provincie waar colour != rood(0)
		arrayLanden[j].kleur = i
		i++
		return to begin

	    
	else if provincie raakt landen waar colour != geel
		land.colour = i
		i = i + 2
	else if i raakt landen waar colour != groen
		colour = groen
		return begin
	else if i raakt landen waar colour != oranje
		colour = oranje
		return begin

# print visualisatie


