class Fighter:
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10

	def attack(self, other_guy):
		other_guy.health = other_guy.health - self.damage

omar = Fighter("Omar")
joe = Fighter("Joe")

print(omar.name)
print(joe.name)

joe.attack(omar)

print(omar.health)