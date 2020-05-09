# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:43:57 2020

@author: Nenad Bubalo 1060/19

Domaci zadatak 11:
    Napisati korake merge sort-a za dati niz [20 80 40 25 60 30].
    
"""

def mergeSort(lista):
    print("Podela niza: ",lista)
    if len(lista)>1:
        sredina = len(lista)//2
        levapolovina = lista[:sredina]
        desnapolovina = lista[sredina:]

        mergeSort(levapolovina)
        mergeSort(desnapolovina)

        i=0
        j=0
        k=0
        while i < len(levapolovina) and j < len(desnapolovina):
            if levapolovina[i] <= desnapolovina[j]:
                lista[k]=levapolovina[i]
                i=i+1
            else:
                lista[k]=desnapolovina[j]
                j=j+1
            k=k+1

        while i < len(levapolovina):
            lista[k]=levapolovina[i]
            i=i+1
            k=k+1

        while j < len(desnapolovina):
            lista[k]=desnapolovina[j]
            j=j+1
            k=k+1
    print("Spajanje Niza: ",lista)

if __name__ == '__main__':
    
    lista = [20, 80, 40, 25, 60, 30]
    mergeSort(lista)
    print("\nSortirana lista Merge nacinom sortiranja je: {}".format(lista))