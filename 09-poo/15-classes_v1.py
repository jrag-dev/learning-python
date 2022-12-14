"""
    Implementación de clases en python
"""

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

    def __str__(self):
        print("\nDetails Product: ")
        print("Name: {0:.>15s} \nPrice: {1:.>12d} \nQuantity: {2:.>7d}".format(self.name, self.price, self.quantity))


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 890, 4)

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

print(type(item2))
print(type(item2.name))
print(type(item2.price))
print(type(item2.quantity))

print(item1.__str__())
print("Total: {0:.>12}".format(item1.calculate_total_price()))

print(item2.__str__())
print("Total: {0:.>12}".format(item2.calculate_total_price()))