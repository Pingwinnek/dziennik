from dziennik import Dziennik

d = Dziennik(rok= 2021, litera= "c")
d.dodaj_studenta(imie="Jan", nazwisko="Nowak")
d.dodaj_studenta(imie="Jan", nazwisko="Kowalski")
print(d.podaj_ilosc_studentow())
