"""
    Uso de *kwargs para establecer valores de objeto
"""

class Car:
    def __init__(self, **kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']


# main code

audi = Car(s=200, c='red')
bmw = Car(s=250, c='yellow')
mb = Car(s=190, c='blue')

print(audi.speed)
print(mb.color)