# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:45:07 2020

@author: Nenad Bubalo

"""


import random
from time import clock
import matplotlib.pyplot as plt

#randlist = [random() for x in range(10000)] ne valja mora celi brojevi

def getnewlist(nums):
    """Funkcija koja vraca listu od (n) random brojeva """
    return [random.randint(1, 100000) for x in range(nums)] # Vraca novu generisanu listu random CELIH brojeva


def bubble(numbers): # Bubble tip sortiranja implementacija
    """Funkcija sortiranja liste tip Bubble"""
    nums = len(numbers)
    #print(nums)
    for i in range(nums):
        for j in range( i + 1, nums):
            if numbers[j] < numbers[i]: # da li je sledeci num manji od trenutnog
                numbers[j], numbers[i] = numbers[i], numbers[j] #ako jeste zameni
                

def shuttle(numbers): #Shuttle (insertion) vrsta sortiranja implementacijom
    """Funkcija sortiranja liste tipa insertion ili Shutter"""
    for index in range(1, len(numbers)):
    
        currentvalue = numbers[index]
        position = index
        
        while position > 0 and numbers[position - 1] > currentvalue: #while true check if num should carry on being compared
            numbers[position] = numbers[position - 1] # ubacivanje num pre num upravo poredjenih var
            position -= 1 # smanjenje pozicije variable za 1
        
        numbers[position] = currentvalue

def selection_sort(numbers):
    """Funkcija sortiranja liste postupkom izbora (selecct-sort)"""
    for index in range(len(numbers)):

        min_idx = index
        for j in range( index +1, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
# Zamena minimalne vrednosti sa uporedjivanom vrednosti

        numbers[index], numbers[min_idx] = numbers[min_idx], numbers[index]


               
def test(sorttype, unsortedlist):
    """Test algoritama za sortiranje koji pravi kopije liste i ponovn izvrsava zbog tacnosti"""
    
    #komada [:] vraca celokupnu kopiju liste i pravi od njega novi objekat KOPIRA
    copy = unsortedlist[:]
    start = clock() # Setuje reme startovanja
    sorttype(copy) # Pokrece sortiranje kopijom liste i vraca u njen argument
    duration  = clock() - start #izracunava koliko je bilo potrebno algoritmu da se izvrsi
    
    return duration

def produceresults(startnumofnums=1, endnumofnums=2000, increment=50):
    """Plotuje grafik random liste i vremena izvrsavanja za svaki algoritam."""
    xvals = []
    ybubble = []
    yshuttle = []
    yselection_sort = []
    
    for i in range(startnumofnums, endnumofnums, increment):
        listtosort = getnewlist(i)[:] 
        xvals.append(i) #dodaje trenutni broj od brojeva u listu od vaznosti po xu
        ybubble.append(test(bubble, listtosort)) #doda vreme vracanja od sortiranja algoritma u yval listu
        yshuttle.append(test(shuttle, listtosort)) #doda vreme vracanja od sortiranja algoritma u yval listu
        yselection_sort.append(test(selection_sort, listtosort)) # doda vreme vracanja od sortiranja algoritma u yval listu
    plt.plot(xvals, ybubble, color="r", label="Bubble") # Linija plota za Bubble
    plt.plot(xvals, yselection_sort, color="g", label="Selection") # Linija plota za Selection
    plt.plot(xvals, yshuttle, color="b", label="Shuttle") # Linije plota za Shuttle
    plt.xlabel("broj brojeva u random listi") #Label za x osu
    plt.ylabel("Vreme Sortiranja / sekunde") #Label za y osu
    plt.title("Vreme potrebno da algoritam sortiranja - sortira random listu")
    plt.legend(loc=2) #legenda gornji levi ugao
    plt.show() 
    
from Vreme_Dijagram import getnewlist, bubble, shuttle, test, selection_sort

randomlist = getnewlist(500) #Lista od 500 random izabranih celih brojeva
#print(randomlist) # mogucnost da isprinta random brojeve koji su korisceni
print("Bubble test izvrsen za: " + str(test(bubble, randomlist)) + " sekundi.")
print("Shuttle test izvrsen za: " + str(test(shuttle, randomlist)) + "sekundi.")
print("Selection izvrsen za: " + str(test(selection_sort, randomlist)) + "sekundi.")

produceresults(1, 500, 10) # Graficka komparacija izmedju algoritama na listi velicine izmedju 1 i 500, sa uvecanjima od 20
