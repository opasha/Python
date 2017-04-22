class Fighter:
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10

	def attack(self, other_guy): 
		other_guy.health = other_guy.health - self.damage #other_guy is omar, self is joe
		print("{} attacks {}!".format(self.name, other_guy.name))
		print("{} loses {} health points!".format(other_guy.name, self.damage))
	
	def __str__(self):
		return "{}: {}".format(self.name, self.health) #overrides the print method to make things cleaner

omar = Fighter("Omar")
joe = Fighter("Joe")

print(omar) # Omar: 100 
print(joe)

joe.attack(omar)
print(omar)

class Boxer(Fighter):
	def heal(self):
		self.health += 10


boxer_omar = Boxer("Boxer Omar")
print(boxer_omar)
print(boxer_omar.damage)
print(boxer_omar.health)

boxer_omar.heal()

print(boxer_omar)