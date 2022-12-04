"""
    Simulación de una cola de banco
"""

ultimo = 10
cola = list(range(1, ultimo + 1))

while True:
    print("\nExisten %d clientes en la cola" % len(cola))
    print("Cola actual: ", cola)
    print("Digite F para adicionar un cliente al final de la cola, ")
    print("o A para realizar la atención. S para salir.")

    operacion = input("Operación (F, A o S): ")

    if operacion == "A":
        if len(cola) > 0:
            atendido = cola.pop(0)
            print("Cliente %d atendido" % atendido)
        else:
            print("¡Cola vacía! Nadie para atender.")

    elif operacion == "F":
        ultimo += 1
        cola.append(ultimo)
    elif operacion == "S":
        break
    else:
        print("¡Operación inválida! ¡Digite solo F, A o S!")