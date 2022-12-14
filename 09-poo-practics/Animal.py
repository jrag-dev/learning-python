"""
    Implementación de una clase padre y una clase hija, aplicando herencia
"""

class Animal:
    numAnimals = 0

    def __init__(self, age="0", name="Godzilla"):
        """
        CONSTRUCTOR DE AN ANIMAL CLASS
        :param age: age of the animal: By default -> 0
        :param name:  name of the animal: By default -> Godzilla
        """
        self.age = age
        self.name = name
        self.live = True
        Animal.numAnimals += 1

    # GETTERS AND SETTERS
    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_live(self, live):
        self.live = live

    def get_live(self):
        return self.live

    # Methods of the class. There methods are instantiated by INSTANCES of the class
    def greeting(self, greet="Hello", receptor="new friend"):
        print(greet + " " + receptor)

    def die_out(self):
        if self.live:
            self.live = False
        Animal.numAnimals -= 1

    def __eq__(self, other):
        """
        Overwrites the equality method of two instances of Animal.
        They are considered equal if they have the same name
        :param other: another object
        :return: False if the objects no equals, True contrary case
        """
        if other is None:
            return False
        if isinstance(other, Animal):
            if self.get_name() == other.get_name():
                return True
            return False

    def __str__(self):
        """
        Overwrites the str method of the animal instance
        They are considered equal if they have the same name
        :return:
        """
        if self.live is False:
            return "Soy " + self.name + " y tenia " + str(self.age) + " años cuando fallecí"
        else:
            return "Soy " + self.name + " y tengo " + str(self.age) + " años." + "¡La vida es maravillosa!"

    @staticmethod
    def get_numAnimals():
        return Animal.numAnimals