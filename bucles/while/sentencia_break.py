s = 0
while True:
    v = int(input("Digite un número a sumar o -1 para salir: "))

    if v == -1:
        break

    s = s + v

print("La sumatoria es: %s" % s)