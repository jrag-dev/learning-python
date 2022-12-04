"""
    Escribir un programa que copie los números impares y números para en otras listas
    individuales
"""

V = [9, 8, 7, 12, 0, 13, 21]

P = []
I = []

for item in V:
    if item % 2 == 0:
        P.append(item)
    else:
        I.append(item)

print("Todos: ", V)
print("Pares: ", P)
print("Impares: ", I)