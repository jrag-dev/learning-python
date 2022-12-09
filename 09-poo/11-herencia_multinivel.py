"""
    En la herencia multinivel, las caracteristicas de la clase base y la clase derivada
    se heredan en la nueva clase derivada. Esto es similar a una relación que representa
    a un niño y un abuelo.
"""

class Grandfather:

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


class Father(Grandfather):

    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        # constructor de grandfather
        Grandfather.__init__(self, grandfathername)


class Son(Father):

    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        # llamamos al constructor de la clase Father
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print("Grandfather name: ", self.grandfathername)
        print("Father name: ", self.fathername)
        print("Son name: ", self.sonname)


# main code
s1 = Son("Milán Alvarado", "José Alvarado", "Rafael Alvarado")
print(s1.grandfathername)
s1.print_name()