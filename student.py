from statistics import mean
from typing import  List


class Student:
    def __init__(self, imie, nazwisko, id):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.rok_urodzenia: int = 0
        self.pesel: int = 0
        self.id: int = id
        self.oceny: List[int] = [1, 4, 3]

    def dodaj_ocene(self, ocena: int):
        self.oceny.append(ocena)

    def pobierz_srednia_ocen(self):
        return self._licz_srednia_ocen()

    def _licz_srednia_ocen(self):
        srednia_ocen = round(mean(self.oceny), 2)

        return srednia_ocen
