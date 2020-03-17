# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:56:07 2020

@author: Nenad
"""

import random
import string

"""
Domaci zadatak 1
Program napisan sa exeptionom ako user unese 0 
odnosno napravi praznu listu, problem unosa karaktera nije ispravljen

"""

print('Domaci zadatak 1')

def kreiranje_lista():
    m = int(input("Unesite broj clanova liste 1 :  "))
    if m == 0:
        
        print('Kreirali ste praznu listu !!!')
        lista1=[]
    else:
        lista1 = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for i in range(m) ]
        print(lista1)
    
    k = int(input("Uneti broj clanova liste 2:  "))
    if k == 0:
        print('Kreirali ste praznu listu !!!')
        lista2=[]
    else:
        lista2 = [random.randint(0,100) for i in range(k)]
        print(lista2)
    return lista1, lista2

def spajanje(): # funkcija dogranicava usera da stavi obe liste prazne
    lista1,lista2 = kreiranje_lista()
    if len(lista1)==0 and len(lista2)==0 :
       print('Unesite neke clanove liste') 
       spajanje()
    else:
        nova = lista1 + lista2
        return print('\nSpojena lista ima vrednosti: \n{}'.format(nova))

print('')

spajanje()

print('')

"""
Domaci zadatak 2
Program napisan sa exeptionom ako korisnik unese 0 ili praznu listu
Problem unosa karaktera umesto integera nije ispravljen 

"""

print('Domaci zadatak 2')
print('')

n = int(input("Uneti broj clanova liste brojeva:  "))

lista5 = [random.randint(0,100) for i in range(n)]
          
print("Clanovi random generisane liste su {}".format(lista5))

 
def maliveliki():
    if len(lista5) == 0:
        print('Morate uneti meki clan niza')
    else:
        return print("Element minimalne vrednosti u listi je {}, \na element maksimalne vrednosti je {}".format(min(lista5),max(lista5)))
print('')

maliveliki()


# komentujte liniju ispod ako pokrecete program ne pokrecete direktno iz command line-a
z=input("\nZa izlaz pritisnite bilo koje dugme") 