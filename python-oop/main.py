from classes import Dog, JackRussellTerrier

d = Dog("Spike", 2)
d.sound = "garr!"
print(d)
print(d.speak())

j = JackRussellTerrier("Jack", 4)
print(j.species)
print(j.speak())

