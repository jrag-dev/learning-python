"""
    lista de números pares entre 1 y 10
"""

even_numbers = list(range(2, 11, 2))
print(even_numbers)

list_even_numbers = []
list_odd_numbers = []

for i in range(1, 11):
    if i % 2 == 0:
        list_even_numbers.append(i)
    else:
        list_odd_numbers.append(i)

print(list_even_numbers)
print(list_odd_numbers)
print("")

squares = []
for value in range(1, 11):
    square = value**2
    squares.append([value, square])

print(squares)

"""
    Estadistica simple con una lista de números
"""

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

minimo = min(digits)
maximo = max(digits)
suma = sum(digits)

sheet = """
    Mínimo: {0!s}
    Máximo: {1!s}
    Suma: {2!s}
""".format(minimo, maximo, suma)
print(sheet)

