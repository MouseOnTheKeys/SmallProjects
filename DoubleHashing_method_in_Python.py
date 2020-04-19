"""
Student:
Nenad Bubalo 1060/19

12. April 2019

Podaci se smeštaju u heš tabelu sa 7 ulaza primenom
metode otvorenog adresiranja sa dvostrukim
heširanjem. Primarna heš funkcija je hp(K)=K mod 7, a
sekundarna heš funkcija je hs(K)=2 + (K mod 3).
Prikazati popunjavanje tabele ako redom dolaze
ključevi 45, 35, 17, 25, 18.
Napomena: Funkcija u slucuju kolizije: hi(K+1)= (hp(K)
+ hs(K)) mod n.

"""

class Element:
    def __init__(self, kljuc, vrednost):
        self.kljuc = kljuc
        self.vrednost = vrednost
        self.sledeci = None

class HashTabela:
    def __init__(self, limit):
        self.tabela = [None] * limit
        self.limit = limit

    def hp(self, kljuc):
        return kljuc % self.limit

    def hs(self, kljuc):
        return 2 + (kljuc % 3)


    # Ubacivanje elemenata sa resavanjem kolizije dvostrukim hesiranjem
    def ubaci(self, kljuc, vrednost):
        print('')
        print('Postupak ubacivanja za element {}:'.format(kljuc))

        broj_ulaza = self.hp(kljuc)
        novi = Element(kljuc, vrednost)
        if self.tabela[broj_ulaza] is None:
            self.tabela[broj_ulaza] = novi
            print('Element {} je na mestu {}'.format(str(novi.kljuc), str(broj_ulaza)))
        else:
            while self.tabela[broj_ulaza] is not None:
                print("Desila se koalizija za element " + str(kljuc) + " na poziciji " + str(
                    broj_ulaza) + " trazi se nova pozicija.")
                broj_ulaza = (broj_ulaza + self.hs(kljuc)) % self.limit
            self.tabela[broj_ulaza] = novi
            print('Nova pozicija za element {} je {}'.format(str(kljuc), str(broj_ulaza)))


    def prikaz(self):
        print('Hes tabela dvostrukim hesiranjem je: ')
        for count, element in enumerate(self.tabela):
            if element is not None:
                print('Na poziciji {} je ({}, {})'.format(str(count), str(element.kljuc), str(element.vrednost)))
                element = element.sledeci
            else:
                print('Na poziciji {} je None'.format(str(count)))


    def dohvati(self, kljuc):
        broj_ulaza = self.hesFunkcija(kljuc)
        tekuci = self.tabela[broj_ulaza]
        while tekuci is not None:
            if tekuci.kljuc == kljuc:
                return tekuci.vrednost
            tekuci = tekuci.sledeci
        return None

    def izbaci(self, kljuc):
        broj_ulaza = self.hesFunkcija(kljuc)
        tekuci = self.tabela[broj_ulaza]
        prethodni = None
        while tekuci is not None:
            if tekuci.kljuc == kljuc:
                if prethodni is None:
                    self.tabela[broj_ulaza] = tekuci.sledeci
                else:
                    prethodni.sledeci = tekuci.sledeci
            prethodni = tekuci
            tekuci = tekuci.sledeci


if __name__ == '__main__':

    print('Domaci Zadatak 1:')

    tabela = HashTabela(7)

    kljucevi = [45, 35, 17, 25, 18]
    podaci = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']

    for i in range(5):
        tabela.ubaci(kljucevi[i], podaci[i])

    print('')
    tabela.prikaz()
    print('')




