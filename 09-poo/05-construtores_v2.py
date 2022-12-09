"""
    Implementación de una clase Addition con constructor parametrizado
"""

class Addition:
    first = 0
    second = 0
    answer = 0

    # constructor parametrizado
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# Creando un objeto de la clase
obj1 = Addition(1000, 2000)

# Creando un objeto de la misma clase
obj2 = Addition(10, 20)

# realizando la suma sobre obj1
obj1.calculate()

# realizando la suma sobre obj2
obj2.calculate()

# mostrando los resultados de obj1
obj1.display()

# mostrando los resultados sobre onj2
obj2.display()