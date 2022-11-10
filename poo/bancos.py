
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []
        self.cuentas = []

    def abre_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def lista_cuentas(self):
        for c in self.cuentas:
            c.resumen()