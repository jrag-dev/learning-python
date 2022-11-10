
class Player:
    def __init__(self):
        self.desc = None
        self.name = None

    def setName(self, name):
        self.name = name.title()

    def getName(self):
        return self.name

    def setDesc(self, desc):
        self.desc = desc.capitalize()

    def getDesc(self):
        return self.desc