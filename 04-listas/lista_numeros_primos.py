"""
    Programa que muestra los números enteros entre 0 y n, donde n es un entero positivo
"""

n = int(input("Introduce el valor maximo: "))

primos = []

for numero in range(2, n + 1):
    # determinamos si numero es primo
    creo_que_es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            creo_que_es_primo = False
            break

    # Y si es primo, lo añadimos a la lista
    if creo_que_es_primo:
        primos.append(numero)

print(primos)
