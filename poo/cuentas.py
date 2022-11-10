
class Cuenta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operaciones = []
        self.deposito(saldo)

    def resumen(self):
        print("CC Número: %s Saldo: %10.2f" % (self.numero, self.saldo))

    def extracion(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operaciones.append(["EXTRACCIÓN", valor, "APROBADA"])
        else:
            self.operaciones.append(["EXTRACCIÓN", valor, "RECHAZADA"])

    def deposito(self, valor):
        self.saldo += valor
        self.operaciones.append(["DEPÓSITO", valor, "EXITOSO"])

    def extracto(self, cliente):
        print("\nExtracto CC Nº %s" % self.numero)
        print("Cliente: %s\n" % cliente.nombre)
        for o in self.operaciones:
            print("%10s %10.2f %10s" % (o[0], o[1], o[2]))

        print("\n   Saldo: %10.2f\n" % self.saldo)


class CuentaEspecial(Cuenta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Cuenta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def extracion(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operaciones.append(["EXTRACCIÓN", valor, "APROBADA"])

    def extracto(self, cliente):
        print("\nExtracto CC Nº %s" % self.numero)
        print("Cliente: %s\n" % cliente.nombre)
        for o in self.operaciones:
            print("%10s %10.2f %10s" % (o[0], o[1], o[2]))

        print("\nSaldo: %10.2f \nLimite: %10.2f \nDisponible: %10.2f" % (self.saldo, self.limite, self.saldo + self.limite))