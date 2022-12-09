"""

"""

class Base:
    def __init__(self):
        """ miembro protegido"""
        self._a = 2


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Llamando a miembros protegidos de la clase Base: ", self._a)

        self._a = 3
        print("Llamando al miembro modificado de la clase Base: ", self._a)


obj1 = Derived()
obj2 = Base()

print("Accediendo a el miembro protegido de obj1: ", obj1._a)

print("Accediendo al miembro protegido de obj2: ", obj2._a)