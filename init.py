class Colleague:

    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age


tom = Colleague('Tom', 'developer', 35)
omar = Colleague('Omar', 'programmer', 29)

print(tom.name)
print(omar.name)

print(tom.position)
print(omar.position)

print(tom.age)
print(omar.age)