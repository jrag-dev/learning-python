"""
    Programa que permite acceder a las letras de una cadena de texto
"""

S = ["manzanas", "peras", "kiwis"]

for item in S:
    print(item)
    for j in item:
        if j == "e":
            j = "µ"
        print(j, end=" ")
    print("\r")


print("Otra forma de acceder: ")

print(S[0][0])
print(S[0][1])
print(S[1][1])
print(S[2][2])
