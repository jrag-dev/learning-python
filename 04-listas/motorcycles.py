"""
    Cambiar, añadir y remover elementos de una lista
"""

motorcycles = ['honda', 'yamaha', 'suzuki']

for item in motorcycles:
    new_item = item.title()     # cambia el item
    print(new_item)
print("")

motorcycles[0] = 'ducati'   # modifica el item de la posición 0

for item in motorcycles:
    new_item = item.title()
    print(new_item)
print("")

motorcycles.append('honda')     # añade un elemento a la lista

for item in motorcycles:
    new_item = item.title()
    print(new_item)
print("")

motorcycles.insert(1, 'xavineta')

for item in motorcycles:
    new_item = item.title()
    print(new_item)
print("")

"""
    # remover elementos de la lista usando la declaración del
    Está se usa cuando se conoce de antemano la posición a eliminar
"""

print(motorcycles)
del motorcycles[0]
print(motorcycles)

"""
    # remover elementos de la lista usando el método pop()
    Esté se usa cuando tu quieres eliminar un elemento de la lista
    pero debes guardarlo para usarlo en otra parte del programa.
    
    Este método elimina el último elemento, a menos que le pasemos 
    la posición como parámetro.
"""
print("")

cars = ['audi', 'toyota', 'ford', 'chevrolet', 'fiat', 'mercedes']
print(cars)

popped_car = cars.pop()
print(cars)
print(popped_car)

cars = ['audi', 'toyota', 'ford', 'chevrolet', 'fiat', 'mercedes']

last_owned = cars.pop()
print("The las car I owned was a " + last_owned.title() + ".")
print("")

"""
    Eliminando items por su posición en la lista
"""

cars = ['audi', 'toyota', 'ford', 'chevrolet', 'fiat', 'mercedes']

first_owned = cars.pop(0)
print("The first car I owned was a " + first_owned.title() + ".")
print("")

"""
    Removiendo un item por su valor.
    
    Se usa cuando no sabemos su posición en la lista pero si su valor.
"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)

"""
    Se puede guardar primero el elemento a eliminar y luego usar el
    método remove() para eliminarlo de la lista
"""

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")