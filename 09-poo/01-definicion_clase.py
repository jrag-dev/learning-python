"""
    Implementacion de una clase en python
"""

class Dog:
    """ Atributos """
    attr1 = "mammal"
    attr2 = "dog"

    """ método"""
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


Rodger = Dog()

# accediendo a los métodos y atributos de la clase Dog
print(Rodger.attr1)
Rodger.fun()