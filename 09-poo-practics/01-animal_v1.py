"""
    Definición de una clase en Python
"""

class Animal:

    numAnimales = None  # variable estática

    def __init__(self, age="0", name="Godzilla"):
        """
        constructor of an animal
        :param age: age of the animal: By default -> 0
        :param name: name of the animal: By default -> Godzilla
        """
        self.__tipo = "Animal"  # Atributo private
        self.age = age      # Atributo public
        self.name = name    # Atributo public
        self.vivo = True    # Atributo public
        Animal.numAnimales += 1

    def greeting(self, saludo="Hello", receptor="nuevo amigo"):
        print(saludo + " " + receptor)

    @staticmethod
    def add(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return " ".join((a, b))
        else:
            raise TypeError

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)