class Animal:
	def __init__(self, name):
		self.name = name

	def talk(self):
		pass

pet_omar = Animal("Omaroo")
print(pet_omar.name)
print(pet_omar.talk())

class Dog(Animal):
		def talk(self):
			return "WOOF"

pet = Dog("Dot")
print(pet.name)
print(pet.talk())

class Cat(Animal):
	def talk(self):
		return "MEOW"

kitten = Cat("Garfield")
print(kitten.name)
print(kitten.talk())