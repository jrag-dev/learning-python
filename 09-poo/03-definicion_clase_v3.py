"""
    aprenderemos sobre variables de clases e instancia de una clase

    Las variables de instancia son para datos, únicos para cada instancia y las
    variables de clase son para atributos y métodos compartidos por todas las
    instancias de la clase.
"""


class Dog:

    """ Variables de clase"""
    animal = 'dog'

    # método init o constructor
    def __init__(self, breed, color):
        """
            variables de instancia
            :param breed:
            :param color:
        """
        self.breed = breed
        self.color = color


# Objetos de la clase Dog
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print("Rodger details:")
print("Rodger is a", Rodger.animal)
print("Breed: ", Rodger.breed)
print("Color: ", Rodger.color)

print("\nBuzo details:")
print("Buzo is a", Buzo.animal)
print("Breed: ", Buzo.breed)
print("Color: ", Buzo.color)

# Las variables de clases pueden ser accedidas usando clases
print("\nAccediendo a varieble de clase usando el nombre de la clase")
print(Dog.animal)