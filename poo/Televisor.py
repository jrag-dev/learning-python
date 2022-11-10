class Televisor:
    def __init__(self, canal, minimo=2, maximo=14):
        self.encendido = False
        self.canal = canal
        self.marca = "Lg"
        self.size = "32 pulgadas"
        self.minimo = minimo
        self.maximo = maximo

    def toString(self):
        print("Bienvenido querido usuario!")
        if self.encendido:
            print("La tv se encuentra encendida")
        else:
            print("La tv se encuentra apagada")

    def cambia_canal_para_abajo(self):
        if self.canal - 1 >= self.minimo:
            self.canal -= 1
        elif self.canal == self.minimo:
            self.canal = self.maximo

    def cambia_canal_para_arriba(self):
        if self.canal + 1 <= self.maximo:
            self.canal += 1
        elif self.canal == self.maximo:
            self.canal = self.minimo

    def cambia_canal_pasado(self, canal):
        if self.minimo < canal < self.maximo:
            self.canal = canal


tv = Televisor(4)
tv.encendido = True
tv.toString()
print(tv.canal)

if tv.encendido:
    print("La tv está encendida")

tv.cambia_canal_para_abajo()
print(tv.canal)

tv.cambia_canal_para_arriba()
tv.cambia_canal_para_arriba()
tv.cambia_canal_para_arriba()
print(tv.canal)

tv.cambia_canal_pasado(2)
print("Canal Actual: ", tv.canal)
tv.cambia_canal_para_abajo()
print(tv.canal)
tv.cambia_canal_para_abajo()
print(tv.canal)
tv.cambia_canal_para_abajo()
print(tv.canal)

tv.cambia_canal_pasado(89)
print(tv.canal)
tv.cambia_canal_para_arriba()
print(tv.canal)
tv.cambia_canal_para_arriba()
print(tv.canal)
tv.cambia_canal_para_arriba()
print(tv.canal)
