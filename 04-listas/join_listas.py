"""
    Haga un programa que lea dos listas y que genere una tercera con los elementos
    de las dos primeras
"""

A = []
B = []
C = []
D = []

print("Elementos de la lista A: ")
while True:
    n = int(input("Ingrese un número (0 para salir): "))
    if n == 0:
        break
    A.append(n)

print("Elementos de la lista B: ")
while True:
    elem = int(input("Ingrese un número (0 para salir): "))
    if elem == 0:
        break
    B.append(elem)

i = 0
while i < len(A):
    print("i: ", i)
    j = 0
    while j < len(B):
        print("j: ", j, end=" ")
        j += 1
    print("\n")
    i += 1

# C = 1er elemento de A, 1er elemento de B, 2do elemento de A, 2d0 elemento de A, ...
i = 0
while i < len(A):
    C.append(A[i])
    j = 0
    while j < len(B):
        if i == j:
            C.append(B[j])
        j += 1
    i += 1

print(A)
print(B)
print(C)
print("")

# C = producto 1er elem de A por el 1er elemento de B, producto 2do elem de A por 2do elem de B, ...
i = 0
while i < len(A):
    j = 0
    while j < len(B):
        if i == j:
            prod = A[i]*B[j]
            D.append(prod)
        j += 1
    i += 1

print(A)
print(B)
print(D)
print("")

# F = generada con los elementos de A y B
i = 0
encontrados = []
aux = B[:]
F = A[:]
print(F)
print("")
while i < len(A):
    j = 0
    while j < len(B):
        if A[i] == B[j]:
            encontrados.append(B[j])
        j += 1
    i += 1

print(A)
print(B)
print(F)
print(encontrados)
print("aux: ", aux)
print("")

i = 0
j = 0
while i < len(aux):
    while j < len(encontrados):
        if encontrados[j] == aux[i]:
            print("encontrados[j]: aux[i]: ", aux[i])
        j += 1
    i += 1

print(A)
print(B)
print("aux: ", aux)
print("")