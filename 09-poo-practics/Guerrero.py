"""
    TODO: implementación de la clase Guerrero
"""
import random
from SerVivo import SerVivo

class Guerrero(SerVivo):
    __max_target = 10

    def __init__(self, name):
        SerVivo.__init__(self)
        self._target = self.__generateTargetToDie()
        self._name = name

    def get_name(self):
        return self._name

    def get_target(self):
        return self._target

    @staticmethod
    def gereraIntAleatorio(a, b):
        return random.randint(a, b)

    def shoot(self):
        """
            Shoot id the warrior is alive generating a random number between 0 and the __max_target
        :return: the number to shoot if the warrior is alive, -1 otherwise
        """
        if self._vivo:
            shot = Guerrero.gereraIntAleatorio(0, Guerrero.__max_target)
            print(self._name + " dispara " + str(shot))
            return shot
        else:
            return -1

    def get_shot(self, shot):
        """
        If the target is guessed by the shoot, then warrior dies
        :param shot: int with the shoot again the soldier.
        :return: True if the shot kills the warrior (shot is the target and the warrior is alive)
        False otherwise.
        """
        isTarget = False
        if self._vivo is True and self._target == shot:
            self._vivo = False
            isTarget = True
            print(self._name + " se muere por disparo " + str(shot))

        return isTarget

    def __generateTargetToDie(self):
        """
        Private method to generate the target to get shot
        """
        return Guerrero.gereraIntAleatorio(0, Guerrero.__max_target)

    def __str__(self):
        """ Override method toString to identify the objects and know their states"""
        return self._name

    @staticmethod
    def get_maxTarget():
        return Guerrero.__max_target


# main

guerrero = Guerrero("Goku")
print(guerrero)

shot = guerrero.shoot()
guerrero.get_shot(shot)