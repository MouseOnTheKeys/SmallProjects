# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:48:28 2020

@author: Nenad
"""

import random

# =============================================================================
# n = int(input("Uneti koeficijent: " ))
# 
# def generisanje(n):    
#     broj = random.sample(range(1,100), n)
#     return broj
# 
# print(generisanje(n))
# 
# =============================================================================

def generisanje():
    n = int(input("Uneti koeficijent: \t" ))
    a = int(input("Uneti tacku a: \t"))
    broj = [random.randint(0,100) for i in range(n)]
    return broj, n, a

#print(generisanje())

def smartPower():
    lista, n, a = generisanje()
    print(lista)
    suma = 0
    
    for i in range(n):
        suma += lista[i]*a**i
    return suma
    
print(smartPower())