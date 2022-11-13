"""
    Preguntar al usuario una temperatura. Entonces, preguntar en que unidad está el valor
    ingresado Celsius o Fahrenheit. El programa debe convertir la temperatura a la otra
    unidad.
"""

head = """
    ************************************************************************
    |   Programa que realiza la conversión de una temperatura ingresada    |
    |   por el usuario en una unidad dada (Celsius o Fahrenheit) a otra    |
    |   unidad.                                                            |
    ************************************************************************
"""
print(head)

temp_celsius = 0.0
temp_fahrenheit = 0.0
unidad_in = ""
unidad_out = ""

temp = float(input("\tIngrese la temperatura: "))

menu = """
    Ingresar la unidad de la temperatura ingresada:
    
    Celsius     =>  1
    Fahrenheit  =>  2
"""
print(menu)

opcion = int(input("Ingresar tu respuesta: "))

if opcion == 1:
    unidad_in = "Celsius"
    unidad_out = "Fahrenheit"
    temp_celsius = temp
    temp_fahrenheit = (9*temp_celsius)/5 + 32
elif opcion == 2:
    unidad_out = "Celsius"
    unidad_in = "Fahrenheit"
    temp_fahrenheit = temp
    temp_celsius = (5*(temp_fahrenheit - 32))/9
else:
    print("\tOpción inválida!!")

sheet = """
    Temperatura de entrada: {0:10.2f} {1!s}
    Temperatura de salida: {2:10.2f} {3!s}
""".format(temp, unidad_in, (temp_celsius if opcion == 2 else temp_fahrenheit), unidad_out)
print(sheet)