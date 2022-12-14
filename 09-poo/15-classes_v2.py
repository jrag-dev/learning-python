"""
    Ejemplo de clases en python
"""

class Drink:
    def __init__(self, name):
        self.__name = name

    def getDetail(self):
        return "La bebida es: " + self.__name


class Product:
    def __init__(self, cost, price):
        self.cost = cost
        self.price = price

    def getGain(self):
        return self.price - self.cost

class Beer(Drink, Product):

    Count = 0
    def __init__(self, name, brand, alcohol, cost, price):
        Drink.__init__(self, name)
        Product.__init__(self, cost, price)
        self.__brand = brand
        self.__alcohol = alcohol
        Beer.Count += 1

    def getDetail(self, text=""):
        return text + super().getDetail() + ", de la marca: " + self.__brand + ", con alcohol: " + str(self.__alcohol)

    @staticmethod
    def getClassInfo():
        return "Se han creado " + str(Beer.Count) + " objetos"


# main code
drink = Drink("agua")
print(drink.getDetail())

beer1 = Beer("Polarcita", "Polar", 4.5, 10, 24)
print(beer1.getDetail())
print(beer1.getGain())

beer2 = Beer("Regional Verde", "Regional", "5.0", 6, 18)
print(beer2.getDetail("Info: "))
print(beer2.getGain())

beer3 = Beer("Branhma", "Regional", "6.0", 14, 21)
print(beer3.getDetail())
print(beer3.getGain())

print(Beer.Count)
print(Beer.getClassInfo())