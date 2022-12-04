"""
    usando listas calcular la media de notas de un alumno
"""

notas = [6, 7, 5, 8, 9]

suma = 0
x = 0

while x < len(notas):
    suma = suma + notas[x]
    x = x + 1

print("Media: %s" % (suma/x))

head = """
    Programa que permite ingresar las notas de un alumno y calcular
    la media del año escolar.
"""
print(head)

notas = []
n = int(input("indicar la cantidad de notas a ingresar: "))
i = 1
while i <= n:
    elemento = float(input("%d elemento del arreglo de notas: " % i))
    notas.append(elemento)
    i += 1

suma = 0
x = 0

while x < len(notas):
    suma = suma + notas[x]
    x = x + 1

print("Media: %s" % (suma/x))