"""
    Implementación de una clase Fecha
"""


class Fecha:
    """
        TODO CLASS DOCUMENTAION
    """

    def __init__(self, day=1, month=1, year=1970):
        """
        TODO DOCUMENTATION OF CONSTRUCTOR AND EXCEPTION HANDLING
        (Type and value control)
        :param day:
        :param month:
        :param year:
        """
        self._day = day
        self._month = month
        self._year = year

    # GETTERS AND SETTERS
    def set_day(self, day):
        self._day = day

    def get_day(self):
        return self._day

    def set_month(self, month):
        self._month = month

    def get_month(self):
        return self._month

    def set_year(self, year):
        self._year = year

    def get_year(self):
        return self._year

    def __str__(self):
        return str(self._day) + "/" + str(self._month) + "/" + str(self._year)


class FechaNueva(Fecha):

    def __init__(self, day=1, month=1, year=1970):
        Fecha.__init__(self, day, month, year)

    def __str__(self):
        return "{0}-{1}-{2}".format(self._day, self._month, self._year)
