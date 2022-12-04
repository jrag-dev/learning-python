"""
    Ordenar una lista de forma permanente con el método sort()
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
print(cars[::-1])


"""
    Ordenar una lista de forma temporar con el método sorted()
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)