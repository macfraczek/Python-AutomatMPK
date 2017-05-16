class Bla:
    def __init__(self, wartosc):
        self.zero=wartosc # pole publiczne
        self._raz=wartosc # pole prywatne
        self.__dwa=wartosc # pole bardziej prywatne?

obiekt=Bla(5)

# Które poprawnie wypisze wartości pól? Odkomentuj i sprawdź.
# print(moneta.zero)
# print(moneta._zero)
# print(moneta.__zero)
# print(moneta._Bla_zero)
# print(moneta._Bla__zero)
# print(moneta.__Bla_zero)
# print(moneta.__Bla__zero)
# print(moneta.raz)
# print(moneta._raz)
# print(moneta.__raz)
# print(moneta._Bla_raz)
# print(moneta._Bla__raz)
# print(moneta.__Bla_raz)
# print(moneta.__Bla__raz)
# print(moneta.dwa)
# print(moneta._dwa)
# print(moneta.__dwa)
# print(moneta._Bla_dwa)
# print(moneta._Bla__dwa)
# print(moneta.__Bla_dwa)
# print(moneta.__Bla__dwa)
# print("5")