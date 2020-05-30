# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:30:53 2020
ASP - Vezbe 12
@author: Nenad Bubalo 1060/19

    Domaci Zadatak 12:
    
    U programskom jeziku Python, napraviti klasu osoba koja sadrži atribute ime, prezime, pol i jmbg.
    Proizvoljno napraviti niz od deset osoba i pronaći osobu sa određenim jmbg-om. Nakon pronalaska osobe
    ispisati ime, prezime i pol osobe.

"""

class Osoba:
    def __init__(self, ime, prezime, jmbg, pol):
        self.ime = ime
        self.prezime = prezime
        self.jmbg = jmbg
        self.pol = pol
        
def linear_search(niz, jmbg):
    for i in range(0, len(niz)):
        if niz[i].jmbg == str(jmbg):
            return "\nIme: {}\nPrezime: {}\nPol: {}\n".format(niz[i].ime, niz[i].prezime, niz[i].pol)
       
    return 'Ne postoji osoba sa trazenim JMBG-om !!!'


if __name__ == '__main__':


    # Proizvoljnih 10 osoba
    o1 = Osoba('Alex', 'Aleksic', '1505991764879', 'Muski')
    o2 = Osoba('Borko', 'Borkic', '2402990725496', 'Muski')
    o3 = Osoba('Cakana', 'Cakic', '2311990725496', 'Zenski')
    o4 = Osoba('Dejan', 'Dekic', '1044990725496', 'Muski')
    o5 = Osoba('Emina', 'Emic', '1003987725497', 'Zenski')
    o6 = Osoba('Filip', 'Fiksic', '1002990725496', 'Muski')
    o7 = Osoba('Gordana', 'Gocic', '1011990725496', 'Zenski')
    o8 = Osoba('Hogar', 'Horic', '0902990725496', 'Muski')
    o9 = Osoba('Janko', 'Janic', '0502997725496', 'Muski')
    o10 = Osoba('Ivona', 'Ivic', '17029720729136', 'Zenski')

    # Niz od 10 osoba
    niz = [o1, o2, o3, o4, o5, o6, o7, o8, o8, o9, o10]

    # Unos trazenog JMBGa
    jmbg = input('Za primer zadatka uneti ili kopirati broj: 1044990725496\nUnesite JMBG: \t')

    # Pozivanje funkcije linearnog trazenja i zapisivanja na novu varijablu rezultat
    rezultat = linear_search(niz, jmbg)

    # Print Rezultata
    print(rezultat)
