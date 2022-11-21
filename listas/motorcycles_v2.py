"""
    Usando valores individuales de un lista
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

i = 0
while i < len(bicycles):
    print(bicycles[i])
    i = i + 1

mensaje = "My first bicycle was a {0!s}".format(bicycles[0].title())

print(mensaje)