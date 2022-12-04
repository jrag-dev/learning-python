plato = 5
pila = list(range(1, plato + 1))

while True:
    print("\nExisten %d platos en la pila" % len(pila))
    print("Pila actual: ", pila)
    print("Digite A para apilar un nuevo plato, ")
    print("o R para retirar de la pila. S para salir.")

    operacion = input("Operación (A, R o S): ")

    if operacion == "R":
        if len(pila) > 0:
            lavado = pila.pop(-1)
            print("Plato % lavado" % lavado)
        else:
            print("¡Pila vacía! Nada para lavar.")
    elif operacion == "A":
        plato += 1  # plato nuevo
        pila.append(plato)
    elif operacion == "S":
        break
    else:
        print("¡Operación inválida! ¡Digite solo A, R o S!")