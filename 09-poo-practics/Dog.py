from Animal import Animal

class Dog(Animal):
    """
        This class inherits all attributes and methods from the Animal class.
        A class used to represent a Dog
    """

    # constructor method
    def __init__(self, age="0", name="Toby", pastor=True):
        Animal.__init__(self, age, name)
        self.pastor = pastor

    # news getters and setters methods
    def set_pastor(self, pastor):
        self.pastor = pastor

    def get_pastor(self):
        return self.pastor

    # overwritten method
    def greeting(self, greet="Guau", receptor="new friend"):
        return greet + " " + receptor


# main
def main():
    dog = Dog("3", "Duque")
    print(dog)
    dog.die_out()
    print(dog)
    print(dog.greeting())
    print(dog.get_name())


if __name__ == "__main__":
    main()