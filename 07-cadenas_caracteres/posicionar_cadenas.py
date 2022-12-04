"""
    Métodos para mostrar cadenas de caracteres de forma más interesantes.
"""

s = "tigre"
print("X" + s.center(20) + "X")

print("X" + s.center(20, ".") + "X")

# # para completar la cadena con espacios a la izquierda utilizar => ljust
print(s.ljust(20, ":"))


i = 0
while i <= 5:
    p = "*"
    j = 0
    while j < 5:
        print(p.ljust(j, ":"))
        j += 1
    k = 5
    while k >= 1:
        print(p.rjust(k, ":"))
        k -= 1
    print("\r")
    i += 1