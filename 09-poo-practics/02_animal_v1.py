"""
    Definición de una clase en Python
"""

class Animal:

    numAnimales = 0  # variable estática

    def __init__(self, age="0", name="Godzilla"):
        """
        constructor of an animal
        :param age: age of the animal: By default -> 0
        :param name: name of the animal: By default -> Godzilla
        """
        self.__tipo = "Animal"  # Atributo private
        self.age = age      # Atributo public
        self.name = name    # Atributo public
        self.live = True    # Atributo public
        Animal.numAnimales += 1

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    @staticmethod
    def get_numAnimals():
        return Animal.numAnimales

    def die_out(self):
        if self.live:
            self.live = False
        Animal.numAnimales -= 1


# main code
animal1 = Animal("4", "Nevado")
print(animal1.getName())
print(Animal.get_numAnimals())

animal2 = Animal("1", "Miu miu")
print(animal2.getName())
print(Animal.get_numAnimals())

animal2.die_out()
print(Animal.get_numAnimals())