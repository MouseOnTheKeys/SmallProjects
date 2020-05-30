# -*- coding: utf-8 -*-
"""
Created on Mon May  19:30:57 2020

@author: Nenad Bubalo 1060/19

Domaci zadatak 13:
   1.   U programskom jeziku Python, napisati funkciju koja rekurzivno proveravada li je dati string palindrom.
        String je palindrom ako se s desna na levo i s leva na desno isto čita
    
"""

# Funkcija koja rekurzivno proverava string
def palindrom(x):
    if len(x) < 2:
        return True
    else:
        if x[0] == x[-1]:
            return palindrom(x[1:-1])
        else:
            return False


if __name__ == "__main__":

    # Unos trazenog stringa
    niska = str(input('Uneti zeljeni "string":'))

    if palindrom(niska) == True:
        print('Provera "stringa" !!! \nTrazeni string je Palindrom.\n')
    else:
        print('Provera "stringa" !!! \nTrazena string NIJE Palindrom.\n')
