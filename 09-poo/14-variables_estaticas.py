"""

"""


class CSStudent:
    stream = "cse"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


# main code
a = CSStudent("Geek", 1)
b = CSStudent("Nerd", 2)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)

# Las variables de clases pueden accederse usando las clases
print(CSStudent.stream)

# cambiando el valor de stream
a.stream = "ece"
print(a.stream)
print(b.stream)

# cambiando el stream para todas las instancias de la clase
CSStudent.stream = "mech"

print(a.stream)
print(b.stream)