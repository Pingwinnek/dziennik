from typing import List
from student import Student

class Dziennik:
    def __init__(self, rok: int, litera: str):
        self._rok_szkolny: int = rok
        self._ktora_klasa_litera: str = litera
        self._uczniowie: List[Student] = []
        self.ostatni_id: int = 0

    def podaj_ilosc_studentow(self) -> int:
        ilosc_studentow = len(self._uczniowie)
        return  ilosc_studentow

    def dodaj_studenta(self, imie: str, nazwisko: str):
        id = self._generuj_id()
        s = Student(imie, nazwisko, id)
        self._uczniowie.append(s)

    def pobierz_studenta(self, id: int) -> Student:
        for uczen in self._uczniowie:
            if uczen.id == id:
                return uczen

    def _generuj_id(self) -> int:
        nowy_id = len(self._uczniowie) + 1
        return nowy_id
