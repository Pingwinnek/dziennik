from dziennik import Dziennik

dziennik = Dziennik(rok= 2021, litera="c")

dziennik.dodaj_studenta(imie="Maciej", nazwisko="Nowak")
dziennik.dodaj_studenta(imie="Jan", nazwisko="Kowalski")

student = dziennik.pobierz_studenta(id=2)
print(student.pobierz_srednia_ocen())
#print(dziennik.podaj_ilosc_studentow())
