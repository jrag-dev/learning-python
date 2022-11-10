"""
    Banco Tatu:
    Hacer un programa para controlar el saldo de sus cuentacorrentistas. Cada
    cuenta corriente puede tener uno o más clientes como titular. El banco
    controla sólo el nombre y teléfono de cada cliente. La cuenta corriente
    presenta un saldo y una lista de operaciones de extraciones y depósitos.
    Cuando un cliente realice una extracción, disminuiremos el saldo de la
    cuenta  corriente. Cuando se realice un depósito aumentaremos el saldo.
    Por ahora, el banco Tatu no ofrece cuentas especiales, osea el cliente
    no puede sacar más dinero de lo que su cuenta le permite.
"""

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def resumen(self):
        print("Nombre: %s \nTeléfono: %s" % (self.nombre, self.telefono))
