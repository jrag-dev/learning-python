"""
    A continuación mostramos como crear listas
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

i = 1
for item in bicycles:
    print("%d. %s" % (i, item))
    i += 1

print("bicycles[0]: %s" % bicycles[0])
print("bicycles[-1]: %s" % bicycles[-1])    # imprime el último elemento de la lista
print("bicycles[-2]: %s" % bicycles[-2])
print("bicycles[::-1]: %s" % bicycles[::-1])    # imprime la lista de atrás hacia adelante

print(bicycles[0].title())