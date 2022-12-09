"""
    Uso de *args para establecer valores de objeto
"""

class Car:
    def __init__(self, *args):
        self.speed = args[0]
        self.color = args[1]


# main code
audi = Car(200, 'red')
bmw = Car(250, 'black')
mb = Car(190, 'white')

print(audi.color)
print(bmw.speed)