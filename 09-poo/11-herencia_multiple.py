"""
    Cuando una clase puede derivar de más de una clase base, este tipo de herencia
    se denomina herencia múltiple. En herencias múltiples, todas las caracteristicas
    de las clases base se heredan en la clase derivada.
"""


class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)


class Father:
    fathername = ""

    def father(self):
        print(self.fathername)


# clase derivada
class Son(Mother, Father):
    def parents(self):
        print("Father: ", self.fathername)
        print("Mother: ", self.mothername)


# main code
s1 = Son()
s1.fathername = "Alvarado"
s1.mothername = "Hilda"
s1.parents()
