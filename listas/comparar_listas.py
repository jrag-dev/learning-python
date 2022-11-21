"""
    Programa que recibe dos listas (arreglos) de entrada y crea una tercera lista
    con los elementos de A y B pero sin elementos repetidos
"""


A = []
n = int(input("indicar la cantidad de elementos a ingresar: "))
i = 1
while i <= n:
    elemento = float(input("%d elemento del arreglo A es: " % i))
    A.append(elemento)
    i += 1

B = []
i = 1
while i <= n:
    elemento = float(input("%d elemento del arreglo B es: " % i))
    B.append(elemento)
    i += 1

C = A[:]
encontrados = []
indices_encontrados = []
Bnew = B[:]

i = 0
while i < len(A):
    j = 0
    while j < len(B):
        if A[i] == B[j]:
            encontrados.append(B[j])
            indices_encontrados.append(j)
            break
        j += 1
    i += 1

j = 0
k = 0
while j < len(indices_encontrados):
    Bnew.pop(indices_encontrados[j] - k)
    k += 1
    j += 1

C.extend(Bnew)

sheet = """
    A = {0!s}
    B = {1!s}
    Encontrados: {2!s}
    C = {3!s}
""".format(A, B, encontrados, C)
print(sheet)