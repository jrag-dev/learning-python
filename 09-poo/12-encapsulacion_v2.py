"""
    Implementación de un ejemplo mostrando como crear y trabajar con miembros privados
"""

class Base:
    def __init__(self):
        self._a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Llamando a miembros privados de la clase base: ")
        print(self.__c)


# main code
obj1 = Base()
print(obj1._a)

obj2 = Derived()