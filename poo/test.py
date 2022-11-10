from clientes import Cliente
from cuentas import Cuenta, CuentaEspecial
from bancos import Banco

juan = Cliente("Juan da Silva", "0414-820-9966")
maria = Cliente("Maria Silva", "0412-8887744")
jose = Cliente("José Alvarado", "0414-8206097")
cuenta1 = Cuenta([juan], 1, 1000)
cuenta2 = CuentaEspecial([maria, juan], 2, 500)
cuenta3 = Cuenta([jose], 3, 2000)

tatu = Banco("Tatú")

tatu.abre_cuenta(cuenta1)
tatu.abre_cuenta(cuenta2)
tatu.abre_cuenta(cuenta3)

cuenta1.extracion(50)
cuenta2.deposito(300)
cuenta1.extracion(190)
cuenta2.deposito(95.15)
cuenta2.extracion(250)
cuenta1.extracion(780)
cuenta2.deposito(780)
cuenta1.extracto(juan)
cuenta2.extracto(maria)

cuenta3.extracion(680)
cuenta3.extracto(jose)

tatu.lista_cuentas()