"""
    Uno de los usos del polimorfismo en python
"""


class India:
    def __init__(self, capital, language, istype):
        self.capital = capital
        self.language = language
        self.istype = istype

        print("Se ejecutó el constructor de India")

    def mostrar_datos(self):
        print("\nCapital: {0} \nLenguaje: {1} \nTipo de País: {2}\n".format(self.capital, self.language, self.istype))


class Usa:
    def __init__(self, capital, language, istype, nuclear):
        self.capital = capital
        self.language = language
        self.istype = istype
        self.nuclear = nuclear

        print("Se ejecutó el constructor de Usa")

    def mostrar_datos(self):
        print("\nCapital: {0} \nLenguaje: {1} \nTipo de País: {2} \nPotencia nuclear: {3}\n".format(self.capital, self.language, self.istype, self.nuclear))


# main code
india = India("New Delhi", "Hindi", "developing")
usa = Usa("Washington", "English", "developing", "Nuclear army")

india.mostrar_datos()
usa.mostrar_datos()
