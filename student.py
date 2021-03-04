from typing import  List

class Student:
    def __init__(self, imie, nazwisko, id):
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.rok_urodzenia: int = 0
        self.pesel: int = 0
        self.id: int = id
        self.oceny: List[int] = []
