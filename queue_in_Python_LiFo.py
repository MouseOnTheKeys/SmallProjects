"""
Student:
Nenad Bubalo 1060/19

29. Mart 2019

Domaci Zadatak Redovi:
U programskom jeziku Python implementirati red. U
implementaciji napisati funkciju dodavanja elemenata u
red. Prilikom implementacije koristiti ubacivanje na kraj i
koristiti ulančanu reprezentaciju reda. Pored funkcije
dodavanja elemenata napisati i jednu funkciju koja će iz
reda obrisati sva pojavljivanja zadatog broja. U glavnom
programu inicijalizovati red, dodati elemente
2,3,5,6,9,2,1,5,6,8 i iz reda izbaciti sva pojavljivanja broja
2.
"""


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedQueue(object):
    def __init__(self):
        self.prvi = None
        self.poslednji = None

    def is_empty(self):
        return self.prvi is None

    def add(self, value):
        novi = Node(value)
        if self.prvi is None:
            self.poslednji = self.prvi = novi
            return
        self.poslednji.next = novi
        self.poslednji = novi

    def remove(self):
        if self.prvi is None:
            print("Red je prazan")
            return
        value = self.prvi.value
        self.prvi = self.prvi.next
        return value

    # Ova funkcija uklanja sve vrednosti u redu, trazena funkcija u zadatku
    def ukoni_vrednost(self, value_ukloni):
        if self.prvi == None:  # ako je red prazan onda nista
            return
        while self.prvi.value == value_ukloni:
            self.prvi = self.prvi.next
        if self.prvi == None:  # provera da li je lista prazna
            return

        trenutni = self.prvi
        while trenutni.next != None:
            if trenutni.next.value == value_ukloni:
                trenutni.next = trenutni.next.next
            else:
                trenutni = trenutni.next  # ne uklanja nego obilazi cvor
        return

    def peek(self):
        return self.prvi.value

    def print(self):
        tekuci = self.prvi
        while tekuci:
            print(tekuci.value)
            tekuci = tekuci.next


if __name__ == "__main__":

    # incijacija i implementacija reda
    red = LinkedQueue()
    # dodavanje reda odredjenih elemenata u red
    lst = [2, 3, 5, 6, 9, 2, 1, 5, 6, 8]

    for i in lst:
        red.add(i)
    # stampanje unetog reda
    print("Vrednosti u redu su:")
    red.print()
    print("")
    # uklanjanje trazene vrednosti (2) iz reda
    print("Elementi reda posle uklanjanja elemenata sa vrednostima: 2 ")
    red.ukoni_vrednost(2)
    # Stampanje reda bez uklonjenih elemenata
    red.print()
