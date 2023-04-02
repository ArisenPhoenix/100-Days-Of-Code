class Dog:
    species = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = "ruf!"

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self):
        return f"{self.name} says {self.sound}"


class JackRussellTerrier(Dog):

    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
