"""
    Implementación de un ejemplo con herencia multi nivel
"""

class Base(object):
    """
        Constructor
    """
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


# clase que hereda de Base
class Child(Base):
    """
        Constructor
    """
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def getAge(self):
        return self.age


# clase que hereda de Child
class GrandChild(Child):
    """
        Constructor
    """
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def getAddress(self):
        return self.address


# main code
g = GrandChild("Nevado", 25, "Calle Vargas")

print("{0} {1} {2}".format(g.getName(), g.getAge(), g.getAddress()))